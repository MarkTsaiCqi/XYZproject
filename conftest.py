"""
conftest.py — 全局 pytest 設定
- web_driver / mobile_driver fixture（自動 quit）
- FAIL 時截圖並嵌入 pytest-html report
"""
import os
import base64
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

try:
    from webdriver_manager.chrome import ChromeDriverManager
    _WDM_AVAILABLE = True
except ImportError:
    _WDM_AVAILABLE = False

# ── 常數 ─────────────────────────────────────────────────────────────────────
SCREENSHOTS_DIR = os.path.join(os.path.dirname(__file__), "reports", "screenshots")

_MOBILE_EMULATION = {
    "deviceMetrics": {"width": 393, "height": 851, "pixelRatio": 2.75, "touch": True},
    "userAgent": (
        "Mozilla/5.0 (Linux; Android 11; Pixel 5) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/144.0.0.0 Mobile Safari/537.36"
    ),
}

# ── Driver 建構工具 ───────────────────────────────────────────────────────────
def _build_options(mobile: bool = False, headless: bool = False) -> webdriver.ChromeOptions:
    options = webdriver.ChromeOptions()
    if mobile:
        options.add_experimental_option("mobileEmulation", _MOBILE_EMULATION)
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    return options


def _make_driver(options: webdriver.ChromeOptions):
    selenium_url = os.getenv("SELENIUM_REMOTE_URL")
    if selenium_url:
        print(f"\n🌐 Selenium Grid: {selenium_url}")
        return webdriver.Remote(command_executor=selenium_url, options=options)
    if _WDM_AVAILABLE:
        print("\n💻 Local Chrome (webdriver-manager)")
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return webdriver.Chrome(options=options)


# ── Fixtures ──────────────────────────────────────────────────────────────────
@pytest.fixture
def web_driver():
    """Desktop Chrome（headless）。用於首頁、email 登入等測試。"""
    driver = _make_driver(_build_options(mobile=False, headless=True))
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture
def mobile_driver():
    """Pixel 5 mobile emulation（non-headless）。用於 Google OAuth 等測試。"""
    driver = _make_driver(_build_options(mobile=True, headless=False))
    yield driver
    driver.quit()


# ── FAIL 截圖 → 嵌入 pytest-html ─────────────────────────────────────────────
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # 只在 test 本體（call phase）失敗時截圖
    if report.when != "call" or not report.failed:
        return

    driver = item.funcargs.get("mobile_driver") or item.funcargs.get("web_driver")
    if not driver:
        return

    # 存截圖
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = (
        item.name.replace("/", "_").replace(":", "_")
                 .replace("[", "_").replace("]", "_")
    )
    png_path = os.path.join(SCREENSHOTS_DIR, f"{safe_name}_{timestamp}.png")

    try:
        # 如果 driver 目前停在已關閉的 popup 視窗，先切回第一個可用視窗
        handles = driver.window_handles
        if handles:
            driver.switch_to.window(handles[0])
        driver.save_screenshot(png_path)
        print(f"\n📸 Screenshot: {png_path}")
    except Exception as exc:
        print(f"\n⚠️  Screenshot failed: {exc}")
        return

    # 用相對路徑嵌入截圖（避開 Jenkins CSP 對 data: URI 的限制）
    try:
        from pytest_html import extras as html_extras
        reports_dir = os.path.join(os.path.dirname(__file__), "reports")
        rel_path = os.path.relpath(png_path, reports_dir).replace(os.sep, "/")
        extra = getattr(report, "extras", [])
        extra.append(
            html_extras.html(
                f'<div><b>Failure Screenshot</b><br>'
                f'<img src="{rel_path}" '
                f'style="max-width:1200px;border:1px solid #ccc;margin-top:6px"/></div>'
            )
        )
        report.extras = extra
    except Exception as exc:
        print(f"⚠️  Embed screenshot failed: {exc}")
