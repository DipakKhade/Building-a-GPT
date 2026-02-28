from typing import List

# custom simple tokenzier  #dipak

class CustomTokenzier:
    trainig_data = ''
    unique_chars = ''

    encoding_mapper: dict[str: int] = {}
    decoding_mapper: dict[int: str] = {}

    def __init__(self, trainig_data_file_path):
        with open(trainig_data_file_path, 'r+') as f:
            content = f.read()
            CustomTokenzier.trainig_data: str = content
            CustomTokenzier.unique_chars: str = CustomTokenzier.get_all_unique_chars_from_traning_txtdata()
            CustomTokenzier.set_encoding_decoding_mapping()

    @staticmethod
    def get_all_unique_chars_from_traning_txtdata() -> str:
        chars = ''
        x = list(set(CustomTokenzier.trainig_data))
        x.sort()
        for char in x:
            chars+= char
        return chars
    
    @staticmethod
    def set_encoding_decoding_mapping() -> None :
        CustomTokenzier.encoding_mapper = [ {char: index} for index, char in enumerate(CustomTokenzier.unique_chars) ]
        CustomTokenzier.decoding_mapper = [ {index: char} for index, char in enumerate(CustomTokenzier.unique_chars) ]
        return

    @staticmethod
    def encode(input_txt: str) -> List[int]:
        encodings = []
        for char in input_txt:
            for encoded_char in CustomTokenzier.encoding_mapper:
                if char == list(encoded_char.keys())[0]:
                    encodings.append(encoded_char[char])
        return encodings

    @staticmethod
    def decoder(encodings: list[int]):
        decoding = []
        for encode in encodings:
            for decode_int in CustomTokenzier.decoding_mapper:
                if encode == list(decode_int.keys())[0]:
                    decoding.append(decode_int[encode])
        return ''.join(decoding)

encoded_txt = CustomTokenzier('traning_input_txt.txt').encode('my name is dipak.')
decoded_txt = CustomTokenzier('traning_input_txt.txt').decoder(encoded_txt) 

print(encoded_txt, decoded_txt)




#tiktoken -- Byte Pair Encoding (BPE) Tokenizer is the ting that ChatGPT uses for tokenzing the input txt
import tiktoken
print('hii')
t = tiktoken.encoding_for_model("gpt-4o")
print('hello')

tiktoken_encoded_txt = t.encode('my name is dipak.')
tiktoken_decoded_txt = t.decode(tiktoken_encoded_txt)

print(tiktoken_encoded_txt, tiktoken_decoded_txt)


