from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """登录页面对象"""

    # 定位器（所有元素集中管理）
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """打开登录页面"""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        """执行登录操作"""
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT)).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        """获取错误提示信息"""
        try:
            error_element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
            return error_element.text
        except:
            return None

    def is_login_successful(self):
        """验证是否登录成功（检查是否跳转到商品页面）"""
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
            return True
        except:
            return False