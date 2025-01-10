import requests 
from bs4 import BeautifulSoup


# infinitie scroll crawl

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get('https://www.wart.co.kr/exec/front/Product/ApiProductNormal?cate_no=32&display_group=8&supplier_code=S0000000&page=3&bInitMore=F&count=16', headers=headers)

data = response.json()
productList = data['rtn_data']['data']

for product in productList :
  print(f"Product Name: {product['product_name_striptag']}")
  print(f"Price: {product['disp_product_price']}")
  print(f"Link: {product['seo_url']}")
  print("---")
