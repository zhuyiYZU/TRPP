import csv

import_file = 'FuExp/MT/technology_prompt_pre.csv'
output_file_PATH = 'FuExp/MT/technology_prompt.csv'
# 打开CSV文件
with open(import_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    # 读取所有行
    extracted_texts = []
    for row in reader:
        if row:  # 确保行不为空
            # 假设目标内容在第一列，提取出 "The prompt used for generating this text could be:" 后面的部分
            label = row[0]
            ori_text = row[1]
            text = row[2]
            try:
                # 使用 split 方法按第一个 '.' 分割，并去除多余的空格和引号
                extracted_text = text.split('.', 1)[1].strip(' "')
                extracted_text = extracted_text.strip('"""')

            except IndexError:
                # 如果没有 '.'，则返回原始文本
                extracted_texts.append(text)
            extracted_texts.append((label, ori_text, extracted_text))

# 输出提取的内容
for extracted_text in extracted_texts:
    print(extracted_text)

# 如果你想将结果保存到一个新的CSV文件中
with open(output_file_PATH, mode='w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file)
    for extracted_text in extracted_texts:
        writer.writerow(extracted_text)

# 读取已生成的文件并过滤掉第一列为 "T" 的行
filtered_texts = []
with open(output_file_PATH, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] != 'T':  # 保留第一列不等于 "T" 的行
            filtered_texts.append(row)

# 将过滤后的结果重新写入输出文件
with open(output_file_PATH, mode='w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(filtered_texts)

print("过滤完成，输出文件中已删除所有第一列值为 'T' 的行")
