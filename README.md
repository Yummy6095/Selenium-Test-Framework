🧪 Selenium + Pytest 自动化测试框架
基于 Python + Selenium + Pytest 的 Web UI 自动化测试框架，采用 Page Object Model 分层设计， 覆盖 saucedemo 电商站点的登录、商品浏览、购物车与结算全流程，共 15 条用例。
Python Selenium Pytest POM Cases
📖 项目简介
本项目针对电商网站 saucedemo 实现登录、商品列表、购物车与下单结算的自动化回归测试。 通过 Page Object Model 将页面元素与业务逻辑分离，用例层只描述业务动作，页面层统一维护定位与操作， 从而降低维护成本、提升脚本可读性与复用性。
用例覆盖 正向流程、异常场景与边界场景，并按 P0 / P1 / P2 划分优先级。
🛠 技术栈
技术	版本	用途
Python	3.12	编程语言
Selenium	4.x	Web UI 自动化
Pytest	8.x	测试框架与用例管理
WebDriverManager	latest	浏览器驱动自动管理
Page Object Model	—	页面与逻辑分层设计
Allure	2.x	测试报告与截图
Git	—	版本控制
📁 项目结构
Selenium-Test-Framework/
├── selenium_test/
│   ├── pages/                  # 页面对象层
│   │   ├── login_page.py       # 登录页
│   │   ├── product_page.py     # 商品列表 / 详情页
│   │   ├── cart_page.py        # 购物车页
│   │   └── checkout_page.py    # 结算页
│   ├── tests/                  # 测试用例层
│   │   ├── test_login.py       # 登录 / 购物车 / 结算（TC-001 ~ TC-009）
│   │   └── test_product.py     # 商品 / 购物车 / 结算补充（9 条新增用例）
│   ├── utils/
│   │   └── driver.py           # 浏览器驱动封装
│   └── reports/                # 测试报告与截图
├── requirements.txt
├── .gitignore
└── README.md
✅ 测试覆盖
模块	用例数	用例编号	脚本
登录模块	3	TC-001 ~ TC-003	test_login.py
商品模块	3	TC-PROD-003 ~ 005	test_product.py
购物车模块	6	TC-004 ~ 008、TC-CART-005	test_login.py / test_product.py
结算模块	3	TC-009、TC-ORDER-002 ~ 003	test_login.py / test_product.py
合计	15	—	—
用例清单
编号	模块	用例标题	类型	优先级
TC-001	登录	标准用户登录成功	冒烟测试	P0
TC-002	登录	锁定用户登录失败	异常测试	P1
TC-003	登录	错误密码登录失败	异常测试	P1
TC-004	购物车	添加商品到购物车	功能测试	P0
TC-005	购物车	多次添加购物车数量累加	功能测试	P1
TC-006	购物车	从购物车移除商品	功能测试	P1
TC-007	购物车	购物车内容页面间保持	功能测试	P1
TC-008	购物车	空购物车无法结算	边界测试	P1
TC-009	结算	完整结算流程	端到端测试	P0
TC-PROD-003	商品	商品价格从低到高排序	功能测试	P1
TC-PROD-004	商品	商品名称 Z-A 排序	功能测试	P1
TC-PROD-005	商品	列表页与详情页信息一致	功能测试	P2
TC-CART-005	购物车	添加多个不同商品	功能测试	P1
TC-ORDER-002	结算	结算必填项为空拦截	异常测试	P1
TC-ORDER-003	结算	完整下单后返回首页	业务闭环	P2
测试结果：15 / 15 全部通过 ✅

==================== 15 passed ====================
🚀 快速开始
1. 克隆项目
git clone https://github.com/Yummy695/Selenium-Test-Framework.git
cd Selenium-Test-Framework
2. 安装依赖
pip install -r requirements.txt
3. 运行测试
cd selenium_test
pytest tests/ -v
只跑某个模块：
pytest tests/test_login.py -v      # 登录 / 购物车 / 结算
pytest tests/test_product.py -v    # 商品 / 排序 / 下单闭环
4. 生成 Allure 报告（可选）
pytest tests/ --alluredir=./reports/allure-results
allure serve ./reports/allure-results

📊 测试报告
运行结束后，Allure 报告输出至 selenium_test/reports/allure-results
失败用例自动截图，随报告按步骤展示
截图可放入 docs/ 目录，在 README 中通过相对路径引用
## 🔄 CI 说明
项目接入 GitHub Actions，每次提交代码自动执行全部测试，执行完成后自动生成并上传 Allure 报告。
