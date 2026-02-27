import requests

def download_training_data():
    url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'
    res = requests.get(url=url)
    with open('traning_input_txt.txt', 'w+') as f:
        f.write(res.text)
    return

download_training_data()

