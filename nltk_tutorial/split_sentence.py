import nltk
from nltk.tokenize import sent_tokenize

# 如果使用的是nltk的第一次，需要下载punkt资源
nltk.download('punkt')

# 示例文本
text = "This is an example sentence. Here is another one! And what about this one? Let's try it out."

# 将文本切分为句子
sentences = sent_tokenize(text)

# 输出切分后的句子
for i, sentence in enumerate(sentences):
    print(f"Sentence {i+1}: {sentence}")