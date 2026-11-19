from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def get_driver():
    # 1. 创建配置对象
    options = Options()
    
    # 2. 核心配置：告诉浏览器在无屏幕环境下运行
    options.add_argument("--headless=new")       # 开启无头模式
    options.add_argument("--no-sandbox")         # 禁用沙箱（GitHub Actions 必须加，否则权限报错）
    options.add_argument("--disable-dev-shm-usage") # 解决内存限制问题
    options.add_argument("--disable-gpu")        # 禁用 GPU 硬件加速
    options.add_argument("--window-size=1920,1080") # 设置分辨率

    # 3. 把 options 传进去
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.implicitly_wait(10)
    return driver
