import requests 
from bs4 import BeautifulSoup
import json
import re

# HTML 파일 읽기
with open("../spot.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# BeautifulSoup 파싱
soup = BeautifulSoup(html_content, "html.parser")

# 괄호 안 숫자 추출 함수
def extract_count(name):
    match = re.search(r'\(([\d,]+)\)', name)  # 괄호 안 숫자 추출
    if match:
        return int(match.group(1).replace(',', ''))  # 쉼표 제거 후 정수형 변환
    return 0

# 공통 로직 함수: 데이터 수집
def extract_data(prefix):
    data = []
    for store_input in soup.find_all("input", id=lambda x: x and x.startswith(prefix)):
        name = store_input['data-name']
        code = store_input['data-code']
        count = extract_count(name)  # 숫자 추출
        data.append({"name": name, "code": code, "count": count})
    return data

# 데이터 수집
store_data = extract_data("loc_target_plus_store_")
multiplex_data = extract_data("loc_target_plus_multiplex_")
brand_data = extract_data("loc_target_plus_brand_")

# 최종 배열 구성 (요구한 형태로 변환)
categories = [
    {"category": "Store", "items": store_data},
    {"category": "Multiplex", "items": multiplex_data},
    {"category": "Brand", "items": brand_data},
]

# JSON 파일로 저장
with open('spot.json', 'w', encoding='UTF-8') as file:
    json.dump(categories, file, ensure_ascii=False, indent=2)
