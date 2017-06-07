from bs4 import BeautifulSoup
import requests

from operator import itemgetter # sort용

keyword = input('검색어를 입력해주세요.\n>>> ')
url = 'http://www.google.co.kr/search?q='+keyword

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

data = ''

for span_tag in soup.find_all('span', { 'class' : 'st' }):
    text = span_tag.text
    text = text.replace('.', '').replace(',', '')

    data = data + text + ' '


# 이제 자주 나오는 단어들을 찾아 볼 거임.

used_words = dict() # 딕셔너리 자료형

length = len(data) - 1

for i in range(0, length, 1):
    word = ''

    # 띄어쓰기를 기준으로 단어를 구분 할 거임.
    while data[i] != ' ' and i < length :
        word = word + data[i]
        i += 1
    
    # 이미 추가했던 단어면 값만 +1 해줌
    if word in used_words:
        used_words[word] += 1
        continue
    
    # 새로운 단어 추가
    if word != '':
        used_words[word] = 0

sorted_words = sorted(used_words.items(), key = itemgetter(1), reverse = True)

print("\n('단어', 사용빈도)\n")
for i in range (0, 6):
    print(sorted_words[i])