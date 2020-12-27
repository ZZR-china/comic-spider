import requests
from requests.exceptions import RequestException

def get_one_page(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}

    response = requests.get(url, headers=headers)

    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def main():
    url = 'https://www.baidu.com/'
    html = get_one_page(url)
    print(html)

if __name__ == '__main__':
    main()