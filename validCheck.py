from datetime import datetime

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        print("输入错误：金额必须是数字。")
        return False

def is_valid_input_choice(input_data, default_value):
    try:
        input_data = int(input_data)
    except ValueError:
        print("输入错误：选项为数字")
        return False
    return True if input_data in default_value else False

def is_valid_input_data(amount):
    try:
        amount = float(amount)
    except ValueError:
        print("输入错误：金额必须是数字。")
        return False
    return True

