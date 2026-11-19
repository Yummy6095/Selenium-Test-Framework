import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def get_driver():
    """获取浏览器驱动实例（本地有界面，云端自动无头）"""
    options = Options()


    options.add_argument("--disable-features=PasswordLeakDetection")
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])


    # 是在 GitHub Actions 云端运行
    if os.getenv("GITHUB_ACTIONS") == "true":
        options.add_argument("--headless=new")  # 开启无头模式
        options.add_argument("--no-sandbox")  # 云端必须禁用沙箱
        options.add_argument("--disable-dev-shm-usage")  # 避免内存溢出崩溃
        options.add_argument("--disable-gpu")  # 禁用GPU
        options.add_argument("--window-size=1920,1080")  # 固定窗口大小（云端不能用maximize）

    # ================= 启动浏览器 =================
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # 本地运行（不是云端），再最大化窗口
    if os.getenv("GITHUB_ACTIONS") != "true":
        driver.maximize_window()

    # 加上隐式等待，给云端一点加载时间
    driver.implicitly_wait(10)

    return driver