from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    """商品页面对象（列表页 + 详情页）"""

    # 列表页定位器
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")

    # 详情页定位器
    DETAIL_NAME = (By.CLASS_NAME, "inventory_details_name")
    DETAIL_PRICE = (By.CLASS_NAME, "inventory_details_price")
    BACK_BUTTON = (By.ID, "back-to-products")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_sort(self, option_value):
        """
        选择排序方式
        :param option_value: 'az' (名称A-Z), 'za' (名称Z-A), 'lohi' (价格低到高), 'hilo' (价格高到低)
        """
        # 使用 Select 类处理下拉框
        from selenium.webdriver.support.ui import Select
        dropdown = self.wait.until(EC.visibility_of_element_located(self.SORT_DROPDOWN))
        select = Select(dropdown)
        select.select_by_value(option_value)

    def get_all_item_names(self):
        """获取当前列表页所有商品名称"""
        elements = self.wait.until(EC.presence_of_all_elements_located(self.ITEM_NAMES))
        return [el.text for el in elements]

    def get_all_item_prices(self):
        """获取当前列表页所有商品价格（返回浮点数列表）"""
        elements = self.wait.until(EC.presence_of_all_elements_located(self.ITEM_PRICES))
        return [float(el.text.replace("$", "")) for el in elements]

    def click_first_item(self):
        """点击第一个商品的名称进入详情页"""
        names = self.wait.until(EC.presence_of_all_elements_located(self.ITEM_NAMES))
        names[0].click()

    def get_detail_name(self):
        """获取详情页的商品名称"""
        return self.wait.until(EC.visibility_of_element_located(self.DETAIL_NAME)).text

    def click_back_to_products(self):
        """详情页点击返回商品列表"""
        self.wait.until(EC.element_to_be_clickable(self.BACK_BUTTON)).click()