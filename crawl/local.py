from bs4 import BeautifulSoup
import json
import re

# HTML 파일 읽기
with open("../local.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# BeautifulSoup 파싱
soup = BeautifulSoup(html_content, "html.parser")

# 시/도 데이터 추출
first_local = []
for city_input in soup.find_all("input", class_="chk_loc_target_plus_1st"):
    city_code = city_input["value"]
    city_name = re.sub(r"\([^)]*\)", "", city_input["data-name"]).strip()  # () 제거
    first_local.append({"code": city_code, "name": city_name})

# 구/군 데이터 추출
second_local = []
for district_input in soup.find_all("input", class_="chk_loc_target_plus_2nd"):
    district_code = district_input["value"]
    district_name = re.sub(r"\([^)]*\)", "", district_input["data-name"]).strip()  # () 제거
    parent_code = district_code[:2]  # 부모 코드: 시/도 코드
    second_local.append({"code": district_code, "name": district_name, "parent_code": parent_code})

# 동/읍/면 데이터 추출
third_local = []
for town_input in soup.find_all("input", class_="chk_loc_target_plus_3rd"):
    town_code = town_input["value"]
    town_name = re.sub(r"\([^)]*\)", "", town_input["data-name"]).strip()  # () 제거
    parent_code = town_code[:4]  # 부모 코드: 구/군 코드
    third_local.append({"code": town_code, "name": town_name, "parent_code": parent_code})

# JSON 파일로 저장
with open("first_local.json", "w", encoding="utf-8") as file:
    json.dump(first_local, file, ensure_ascii=False, indent=4)

with open("second_local.json", "w", encoding="utf-8") as file:
    json.dump(second_local, file, ensure_ascii=False, indent=4)

with open("third_local.json", "w", encoding="utf-8") as file:
    json.dump(third_local, file, ensure_ascii=False, indent=4)

print("시/도, 구/군, 동/읍/면 데이터가 각각 JSON 파일로 저장되었습니다.")
