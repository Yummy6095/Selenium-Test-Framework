from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """购物车页面对象"""

    # 定位器
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self):
        """添加背包到购物车"""
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        )
        add_button.click()

    def get_cart_count(self):
        """获取购物车商品数量"""
        try:
            badge = self.wait.until(
                EC.visibility_of_element_located(self.SHOPPING_CART_BADGE)
            )
            return int(badge.text)
        except:
            return 0

    def open_cart(self):
        """打开购物车（增加短暂休眠防止页面跳转过快导致元素失效）"""
        import time
        time.sleep(0.5)
        try:
            cart_link = self.wait.until(EC.element_to_be_clickable(self.SHOPPING_CART_LINK))
            cart_link.click()
        except Exception:
            self.driver.find_element(*self.SHOPPING_CART_LINK).click()

    def get_cart_items_count(self):
        """获取购物车中的商品数量"""
        try:
            items = self.wait.until(
                EC.visibility_of_all_elements_located(self.CART_ITEM)
            )
            return len(items)
        except:
            return 0

    def remove_item_from_cart(self):
        """移除商品（使用 JS 点击增强稳定性）"""
        import time
        time.sleep(0.5)  # 等待列表渲染
        remove_btn = self.wait.until(EC.presence_of_element_located(self.REMOVE_BUTTON))
        try:
            self.driver.execute_script("arguments[0].click();", remove_btn)
        except Exception:
            self.driver.find_element(*self.REMOVE_BUTTON).click()

    def proceed_to_checkout(self):
        """去结算"""
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_btn.click()

    def continue_shopping(self):
        """继续购物（增加等待）"""
        import time
        time.sleep(0.5)
        try:
            continue_btn = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON))
            continue_btn.click()
        except Exception:
            self.driver.find_element(*self.CONTINUE_SHOPPING_BUTTON).click()