# pypi.org
import requests # 2.28.2            

url1='https://iamawesome.com'
url2='https://ru.wikipedia.org/wiki/Facebook'

response=requests.get(url2)
text=response.text

with open('text.html', 'w',encoding="utf-8") as file:
    file.write(text)
    