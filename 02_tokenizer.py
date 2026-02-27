
# custom simple tokenzier  #dipak
class CustomTokenzier:
    def __init__(self, trainig_data_file_path):
        with open(trainig_data_file_path, 'r+') as f:
            content = f.read()
            self.trainig_data = content

    def get_all_unique_chars_from_traning_txtdata(self):
        chars = ''
        for char in list(set(self.trainig_data)):
            chars+= char
        return chars
    
        # ' '.join(chars) # this will also so same thigs, may can be more optimal

    def encode(self):
        pass

    def decoder(self):
        pass


tokenzier = CustomTokenzier('traning_input_txt.txt')
print(tokenzier.get_all_unique_chars_from_traning_txtdata())


#tiktoken -- Byte Pair Encoding (BPE) Tokenizer is the ting that ChatGPT uses for tokenzing the input txt

