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
        for char in list(set(CustomTokenzier.trainig_data)):
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
    def decoder():
        pass


CustomTokenzier('traning_input_txt.txt').encode('Before')


#tiktoken -- Byte Pair Encoding (BPE) Tokenizer is the ting that ChatGPT uses for tokenzing the input txt

