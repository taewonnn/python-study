from bs4 import BeautifulSoup
import json

# HTML 파일 읽기
with open("../test.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# BeautifulSoup 파싱
soup = BeautifulSoup(html_content, "html.parser")

# 데이터 추출
data_list = []

# 모든 체크박스 input 태그 순회
for input_tag in soup.find_all("input", {"type": "checkbox"}):
    code = input_tag.get("value")  # 지역 코드 추출

    # input과 연결된 label 태그의 텍스트를 가져오기
    label_tag = soup.find("label", {"htmlFor": input_tag.get("id")})
    name = label_tag.text.strip() if label_tag else None  # label이 존재하면 텍스트 가져오기

    if code and name:  # code와 name 둘 다 존재해야 추가
        # parent_code는 code의 앞 2글자로 설정
        parent_code = code[:2]  # 부모 코드는 항상 앞의 두 자리 숫자
        

        data_list.append({
            "code": code,
            "name": name,
            "parent_code": parent_code
        })

# 결과를 JSON 파일로 저장
with open("local_third.json", "w", encoding="utf-8") as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=4)
