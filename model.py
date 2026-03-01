import torch
from modules.tokenizer import BPETokenizer

bpe_tokenizer = BPETokenizer()

text_data = ''
with open('data/traning_input_txt.txt', 'r+') as f:
    text_data = f.read()


input_tokens = bpe_tokenizer.encoder(text_data)
print(input_tokens)


