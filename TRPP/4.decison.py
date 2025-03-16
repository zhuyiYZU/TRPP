import csv

# 初始化count变量
count = 0
total_rows = 0

# 使用with open读取CSV文件
with open('step3.Grammly/MT/technology.csv', mode='r', newline='', encoding='utf8') as file:
    reader = csv.reader(file)

    for row in reader:
        total_rows += 1
        if row[2] == row[0] or row[3] == row[0] or row[4] == row[0]:
            count += 1

# 计算比例
proportion = count / (total_rows - 1) if total_rows > 1 else 0  # 减去标题行

print(f'Count: {count}, Proportion: {proportion}')
