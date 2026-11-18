import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 1. 全局的 WebDriver Fixture
@pytest.fixture(scope="function")
def driver():
    """
    每个测试用例执行前启动浏览器，执行后关闭。
    加入了无头模式，方便在 GitHub Actions 上运行。
    """
    chrome_options = Options()
    # 重要：在 GitHub Actions 等 Linux 服务器上运行，必须加下面两个参数
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')  # 设置窗口大小防报错

    # 初始化 driver
    driver = webdriver.Chrome(options=chrome_options)
    # 隐式等待，兜底防报错
    driver.implicitly_wait(10)

    yield driver  # 将 driver 交给你在测试用例中使用

    # 用例结束后退出浏览器
    driver.quit()


# 2. 自动截图并附加到 Allure 报告的钩子函数
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    监听测试用例的执行结果。如果失败，自动截图并附着到 Allure 报告。
    """
    outcome = yield
    rep = outcome.get_result()

    # 只在用例执行阶段（call）且失败（failed）时截图
    if rep.when == "call" and rep.failed:
        # 从测试用例的参数中获取 driver（前提是你的用例传了 driver 这个 fixture）
        driver = item.funcargs.get('driver')
        if driver:
            # 截图并附加到 Allure 报告
            allure.attach(
                driver.get_screenshot_as_png(),
                name="失败截图_" + item.name,
                attachment_type=allure.attachment_type.PNG
            )