import requests

def download_training_data():
    url = 'https://www.gutenberg.org/cache/epub/7864/pg7864.txt'
    res = requests.get(url=url, stream=True, timeout=30, headers={
        'User-Agent': 'Mozilla/5.0'
    })
    with open('traning_input_txt.txt', 'w+') as f:
        f.write(res.text)
    return

download_training_data()

