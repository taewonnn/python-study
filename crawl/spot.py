import requests 
from bs4 import BeautifulSoup
import json
import re

# HTML 파일 읽기
with open("../spot.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# BeautifulSoup 파싱
soup = BeautifulSoup(html_content, "html.parser")

categories = {
    "store": [],       # 스토어 데이터 저장
    "multiplex": [],   # 복합몰 데이터 저장
    "brand": []        # 브랜드 데이터 저장
}

# 괄호 안 숫자 추출 함수
def extract_count(name):
    match = re.search(r'\(([\d,]+)\)', name)  # 괄호 안 숫자 추출
    if match:
        return int(match.group(1).replace(',', ''))  # 쉼표 제거 후 정수형 변환
    return 0

# 카테고리 별 데이터(이름 + 개수 + 고유번호) - 스토어
for store_input in soup.find_all("input", id=lambda x: x and x.startswith("loc_target_plus_store_")):
    name = store_input['data-name']
    code = store_input['data-code']
    count = extract_count(name)  # 숫자 추출
    categories["store"].append({"name": name, "code": code, "count": count})

# 카테고리 별 데이터(이름 + 개수 + 고유번호) - 복합몰
for store_input in soup.find_all("input", id=lambda x: x and x.startswith("loc_target_plus_multiplex_")):
    name = store_input['data-name']
    code = store_input['data-code']
    count = extract_count(name)  # 숫자 추출
    categories["multiplex"].append({"name": name, "code": code, "count": count})

# 카테고리 별 데이터(이름 + 개수 + 고유번호) - 브랜드
for store_input in soup.find_all("input", id=lambda x: x and x.startswith("loc_target_plus_brand_")):
    name = store_input['data-name']
    code = store_input['data-code']
    count = extract_count(name)  # 숫자 추출
    categories["brand"].append({"name": name, "code": code, "count": count})

# 결과 출력
print(categories)

# JSON 파일로 저장
with open('spot.json', 'w', encoding='UTF-8') as file:
    json.dump(categories, file, ensure_ascii=False, indent=2)
