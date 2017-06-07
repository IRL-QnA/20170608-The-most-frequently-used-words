from bs4 import BeautifulSoup
import requests
html = requests.get(input("url을 입력하세요.")).text
print(html)