import torch
from modules.tokenizer import BPETokenizer

bpe_tokenizer = BPETokenizer()

text_data = ''
with open('data/traning_input_txt.txt', 'r+') as f:
    text_data = f.read()


input_tokens = torch.tensor(bpe_tokenizer.encoder(text_data), dtype=torch.long)

traning_data_count = int(0.9 * input_tokens)

print(traning_data_count)


