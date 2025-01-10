import requests 
from bs4 import BeautifulSoup

# response = requests.get("https://naver.com")
# soup = BeautifulSoup(response.text, "html.parser")
# print("Title:", soup.title.string if soup.title else "No title found")



response = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')

# print(response.content)


# BeautifulSup -> encoding
soup = BeautifulSoup(response.content, "html.parser")
# print(soup)


# 특정 요소 찾기 - 현재가
# find_all('태그명', 속성명)
print('현재가: ',soup.find_all('strong',id='_nowVal')[0].text)
print('거래량: ',soup.find_all('span',id='_quant')[0].text)

#class명으로 가져올 땐 class_)
print('거래량: ',soup.find_all('span',class_='tah')[5].text)


print('현재가: ',soup.find_all('span', class_='blind')[14].text)


# selector

# class
# print(soup.select('.f_down'))
# id
# print(soup.select('#_nowVal'))
# 태그
# print(soup.select('strong'))

# > >
print(soup.select('.gray .f_down em')[0].text)

# 이미지 수집
img = soup.select('#img_chart_area')[0]
print(img['src']) # https://ssl.pstatic.net/imgfinance/chart/item/area/day/005930.png?sidcode=1736493365250




print('---------------------')

sub = ['005930', '066575', '005380', '035720', '034220', '003490']


# 함수로 변경
# =>  f'문자열{}'
def crawlingValue (code) :
  data = requests.get(f'https://finance.naver.com/item/sise.nhn?code={code}')
  
  soup = BeautifulSoup(data.content, 'html.parser')
  price = soup.select('#_nowVal')[0].text
  print(soup.select('#_nowVal')[0].text)
  return price



f = open('a.csv', 'w')
for i in range(6) :
  f.write('\n' + crawlingValue(sub[i]))
f.close()