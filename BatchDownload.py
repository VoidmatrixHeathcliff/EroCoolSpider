import subprocess
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

input_link = input("请输入列表链接：")
raw_link = input_link[0:input_link.find('/', 20)]
content = requests.get(input_link, headers=headers)
content_html = BeautifulSoup(content.text, 'lxml')
list_html = content_html.find('ul', class_='slists')
for ele in list_html.find_all('a'):
    subprocess.Popen('python main.py ' + raw_link + ele.get('href'), creationflags=subprocess.CREATE_NEW_CONSOLE)