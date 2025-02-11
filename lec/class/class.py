# class
# 💡 코드의 중복을 줄이고 재사용성을 갖추기 위한 체계 필요

# 클래스 정의
class YalcoChicken:
    # 생성자 (constructor)
    # __init__ 메서드는 객체 인스턴스를 생성할 때 자동 호출
    #  self는 인스턴스를 참조하는 첫 번째 인자
    def __init__(self, no, name):
        # 인스턴스 속성 (instance attribute)
        self.no = no
        self.name = name

    # 인스턴스 메소드
    # 메소드 method : 클래스에 속한 함수
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



class Button:
    def __init__(self, imprint, spaces):
        self.imprint = imprint
        self.spaces = spaces
    
    def place(self):
        print(f"각인: ${self.imprint}, 공간: {self.spaces}")


buttons = [
    Button("0", 2),
    Button("1", 1),
    Button("=", 3)
]

for button in buttons:
    button.place()
    

# 각인: $0, 공간: 2
# 각인: $1, 공간: 1
# 각인: $=, 공간: 3



# Ex.

class Slime:
    def __init__(self):
        self.hp = 50.0
        self.attack = 8.0
        self.defense = 0.2
        
    def attack_enemy(self, enemy):
        print('📌')
        enemy.hp -= self.attack * (1 - enemy.defense)



slime_1 = Slime()
slime_2 = Slime()

slime_1.attack_enemy(slime_2)

pass

while slime_1.hp > 0:
    slime_2.attack_enemy(slime_1)

# 📌
# 📌
# 📌
# 📌
# 📌
# 📌
# 📌
# 📌
# 📌