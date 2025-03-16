import csv

import pandas as pd

# 读取相似度结果
df = pd.read_csv('diffPrompt/P2/similarity_DT_pubmed_prompt_final.csv')

# 预测标签
predicted_labels = []
for similarity in df['similarity']:
    predicted_label = 2 if similarity > 0.91 else 1
    predicted_labels.append(predicted_label)

# 添加预测标签列
df['predicted_label'] = predicted_labels

# 保存预测结果到CSV文件
df.to_csv('diffPrompt/P2/label_similarity_DT_pubmed_prompt_final.csv', index=False)
print("预测标签完成并已保存到文件")

with open('diffPrompt/P2/label_similarity_DT_pubmed_prompt_final.csv', 'r', encoding='utf-8', errors='ignore') as file:
    count = 0
    reader = csv.reader(file)
    total = 0
    for row in reader:
        total += 1
        if row[0] == row[4]:
            count += 1
print(f'{count}')
print(f'{total-1}')
print(f"预测acc={count/(total-1)}")