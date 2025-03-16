import pandas as pd
import torch
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertTokenizer, BertModel
import numpy as np
import io

# 读取CSV文件
with open('diffPrompt/P2/DT_pubmed_prompt_final.csv', 'rb') as f:
    content = f.read().decode('utf-8', errors='ignore')
df = pd.read_csv(io.StringIO(content))
# df = pd.read_csv('LZL/M_ok.csv', errors='ignore')

# 加载预训练的BERT模型和tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_bert_embedding(text):
    if not isinstance(text, str):
        text = str(text)
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).cpu().detach().numpy()

# 为每一行计算相似度
similarities = []
for index, row in df.iterrows():
    embedding_col2 = get_bert_embedding(row[1])
    embedding_col3 = get_bert_embedding(row[2])
    similarity = cosine_similarity(embedding_col2, embedding_col3)[0][0]
    similarities.append(similarity)

# 将相似度写入第四列
df['similarity'] = similarities

# 保存中间结果到CSV文件
df.to_csv('diffPrompt/P2/similarity_DT_pubmed_prompt_final.csv', index=False)
print("相似度计算完成并已保存到文件")







