from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def get_driver():
    """获取浏览器驱动实例（已禁用密码泄露检测）"""
    options = Options()

    # 1. 彻底禁用密码泄露检测（核心）
    options.add_argument("--disable-features=PasswordLeakDetection")

    # 2. 禁用密码保存和自动填充服务（辅助）
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)

    # 3. (可选) 关闭顶部的“Chrome正受到自动测试软件控制”提示
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver