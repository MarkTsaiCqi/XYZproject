from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import BaseAction

"""
    封装登录页面的可操作元素
"""
# ── 定位器 ────────────────────────────────────────────────────────────────────
# Modal 觸發入口（現版首頁用 Start Chatting）
LOGIN_TRIGGER = By.XPATH, "//*[contains(text(), 'Start Chatting') or contains(text(), 'Start chatting') or contains(text(), 'Create Agent')]"

# Modal 內元素
LOGIN_EMAIL_INPUT  = By.CSS_SELECTOR, "input[placeholder='example@site.com']"
# 箭頭按鈕是 email input 的 following-sibling button
EMAIL_NEXT_BUTTON  = By.XPATH, "//input[@placeholder='example@site.com']/following-sibling::button"
LOGIN_PASSWORD_INPUT = By.CSS_SELECTOR, "input[placeholder='Password']"
MODAL_CLOSE_BUTTON = By.XPATH, "//dialog//button[.//img] | //div[@role='dialog']//button[contains(@class,'close')]"
EMAIL_ERROR_MSG    = By.XPATH, "//*[contains(text(),'format error') or contains(text(),'Mailbox')]"
MODAL_DIALOG       = By.CSS_SELECTOR, "dialog[open], [role='dialog']"

# 登入後出現的元素（logged-in indicator）
# 登入成功後「Start Chatting」消失，header 右側會出現使用者 avatar/icon
LOGGED_IN_INDICATOR = By.XPATH, "//main[not(.//*[contains(text(),'Start Chatting')])]"

# 第三方登入
GOOGLE_LOGIN_BUTTON    = By.XPATH, "//dialog//*[contains(text(),'Google')]/ancestor::*[@role='button' or self::button][1]"
MICROSOFT_LOGIN_BUTTON = By.XPATH, "//dialog//*[contains(text(),'Microsoft')]/ancestor::*[@role='button' or self::button][1]"
GITHUB_LOGIN_BUTTON    = By.XPATH, "//dialog//*[contains(text(),'GitHub')]/ancestor::*[@role='button' or self::button][1]"


class LoginPage:
    def __init__(self, driver):
        self.driver = BaseAction(driver)
        self._raw_driver = driver

    # ── 觸發登入 Modal ────────────────────────────────────────────────────────
    def open_login_modal(self):
        """點擊 Start Chatting 開啟登入 Modal"""
        self.driver.base_click(LOGIN_TRIGGER)

    def input_email(self, email):
        """輸入 Email"""
        self.driver.base_input(LOGIN_EMAIL_INPUT, email)

    def click_email_next(self):
        """點擊 email 右側箭頭按鈕"""
        self.driver.base_click(EMAIL_NEXT_BUTTON)

    def input_password(self, password):
        """輸入密碼"""
        self.driver.base_input(LOGIN_PASSWORD_INPUT, password)

    def submit_login_with_enter(self):
        """在密碼欄位按 Enter 送出"""
        self.driver.base_input(LOGIN_PASSWORD_INPUT, Keys.RETURN)

    def close_modal(self):
        """點擊 X 關閉 Modal"""
        self.driver.base_click(MODAL_CLOSE_BUTTON)

    def login_with_email(self, email, password):
        """完整 Email 登入流程"""
        self.open_login_modal()
        self.input_email(email)
        self.click_email_next()
        self.input_password(password)
        self.submit_login_with_enter()

    # ── 驗證輔助 ──────────────────────────────────────────────────────────────
    def is_modal_visible(self) -> bool:
        """回傳 Modal 目前是否顯示"""
        try:
            el = WebDriverWait(self._raw_driver, 3).until(
                EC.presence_of_element_located(MODAL_DIALOG)
            )
            return el.is_displayed()
        except Exception:
            return False

    def get_email_error_message(self) -> str:
        """取得 email 欄位的錯誤訊息文字（無則回傳空字串）"""
        try:
            el = WebDriverWait(self._raw_driver, 3).until(
                EC.presence_of_element_located(EMAIL_ERROR_MSG)
            )
            return el.text
        except Exception:
            return ""

    def is_email_next_button_enabled(self) -> bool:
        """回傳箭頭按鈕是否為可點擊狀態"""
        try:
            el = self.driver.find_element(EMAIL_NEXT_BUTTON)
            return el.is_enabled()
        except Exception:
            return False

    def check_login_user(self) -> str:
        """登入後取得用戶識別文字；可依實際 UI 調整 locator"""
        try:
            # 等待 Start Chatting 消失，代表已登入
            WebDriverWait(self._raw_driver, 10).until(
                EC.invisibility_of_element_located(LOGIN_TRIGGER)
            )
            return "logged_in"
        except Exception:
            return ""

    # ── scene_login.py 相容介面（保持舊名稱可呼叫）────────────────────────────
    def input_login_button(self):
        self.open_login_modal()

    def input_account(self, email):
        self.input_email(email)

    def input_user_next(self):
        self.click_email_next()

    def click_login(self):
        self.submit_login_with_enter()

    # ── 第三方登入 ────────────────────────────────────────────────────────────
    def click_google_login(self):
        self.driver.base_click(GOOGLE_LOGIN_BUTTON)

    def click_microsoft_login(self):
        self.driver.base_click(MICROSOFT_LOGIN_BUTTON)

    def click_github_login(self):
        self.driver.base_click(GITHUB_LOGIN_BUTTON)

