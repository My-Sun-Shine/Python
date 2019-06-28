import csv
import pandas as pd
# pandas模块写入和读取csv文件 ##########################################################################################################
books = []
book = {
    '书名': '笑傲江湖',
    '作者': '金庸',
}
# 如果 book 条数足够多的话，pandas 会每次往文件中写 50 条数据。
books.append(book)
for i in range(0, 100):
    books.append(book)
data = pd.DataFrame(books)
# 写入csv文件,'a+'是追加模式,w是写入模式，会覆盖的
data.to_csv('PythonBook.csv', header=True,
            index=False, mode='w', encoding='utf-8')

data = pd.read_csv("PythonBook.csv")
# print(data)
print(data.count())
print('---'*30)
# csv模块写入和读取csv文件 ##########################################################################################################
with open('data.csv', 'w', newline="") as f:
    # delimiter为空格，此时输出结果的每一列就是以空格分隔了
    writer = csv.writer(f, delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    # 这里不需要readlines
    for line in reader:
        print(line)
print('---'*30)
# 写入字典格式数据
fieldnames = ['id', 'name', 'age']  # 标题名称
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  # 先写入头信息
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})

# a 为追加模式 encoding='utf-8' 设置写入中文
with open('data.csv', 'a', encoding='utf-8', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id': '10005', 'name': '王伟', 'age': 22})
# 如果CSV文件中包含中文的话，还需要指定文件编码
with open("data.csv", "r", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # 这里不需要readlines
    for line in reader:
        print(line)
