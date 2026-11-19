import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    options = Options()
    
    # 1. 无头模式
    options.add_argument("--headless=new") 
    
    # 2. 禁用沙箱
    options.add_argument("--no-sandbox") 
    
    # 3. 防止内存溢出崩溃
    options.add_argument("--disable-dev-shm-usage") 
    
    # 4. 禁用 GPU 硬件加速
    options.add_argument("--disable-gpu")
    
    # 5. 设置窗口大小
    options.add_argument("--window-size=1920,1080")

    # 启动浏览器
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    # 关闭浏览器
    driver.quit()

# 失败自动截图并附到 Allure 报告
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="失败截图_" + item.name,
                attachment_type=allure.attachment_type.PNG
            )
