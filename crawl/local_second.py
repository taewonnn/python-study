from bs4 import BeautifulSoup
import json

# response = requests.get("https://naver.com")
# soup = BeautifulSoup(response.text, "html.parser")
# print("Title:", soup.title.string if soup.title else "No title found")



with open("../test.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# print(html_content)

# bs4
soup = BeautifulSoup(html_content, "html.parser")

print(soup)

# data 추출
data_list = []

for input_tag in soup.find_all("input", {"type": "checkbox"}):  # 체크박스 input 태그 검색
    code = input_tag.get("value")  # 지역 코드
    name = input_tag.get("data-name")  # 이름
    
    if code and name:
        # parent_code는 code의 앞 2글자로 설정
        parent_code = code[:2]  # 부모 코드는 항상 앞의 두 자리 숫자
        
        data_list.append({
            "code": code,
            "name": name,
            "parent_code": parent_code
        })
        

with open("local_second.json", "w", encoding="utf-8") as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=4)