"""
Login 功能自動化測試
對應 TC-001：https://github.com/MarkTsaiCqi/XYZproject
"""
import pytest
import config
from page.login import LoginPage


# ── 共用 fixture ──────────────────────────────────────────────────────────────
@pytest.fixture
def login_page(web_driver):
    web_driver.get(config.URL)
    return LoginPage(web_driver)


# ── A 群組：Modal 開關行為 ─────────────────────────────────────────────────────
class TestLoginModal:

    def test_A001_open_modal_via_start_chatting(self, login_page):
        """A-001：點擊 Start Chatting 應開啟登入 Modal"""
        login_page.open_login_modal()
        assert login_page.is_modal_visible(), "Login modal should be visible after clicking Start Chatting"

    def test_A002_close_modal_with_x_button(self, login_page):
        """A-002：點擊 X 應關閉 Modal"""
        login_page.open_login_modal()
        assert login_page.is_modal_visible()
        login_page.close_modal()
        assert not login_page.is_modal_visible(), "Modal should be closed after clicking X"

    def test_A004_close_modal_with_escape(self, login_page, web_driver):
        """A-004：按 ESC 應關閉 Modal"""
        from selenium.webdriver.common.keys import Keys
        login_page.open_login_modal()
        assert login_page.is_modal_visible()
        web_driver.find_element(*("tag name", "body")).send_keys(Keys.ESCAPE)
        assert not login_page.is_modal_visible(), "Modal should be closed after pressing Escape"


# ── B 群組：Email 驗證 ────────────────────────────────────────────────────────
class TestEmailValidation:

    def test_B002_empty_email_button_disabled(self, login_page):
        """B-002：空白 email 時，箭頭按鈕應為 disabled"""
        login_page.open_login_modal()
        assert not login_page.is_email_next_button_enabled(), \
            "Arrow button should be disabled when email is empty"

    def test_B003_invalid_email_format_shows_error(self, login_page):
        """B-003：格式錯誤的 email 送出後應顯示錯誤訊息"""
        login_page.open_login_modal()
        login_page.input_email("notanemail")
        login_page.click_email_next()
        error = login_page.get_email_error_message()
        assert error != "", f"Expected error message, got empty string"

    def test_B004_email_with_spaces_rejected(self, login_page):
        """B-004：前後有空白的 email 應被拒絕（已知 bug BUG-001：應 auto-trim）"""
        login_page.open_login_modal()
        login_page.input_email("  user@test.com  ")
        login_page.click_email_next()
        error = login_page.get_email_error_message()
        # 目前行為：顯示格式錯誤（BUG-001 待修）
        # 預期行為：應自動 trim 並通過驗證
        assert error != "", "BUG-001: spaces in email should ideally be trimmed, currently shows error"

    def test_B005_overlength_email_rejected(self, login_page):
        """B-005：超過 254 字元的 email 應被拒絕（已知 bug BUG-002）"""
        long_email = "a" * 247 + "@test.com"  # 257 chars
        login_page.open_login_modal()
        login_page.input_email(long_email)
        login_page.click_email_next()
        # 預期：顯示錯誤或 modal 停留
        # 目前行為（BUG-002）：直接進入建號流程
        assert login_page.is_modal_visible() or login_page.get_email_error_message() != "", \
            "BUG-002: overlength email (>254 chars) should be rejected"


# ── D 群組：UI 驗證 ───────────────────────────────────────────────────────────
class TestLoginUI:

    def test_D001_modal_elements_present(self, login_page, web_driver):
        """D-001：Modal 應包含 email input、4 個 OAuth 按鈕、X 按鈕"""
        from selenium.webdriver.common.by import By
        login_page.open_login_modal()
        assert web_driver.find_element(By.CSS_SELECTOR, "input[placeholder='example@site.com']")
        for provider in ["Wallet", "Google", "Microsoft", "GitHub"]:
            assert web_driver.find_element(
                By.XPATH, f"//dialog//*[contains(text(),'{provider}')]"
            ), f"{provider} button not found in modal"

    def test_D002_privacy_policy_link(self, login_page, web_driver):
        """D-002：Privacy Policy 連結應可開啟對應頁面"""
        from selenium.webdriver.common.by import By
        login_page.open_login_modal()
        link = web_driver.find_element(By.XPATH, "//dialog//a[contains(text(),'Privacy')]")
        href = link.get_attribute("href")
        assert "Privacy" in href or "privacy" in href, f"Unexpected Privacy Policy URL: {href}"

    def test_D003_terms_of_service_link(self, login_page, web_driver):
        """D-003：Terms of Service 連結應可開啟對應頁面"""
        from selenium.webdriver.common.by import By
        login_page.open_login_modal()
        link = web_driver.find_element(By.XPATH, "//dialog//a[contains(text(),'Terms')]")
        href = link.get_attribute("href")
        assert "Terms" in href or "terms" in href, f"Unexpected Terms of Service URL: {href}"
