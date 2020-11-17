from bs4 import BeautifulSoup
import requests

from operator import itemgetter

keyword = input('검색어를 입력하세요.\n>>>')
url = 'http://www.google.co.kr/search?q='+keyword

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
data = ''

for span_tag in soup.find_all( 'span', { 'class' : 'st' } ):
    text = span_tag.text
    text = text.replace('.', '').replace(',', '')
    data = data + text + ' '

used_words = dict()
length = len(data) - 1
parsed_list = []

f = open('list.txt','r')

while True:
    line = f.readline()

    if not line: break

    line = line.replace('\n', '')
    parsed_list.append(line)

for i in range (0, length, 1):
    word = ''

    while data[i] != ' ' and i < length:
        word += data[i]
        i += 1

    if word in used_words:
        used_words[word] += 1
        continue

    if len(word) > 1 and word in parsed_list:
        used_words[word] = 1
        
sorted_words = sorted( used_words.items(), key = itemgetter(1), reverse = True)

if sorted_words:
    print("\n('단어',사용빈도)\n")
    print(sorted_words)
else:
    print('사용된 단어 중 위키백과 5000단어와 일치하는 단어가 없습니다.')

f.close()