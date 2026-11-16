import pytest
import allure
from utils.driver import get_driver
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("核心业务流程测试")
class TestSauceDemo:

    def setup_method(self):
        self.driver = get_driver()
        self.login_page = LoginPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.login_page.open()

    def teardown_method(self):
        """安全退出浏览器"""
        try:
            if self.driver:
                self.driver.quit()
        except Exception as e:
            print(f"清理浏览器时发生异常: {e}")
    # ========== 登录模块 ==========

    @allure.story("登录模块")
    @allure.title("TC-001: 标准用户登录成功")
    def test_login_with_standard_user(self):
        with allure.step("输入标准用户名和密码并登录"):
            self.login_page.login("standard_user", "secret_sauce")
        with allure.step("验证是否成功进入商品列表页"):
            assert self.login_page.is_login_successful() == True

    @allure.story("登录模块")
    @allure.title("TC-002: 锁定用户登录失败")
    def test_login_with_locked_out_user(self):
        with allure.step("输入锁定用户账号并尝试登录"):
            self.login_page.login("locked_out_user", "secret_sauce")
        with allure.step("获取错误提示并验证内容包含 'locked out'"):
            error_msg = self.login_page.get_error_message()
            assert error_msg is not None
            assert "locked out" in error_msg.lower()

    @allure.story("登录模块")
    @allure.title("TC-003: 错误密码登录失败")
    def test_login_with_wrong_password(self):
        with allure.step("输入错误密码并尝试登录"):
            self.login_page.login("standard_user", "wrong_password")
        with allure.step("获取错误提示并验证内容"):
            error_msg = self.login_page.get_error_message()
            assert error_msg is not None
            assert "username and password" in error_msg.lower()

    # ========== 购物车模块 ==========

    @allure.story("购物车模块")
    @allure.title("TC-004: 添加商品到购物车")
    def test_add_item_to_cart(self):
        with allure.step("登录系统"):
            self.login_page.login("standard_user", "secret_sauce")
        with allure.step("点击背包商品的'Add to cart'按钮"):
            self.cart_page.add_backpack_to_cart()
        with allure.step("验证购物车角标数量为 1"):
            assert self.cart_page.get_cart_count() == 1

    @allure.story("购物车模块")
    @allure.title("TC-005: 多次添加购物车数量累加")
    def test_cart_count_increases(self):
        with allure.step("登录系统"):
            self.login_page.login("standard_user", "secret_sauce")
        with allure.step("第一次添加商品"):
            self.cart_page.add_backpack_to_cart()
            assert self.cart_page.get_cart_count() == 1
        with allure.step("验证数量正确累加（暂留作后续扩展）"):
            pass

    @allure.story("购物车模块")
    @allure.title("TC-006: 从购物车移除商品")
    def test_remove_item_from_cart(self):
        with allure.step("登录并添加商品到购物车"):
            self.login_page.login("standard_user", "secret_sauce")
            self.cart_page.add_backpack_to_cart()
            assert self.cart_page.get_cart_count() == 1
        with allure.step("进入购物车页面"):
            self.cart_page.open_cart()
        with allure.step("点击移除按钮"):
            self.cart_page.remove_item_from_cart()
        with allure.step("验证购物车内商品数量为 0"):
            assert self.cart_page.get_cart_items_count() == 0

    @allure.story("购物车模块")
    @allure.title("TC-007: 购物车内容页面间保持")
    def test_cart_persistence(self):
        with allure.step("登录并添加商品"):
            self.login_page.login("standard_user", "secret_sauce")
            self.cart_page.add_backpack_to_cart()
            assert self.cart_page.get_cart_count() == 1
        with allure.step("进入购物车并确认有商品"):
            self.cart_page.open_cart()
            assert self.cart_page.get_cart_items_count() == 1
        with allure.step("点击继续购物返回列表页，再次进入购物车"):
            self.cart_page.continue_shopping()
            self.cart_page.open_cart()
        with allure.step("验证商品依然存在"):
            assert self.cart_page.get_cart_items_count() == 1

    @allure.story("购物车模块")
    @allure.title("TC-008: 空购物车无法结算")
    def test_empty_cart_checkout_disabled(self):
        with allure.step("登录系统并直接进入购物车"):
            self.login_page.login("standard_user", "secret_sauce")
            self.cart_page.open_cart()
        with allure.step("验证购物车内商品数量为 0"):
            assert self.cart_page.get_cart_items_count() == 0

    # ========== 结算模块 ==========

    @allure.story("结算模块")
    @allure.title("TC-009: 完整结算流程")
    def test_complete_checkout_flow(self):
        with allure.step("登录并添加商品"):
            self.login_page.login("standard_user", "secret_sauce")
            assert self.login_page.is_login_successful()
            self.cart_page.add_backpack_to_cart()
            assert self.cart_page.get_cart_count() == 1
        with allure.step("进入购物车并点击结算"):
            self.cart_page.open_cart()
            self.cart_page.proceed_to_checkout()
        with allure.step("填写收货信息并继续"):
            self.checkout_page.fill_info("Test", "User", "12345")
            self.checkout_page.click_continue()
        with allure.step("点击完成订单"):
            self.checkout_page.click_finish()
        with allure.step("验证订单完成页面显示成功提示"):
            success_msg = self.checkout_page.get_success_message()
            assert "Thank you" in success_msg or "Complete" in success_msg