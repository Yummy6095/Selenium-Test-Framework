from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# ... 在你的 driver fixture 内部 ...
chrome_options = Options()
# 1. 使用新版无头模式
chrome_options.add_argument("--headless=new") 

# 2. 禁用沙箱 (GitHub Actions 环境必需)
chrome_options.add_argument("--no-sandbox") 

# 3. 禁用 /dev/shm 使用 (CI 环境内存优化)
chrome_options.add_argument("--disable-dev-shm-usage") 

# 4. 禁用 GPU (CI 环境不需要)
chrome_options.add_argument("--disable-gpu") 

# 5. 指定窗口大小，避免页面布局异常
chrome_options.add_argument("--window-size=1920,1080")

chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-software-rasterizer")

# 使用 webdriver-manager 自动管理驱动
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
