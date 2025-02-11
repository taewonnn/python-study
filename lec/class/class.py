# class
# 💡 코드의 중복을 줄이고 재사용성을 갖추기 위한 체계 필요

# 클래스 정의
class YalcoChicken:
    # 생성자 (constructor)
    def __init__(self, no, name):
        # 인스턴스 속성 (instance attribute)
        self.no = no
        self.name = name

    # 인스턴스 메소드
    # 메소드 -> 클래스에 속한 함수
    def intro(self):
        return f"안녕하세요, 얄코치킨 {self.no}호 {self.name}점입니다!"


# 인스턴스 생성 (생성자 호출)
store_1 = YalcoChicken(1, "강남")
store_2 = YalcoChicken(2, "판교")


# 인스턴스가 클래스에 속하는지 확인
store_type = type(store_1).__name__ # 💡 인스턴스가 속한 클래스의 이름을 반환
store_is_yc = isinstance(store_1, YalcoChicken)

print(store_type) # YalcoChicken
print(store_is_yc) # True
print(store_1.intro()) # 안녕하세요, 얄코치킨 1호 강남점입니다!

pass


