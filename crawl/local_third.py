from bs4 import BeautifulSoup
import json
import re  # 정규식을 위한 모듈

# HTML 파일 읽기
with open("../test2.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# BeautifulSoup 파싱
soup = BeautifulSoup(html_content, "html.parser")

# 데이터 추출
data_list = []

# 모든 체크박스 input 태그 순회
for input_tag in soup.find_all("input", {"type": "checkbox"}):
    code = input_tag.get("value")  # 지역 코드 추출
    parent_code =  code[:2]  # 앞 2글자 사용)

    # data-name에서 괄호와 "XXX구"를 제거한 이름 가져오기
    data_name = input_tag.get("data-name")
    if data_name:
        # 1. 괄호 제거
        name = re.sub(r'\(.*?\)', '', data_name).strip()
        
        # 2. "XXX구"와 같은 부분 제거 (단, "전체"로 끝나는 이름은 제외)
        if not name.endswith("전체"):  # "전체" 예외 처리
            name = re.sub(r'.+(구|시|군)\s*', '', name).strip()

        # 데이터를 리스트에 추가
        data_list.append({
            "code": code,
            "name": name,  # 최종 처리된 이름
            "parent_code": parent_code
        })

# 결과를 JSON 파일로 저장
with open("local_third.json", "w", encoding="utf-8") as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=4)

print("JSON 파일 저장 완료!")
