🧪 Selenium + Pytest 自动化测试框架
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-green.svg)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-8.x-orange.svg)](https://docs.pytest.org/)
📖 项目简介
本项目是一个基于 Python + Selenium + Pytest*的 Web 自动化测试框架，针对 [SauceDemo](https://www.saucedemo.com/) 电商网站，实现了登录、购物车、结算流程的自动化测试。
通过 Page Object Model设计模式，将页面元素与业务逻辑分离，提高了脚本的可维护性和可读性。项目共包含 9 个测试用例，覆盖正向场景、异常场景和边界场景。
🛠️ 技术栈
| 技术 | 用途 |
|------|------|
| Python 3.12 | 编程语言 |
| Selenium 4.x | Web 自动化测试 |
| Pytest 8.x | 测试框架 |
| WebDriverManager | 自动管理浏览器驱动 |
| Page Object Model | 设计模式 |
| Git | 版本控制 |
📁 项目结构
Selenium-Test-Framework/
├── selenium_test/
│ ├── pages/ # 页面对象层
│ │ ├── login_page.py # 登录页面
│ │ ├── cart_page.py # 购物车页面
│ │ └── checkout_page.py # 结算页面
│ ├── tests/ # 测试用例层
│ │ └── test_login.py # 测试用例（9个）
│ ├── utils/ # 工具层
│ │ └── driver.py # 浏览器驱动封装
│ └── reports/ # 测试报告目录
├── requirements.txt # 项目依赖
├── .gitignore # Git 忽略文件
└── README.md # 项目说明
🧪 测试用例覆盖
| 模块 | 用例编号 | 测试场景 | 类型 |
|------|----------|----------|------|
| 登录 | TC-001 | 标准用户登录成功 | 正向 |
| 登录 | TC-002 | 锁定用户登录失败 | 异常 |
| 登录 | TC-003 | 错误密码登录失败 | 异常 |
| 购物车 | TC-004 | 添加商品到购物车 | 正向 |
| 购物车 | TC-005 | 多次添加购物车数量累加 | 正向 |
| 购物车 | TC-006 | 从购物车移除商品 | 正向 |
| 购物车 | TC-007 | 购物车内容页面间保持 | 正向 |
| 购物车 | TC-008 | 空购物车无法结算 | 边界 |
| 结算 | TC-009 | 完整结算流程 | 端到端 |
测试结果：9/9 全部通过 ✅
🚀 快速开始
1. 克隆项目
bash
git clone https://github.com/Yummy695/Selenium-Test-Framework.git
cd Selenium-Test-Framework
2.安装依赖
pip install -r requirements.txt
3.运行测试
cd selenium_test
pytest tests/ -v
4.生成html报告
pytest tests/ --html=reports/report.html --self-contained-html
运行结果实例
==================== test session starts ====================
collected 9 items
tests/test_login.py::TestSauceDemo::test_login_with_standard_user PASSED
tests/test_login.py::TestSauceDemo::test_login_with_locked_out_user PASSED
tests/test_login.py::TestSauceDemo::test_login_with_wrong_password PASSED
tests/test_login.py::TestSauceDemo::test_add_item_to_cart PASSED
tests/test_login.py::TestSauceDemo::test_cart_count_increases PASSED
tests/test_login.py::TestSauceDemo::test_remove_item_from_cart PASSED
tests/test_login.py::TestSauceDemo::test_cart_persistence PASSED
tests/test_login.py::TestSauceDemo::test_empty_cart_checkout_disabled PASSED
tests/test_login.py::TestSauceDemo::test_complete_checkout_flow PASSED
==================== 9 passed in 74.89s ====================
