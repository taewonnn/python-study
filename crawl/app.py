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






