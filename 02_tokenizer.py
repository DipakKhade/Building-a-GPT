from typing import List
# custom simple tokenzier  #dipak
class CustomTokenzier:
    trainig_data = ''
    unique_chars = ''
    def __init__(self, trainig_data_file_path):
        with open(trainig_data_file_path, 'r+') as f:
            content = f.read()
            CustomTokenzier.trainig_data = content
            CustomTokenzier.unique_chars = CustomTokenzier.get_all_unique_chars_from_traning_txtdata(CustomTokenzier.trainig_data)

    @staticmethod
    def get_all_unique_chars_from_traning_txtdata():
        chars = ''
        for char in list(set(trainig_data)):
            chars+= char
        return chars
    
        # ' '.join(chars) # this will also so same thigs, may can be more optimal

    @staticmethod
    def encode(input_txt: List[str]) -> List[int]:
        pass

    @staticmethod
    def decoder():
        pass


tokenzier = CustomTokenzier('traning_input_txt.txt')
print(tokenzier.get_all_unique_chars_from_traning_txtdata())


#tiktoken -- Byte Pair Encoding (BPE) Tokenizer is the ting that ChatGPT uses for tokenzing the input txt

