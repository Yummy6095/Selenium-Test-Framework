import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver import get_driver
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage


@allure.feature("商品与扩展业务流程测试")
class TestProductFeatures:

    def setup_method(self):
        self.driver = get_driver()
        self.login_page = LoginPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

        with allure.step("前置操作：打开网站并登录"):
            self.login_page.open()
            self.login_page.login("standard_user", "secret_sauce")
            assert self.login_page.is_login_successful()

    def teardown_method(self):
        """安全退出浏览器"""
        try:
            if self.driver:
                self.driver.quit()
        except Exception as e:
            print(f"清理浏览器时发生异常: {e}")

    @allure.story("商品模块")
    @allure.title("TC-PROD-003: 商品价格从低到高排序")
    def test_sort_by_price_low_to_high(self):
        with allure.step("在下拉框选择价格低到高排序"):
            self.product_page.select_sort("lohi")
        with allure.step("获取当前列表所有商品价格"):
            prices = self.product_page.get_all_item_prices()
        with allure.step("断言价格列表是否为升序排列"):
            assert prices == sorted(prices), f"价格排序错误: {prices}"

    @allure.story("商品模块")
    @allure.title("TC-PROD-004: 商品名称 Z-A 排序")
    def test_sort_by_name_z_to_a(self):
        with allure.step("在下拉框选择名称 Z-A 排序"):
            self.product_page.select_sort("za")
        with allure.step("获取当前列表所有商品名称"):
            names = self.product_page.get_all_item_names()
        with allure.step("断言名称列表是否为降序排列"):
            assert names == sorted(names, reverse=True), f"名称排序错误: {names}"

    @allure.story("商品模块")
    @allure.title("TC-PROD-005: 列表页与详情页商品信息一致")
    def test_product_detail_consistency(self):
        with allure.step("记录列表页第一个商品的名称"):
            names = self.product_page.get_all_item_names()
            first_item_name = names[0]
        with allure.step("点击第一个商品进入详情页"):
            self.product_page.click_first_item()
        with allure.step("获取详情页商品名称并比对"):
            detail_name = self.product_page.get_detail_name()
            assert detail_name == first_item_name, f"详情页名称 {detail_name} 与列表页 {first_item_name} 不一致"
        with allure.step("点击返回按钮，验证返回列表页"):
            self.product_page.click_back_to_products()
            assert "inventory.html" in self.driver.current_url

    @allure.story("购物车模块")
    @allure.title("TC-CART-005: 添加多个不同商品，验证数量累加")
    def test_add_multiple_different_items(self):
        with allure.step("添加第一个商品（背包）"):
            self.cart_page.add_backpack_to_cart()
        with allure.step("添加第二个商品（自行车灯）"):
            from selenium.webdriver.common.by import By
            bike_light_btn = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
            bike_light_btn.click()
        with allure.step("验证购物车角标数量为 2"):
            assert self.cart_page.get_cart_count() == 2

    @allure.story("结算模块")
    @allure.title("TC-ORDER-002: 结算时必填项为空，拦截报错")
    def test_checkout_with_empty_info(self):
        with allure.step("添加商品并进入结算页面"):
            self.cart_page.add_backpack_to_cart()
            self.cart_page.open_cart()
            self.cart_page.proceed_to_checkout()
        with allure.step("不填写任何信息，直接点击继续"):
            self.checkout_page.click_continue()
        with allure.step("验证页面出现错误提示且未跳转"):
            # 注意：这里不要写任何 import，直接用顶部的 WebDriverWait
            error_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
            )
            assert "Error: First Name is required" in error_element.text
            assert "checkout-step-one.html" in self.driver.current_url

    @allure.story("结算模块")
    @allure.title("TC-ORDER-003: 完整下单后，点击返回首页继续购物")
    def test_continue_shopping_after_checkout(self):
        with allure.step("快速完成一次下单流程"):
            self.cart_page.add_backpack_to_cart()
            self.cart_page.open_cart()
            self.cart_page.proceed_to_checkout()
            self.checkout_page.fill_info("Test", "User", "12345")
            self.checkout_page.click_continue()
            self.checkout_page.click_finish()
        with allure.step("在订单完成页点击返回首页按钮"):
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            back_home_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "back-to-products"))
            )
            back_home_btn.click()
        with allure.step("验证是否回到列表页，且购物车已被清空"):
            assert "inventory.html" in self.driver.current_url
            assert self.cart_page.get_cart_count() == 0