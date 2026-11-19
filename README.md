# Selenium + Pytest Web 自动化测试框架

<p align="center">
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12-blue" /></a>
<a href="https://www.selenium.dev/"><img src="https://img.shields.io/badge/Selenium-4.x-green" /></a>
<a href="https://docs.pytest.org/"><img src="https://img.shields.io/badge/Pytest-8.x-orange" /></a>
<a href="https://docs.qameta.io/allure/"><img src="https://img.shields.io/badge/Allure-Report-purple" /></a>
<img src="https://img.shields.io/badge/POM-Design-yellow" />
<img src="https://img.shields.io/badge/15%2F15-PASSED-success" />
</p>> 
> 基于 Python + Selenium + Pytest 的 Web 自动化测试项目，针对 `https://www.saucedemo.com/` 演示电商站点，采用 **Page Object Model** 模式，分离页面元素与业务逻辑，便于维护扩展。集成 GitHub Actions 持续执行 + Allure 可视化报告。

## 🛠️ 技术栈

表格

| 技术 | 用途 |
| --- | --- |
| Python 3.12 | 编程语言 |
| Selenium 4.x | Web 自动化驱动 |
| Pytest 8.x | 测试执行框架 |
| WebDriverManager | 浏览器驱动自动管理 |
| Allure | 可视化测试报告 |
| Page Object Model | 分层设计模式 |
| Git + GitHub Actions | 版本控制 & CI 自动执行 |

## 📁 项目结构

```
Selenium-Test-Framework/
├── selenium_test/
│   ├── pages/                # 页面对象层
│   │   ├── login_page.py     # 登录页面
│   │   ├── inventory_page.py # 商品列表页
│   │   ├── cart_page.py      # 购物车页面
│   │   └── checkout_page.py  # 结算页面
│   ├── tests/                # 测试用例层
│   │   ├── test_login.py     # 登录、购物车、结算基础用例（9条）
│   │   └── test_product.py   # 商品扩展场景用例（6条）
│   ├── utils/                # 工具层
│   │   └── driver.py         # 浏览器驱动封装
│   └── reports/              # Allure报告、截图目录
├── .github/workflows/        # GitHub Actions CI配置
├── requirements.txt          # 项目依赖
├── .gitignore
└── README.md
```

## 🧪 测试用例覆盖

表格

| 模块 | 用例数量 |
| --- | --- |
| 登录模块 | TC-001 ~ TC-003 |
| 购物车模块 | TC-004 ~ TC-008 |
| 结算模块 | TC-009 |
| 商品扩展模块 | TC-010 ~ TC-015 |

> 
> 合计：**15 条测试用例，15/15 全部通过 ✅**

### Allure 报告总览

### Allure 用例详情

### GitHub Actions CI 流水线

## 🚀 快速开始

1. 克隆项目

```
git clone https://github.com/Yummy695/Selenium-Test-Framework.git
cd Selenium-Test-Framework
```

2. 安装依赖

```
pip install -r requirements.txt
```

3. 执行测试并生成 Allure 结果

```
cd selenium_test
pytest tests/ -v --alluredir=reports/allure-results
```

4. 本地打开 Allure 报告

```
allure serve reports/allure-results
```

5. 单独执行指定模块

```
# 只跑登录&购物车结算用例
pytest tests/test_login.py -v
# 只跑商品扩展用例
pytest tests/test_product.py -v
```

## ✅ 运行样例

```
==================== test session starts ====================
collected 15 items
tests/test_login.py::TestSauceDemo::test_login_with_standard_user PASSED
tests/test_login.py::TestSauceDemo::test_login_with_locked_out_user PASSED
tests/test_login.py::TestSauceDemo::test_login_with_wrong_password PASSED
tests/test_login.py::TestSauceDemo::test_add_item_to_cart PASSED
tests/test_login.py::TestSauceDemo::test_cart_count_increases PASSED
tests/test_login.py::TestSauceDemo::test_remove_item_from_cart PASSED
tests/test_login.py::TestSauceDemo::test_cart_persistence PASSED
tests/test_login.py::TestSauceDemo::test_empty_cart_checkout_disabled PASSED
tests/test_login.py::TestSauceDemo::test_complete_checkout_flow PASSED
tests/test_product.py::TestProduct::xxx PASSED
tests/test_product.py::TestProduct::xxx PASSED
tests/test_product.py::TestProduct::xxx PASSED
tests/test_product.py::TestProduct::xxx PASSED
tests/test_product.py::TestProduct::xxx PASSED
tests/test_product.py::TestProduct::xxx PASSED
==================== 15 passed in 92.65s ====================
```

## 🔄 CI 说明

项目接入 GitHub Actions，每次提交代码自动执行全部测试，执行完成后自动生成并上传 Allure 报告
