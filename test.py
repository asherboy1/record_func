from io import TextIOWrapper
from datetime import datetime
import csv

# try:
#     with open('data/record.csv', mode="a", encoding="utf8") as f:
#         if isinstance(f, TextIOWrapper):
#             print("ok")
# except:
#     print("1")

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_expense():
    while True:
        date = input("请输入开销日期 (YYYY-MM-DD): ")
        if not is_valid_date(date):
            print("输入错误：日期格式不正确，请使用 YYYY-MM-DD 格式。")


if __name__ == "__main__":
    import os
    def loads_data():
        files = os.listdir("data/")
        if "record.csv" in files:
            f = open('data/record.csv', mode="a", newline='\n', encoding="utf8")
            print("ok")
            return f
        else:
            f = open('data/record.csv', mode="w", newline='', encoding="utf8")
            writer = csv.writer(f)
            writer.writerow(['日期', '金额', '类别', '描述'])
            return f
    f = loads_data()
    writer = csv.writer(f)
    writer.writerows([(1,2,3,4)])
    f.close()


