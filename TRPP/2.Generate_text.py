import csv
import json

from openai import OpenAI
import codecs
import pandas as pd
import time
list_label = list()
i = 0  # i记录list_label中的位置
label0 = 0
label1 = 0
count_num = 0

client = OpenAI(
    base_url='https://xiaoai.plus/v1',
    # sk-xxx替换为自己的key
    api_key='sk-XXX'  # 3.5
)



def read_csv_row_range(csv_file, start_row, end_row):
    with open(csv_file, 'r', encoding='utf-8', errors='ignore') as file:
        csv_reader = csv.reader(file)
        for index, row in enumerate(csv_reader):
            if start_row <= index + 1 <= end_row:
                yield row


csv_file = 'FuExp/MT/technology_prompt_app.csv'
out_PATH = 'FuExp/MT/technology_prompt_final.csv'
start_row = 0  # 起始行号
end_row = 2  # 结束行号
row_step = 3  # 行步长

str = 'Output in one paragraph, without punctuation or blank lines'



while True:
    messages = []
    # 判断文件的总行数
    with open(csv_file, 'r', encoding='utf-8', errors='ignore') as file:
        csv_reader = csv.reader(file)
        total_lines = sum(1 for _ in csv_reader)

    # 如果剩余的行数小于 row_step，则调整 end_row 为文件的总行数
    if end_row > total_lines:
        end_row = total_lines

    for row in read_csv_row_range(csv_file, start_row, end_row):
        label = row[0]
        ori_text = row[1]
        # content = str + row[1]
        content = row[2] + str
        print("user:" + content)
        messages.append({"role": "user", "content": content})

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        time.sleep(20)
        chat_response = completion
        answer = chat_response.choices[0].message.content
        print(f'LLM: {answer}')
        messages.append({"role": "assistant", "content": answer})
        with open(out_PATH, 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([label, ori_text, answer])

    # 增加起始行号和结束行号
    start_row += row_step
    end_row += row_step

    # 如果已经处理到文件末尾，则跳出循环
    if start_row >= total_lines:
        break








