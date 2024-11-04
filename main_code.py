import io
from io import TextIOWrapper
from validCheck import is_valid_date, is_valid_input_data, is_valid_input_choice
from config import category_dict, function_dict
import csv
import os

def loads_data():
    files = os.listdir("data/")
    if "record.csv" in files:
        f = open('data/record.csv', mode="a", newline='',  encoding="utf8")
        print("读取成功！")
        return f
    else:
        f = open('data/record.csv', mode="w", newline='', encoding="utf8")
        writer = csv.writer(f)
        writer.writerow(['日期', '类别', '开销类别', '金额', '描述'])
        print("读取成功！")
        return f

def insert_data(f):
    InsertData = list()

    while True:
        date = input("请输入开销日期 (YYYY-MM-DD): ")
        if not is_valid_date(date):
            continue
        print("*" * 20)

        print("输入 1-收入 2-支出")
        category = input("请输入开销类别: ")
        if not is_valid_input_choice(category, category_dict):
            print("请按照所提供选项选择！")
            continue
        print("*" * 20)

        promo_str = "输入 1-转账 2-现金" if int(category) == 1 else "输入 1-餐饮 2-交通 3-住宿 4-购物 5-娱乐 6-通讯"
        print(promo_str)
        category_detail = input("请输入开销类别: ")
        if not is_valid_input_choice(category_detail, category_dict[int(category)]):
            print("请按照所提供选项选择！")
            continue
        print("*" * 20)

        amount = input("请输入金额: ")
        if not is_valid_input_data(amount):
            continue
        amount = float(amount)
        print("*" * 20)

        description = input("请输入开销描述: ")

        InsertData.append((date, category, category_detail, amount, description))
    # TODO 优化中途退出、记录为空写入等场景
    _save_data(f, InsertData)
    main()
# TODO 优化
def _save_data(f:io.TextIOWrapper, data:list):
    try:
        writer = csv.writer(f)
        writer.writerows(data)
        print("开销记录成功！")
    except TypeError:
        print("开销记录失败！")
    finally:
        f.close()


def search_data():
    pass

def analyze_data():
    pass


def main():
    """主线程程序，用于接收用户指令"""
    while True:
        print("*" * 20)
        print("输入【1】 录入数据")
        print("输入【2】 查询数据")
        print("输入【3】 分析数据")
        print("输入【4】 退出")
        print("*" * 20)

        code = input("请输入所想完成指令！\n")
        if not is_valid_input_choice(code, function_dict):
            print("请按照所提示选项选择！")
            continue

        code = int(code)
        data = loads_data()
        if not isinstance(data, TextIOWrapper):
            print("插入数据失败，源文件有问题")
            break
            
        if code == 1:
            insert_data(data)
        elif code == 2:
            search_data(data)
        elif code == 3:
            analyze_data(data)
        elif code == 4:
            print("感谢使用！再见！")
            break
        else:
            print("请输入正确指令！")
            continue


if __name__ == "__main__":
    print("ok")