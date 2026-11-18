import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

def create_test_excel():
    # 1. 创建 Excel 工作簿
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "自动化测试用例"

    # 2. 定义表头
    headers = ["用例编号", "所属模块", "测试标题", "前置条件", "测试步骤", "预期结果", "优先级", "测试类型", "自动化脚本"]
    ws.append(headers)

    # 3. 定义 15 条测试用例数据
    data = [
        ["TC-001", "登录模块", "标准用户登录成功", "处于登录页", "1. 输入 standard_user\n2. 输入 secret_sauce\n3. 点击登录", "跳转至商品列表页，显示商品列表", "P0", "冒烟测试", "test_login.py"],
        ["TC-002", "登录模块", "锁定用户登录失败", "处于登录页", "1. 输入 locked_out_user\n2. 输入 secret_sauce\n3. 点击登录", "登录失败，提示“locked out”", "P1", "异常测试", "test_login.py"],
        ["TC-003", "登录模块", "错误密码登录失败", "处于登录页", "1. 输入 standard_user\n2. 输入 wrong_password\n3. 点击登录", "登录失败，提示账号密码不匹配", "P1", "异常测试", "test_login.py"],
        ["TC-004", "购物车模块", "添加商品到购物车", "已登录，处于列表页", "1. 点击背包商品的“Add to cart”按钮", "按钮变为“Remove”，购物车角标显示为1", "P0", "功能测试", "test_login.py"],
        ["TC-005", "购物车模块", "多次添加购物车数量累加", "已登录，处于列表页", "1. 添加背包\n2. 添加车灯", "购物车角标数量正确累加（显示为2）", "P1", "功能测试", "test_login.py"],
        ["TC-006", "购物车模块", "从购物车移除商品", "购物车中有商品", "1. 进入购物车\n2. 点击“Remove”按钮", "商品从购物车移除，角标消失", "P1", "功能测试", "test_login.py"],
        ["TC-007", "购物车模块", "购物车内容页面间保持", "购物车中有商品", "1. 进入购物车\n2. 点击继续购物\n3. 再次进入购物车", "商品依然存在于购物车中，数据未丢失", "P1", "功能测试", "test_login.py"],
        ["TC-008", "购物车模块", "空购物车无法结算", "已登录，购物车为空", "1. 直接进入购物车页面", "购物车列表为空，无结算按钮或不可点击", "P1", "边界测试", "test_login.py"],
        ["TC-009", "结算模块", "完整结算流程", "购物车中有商品", "1. 进入购物车\n2. 点击Checkout\n3. 填写信息\n4. 点击Continue\n5. 点击Finish", "结算成功，跳转至完成页并提示“Thank you”", "P0", "端到端测试", "test_login.py"],
        ["TC-PROD-003", "商品模块", "商品价格从低到高排序", "已登录，处于列表页", "1. 下拉框选择 Price (low to high)", "页面商品列表按价格从低到高排序", "P1", "功能测试", "test_product.py"],
        ["TC-PROD-004", "商品模块", "商品名称 Z-A 排序", "已登录，处于列表页", "1. 下拉框选择 Name (Z to A)", "页面商品列表按名称降序排序", "P1", "功能测试", "test_product.py"],
        ["TC-PROD-005", "商品模块", "列表页与详情页信息一致", "已登录，处于列表页", "1. 记录列表页第一个商品名\n2. 点击进入详情页", "详情页商品名称与列表页一致", "P2", "功能测试", "test_product.py"],
        ["TC-CART-005", "购物车模块", "添加多个不同商品", "已登录，处于列表页", "1. 添加背包\n2. 添加车灯", "购物车角标数量显示为2", "P1", "功能测试", "test_product.py"],
        ["TC-ORDER-002", "结算模块", "结算必填项为空拦截", "购物车有商品，处于结算页", "1. 不填写任何信息\n2. 直接点击Continue", "页面拦截跳转，提示First Name is required", "P1", "异常测试", "test_product.py"],
        ["TC-ORDER-003", "结算模块", "完整下单后返回首页", "完成一次结算", "1. 点击Finish完成订单\n2. 点击Back Home按钮", "跳转回列表页，且购物车角标被清空", "P2", "业务闭环", "test_product.py"]
    ]

    for row in data:
        ws.append(row)

    # 4. 美化样式
    # 定义表头样式（蓝色背景，白色粗体字，居中）
    header_fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")
    header_font = Font(color="FFFFFF", bold=True)
    header_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    # 定义数据行样式（垂直居中，左对齐，自动换行）
    data_alignment = Alignment(vertical="center", horizontal="left", wrap_text=True)
    center_alignment = Alignment(vertical="center", horizontal="center", wrap_text=True)

    # 定义边框
    thin_border = Border(left=Side(style='thin'), right=Side(style='thin'),
                         top=Side(style='thin'), bottom=Side(style='thin'))

    # 应用到表头
    for cell in ws[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = header_alignment
        cell.border = thin_border
    ws.row_dimensions[1].height = 25  # 表头行高

    # 应用到数据行
    for row in ws.iter_rows(min_row=2, max_row=len(data)+1, max_col=len(headers)):
        for cell in row:
            cell.border = thin_border
            # 只有“用例编号、所属模块、优先级、测试类型”居中，其他左对齐
            if cell.column_letter in ['A', 'B', 'G', 'H']:
                cell.alignment = center_alignment
            else:
                cell.alignment = data_alignment

    # 5. 设置列宽（确保内容能显示完整）
    column_widths = {
        'A': 15,  # 用例编号
        'B': 12,  # 所属模块
        'C': 20,  # 测试标题
        'D': 20,  # 前置条件
        'E': 35,  # 测试步骤 (宽一点)
        'F': 35,  # 预期结果 (宽一点)
        'G': 8,   # 优先级
        'H': 12,  # 测试类型
        'I': 18   # 自动化脚本
    }
    for col, width in column_widths.items():
        ws.column_dimensions[col].width = width

    # 6. 保存文件
    file_name = "自动化测试用例.xlsx"
    wb.save(file_name)
    print(f"✅ 成功生成完美的 Excel 文件: {file_name}")

if __name__ == "__main__":
    create_test_excel()