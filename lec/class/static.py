# 정적 / 클래스 요소

# 인스턴스가 각 매장이라면 클래스는 본사입니다. 
# 본사가 갖고 있고 모든 매장들에 동일하게 적용되는 요소들입니다.


class YalcoChicken:
    # 클래스 변수
    company_name = "yalco"
    
    # 클래스 메소드
    # 첫 인자로 해당 클래스를 가리키는 cls 받음
    # 클래스와 인스턴스에서 모두 사용 가능
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name
        

    # 정적 메소드
    # 클래스의 상태와 무관한 메소드
    # 클래스와 인스턴스에서 모두 접근 가능
    @staticmethod
    def tax_investigation():
        return "세무자료"
        

    def __init__(self, no, name):
        self.no = no
        self.name = name

    def intro(self):
        return f"안녕하세요, {YalcoChicken.company_name} {self.no}호 {self.name}점입니다!"


pass

# 인스턴스 속성들은 각 매장마다 따로 있지만 클래스 변수는 본사 한 곳에만 위치합니다.


# 클래스 변수는 인스턴스 메소드에서 사용 가능 (반대는 동작X)
store_1 = YalcoChicken(1, "강남")
store_1_intro = store_1.intro() 

yc_company_name = YalcoChicken.company_name # yalco


# class method 사용
YalcoChicken.change_company_name('test')
print(YalcoChicken.company_name) # test



# 정적 메소드도 클래스에서 접근 가능 (인스턴스에서도 가능)
tax_invest_result = YalcoChicken.tax_investigation()





# 자동으로 매장 번호 1올리기

class YalcoChicken:
    company_name = "얄코치킨"
    
    # 다음에 오픈할 매장의 번호
    next_no = 1

    def __init__(self, name):
        self.no = YalcoChicken.next_no
        self.name = name
        YalcoChicken.next_no += 1

    def intro(self):
        return f"안녕하세요, {YalcoChicken.company_name} {self.no}호 {self.name}점입니다!"
      
      
store_1 = YalcoChicken("강남")
store_2 = YalcoChicken("판교")
store_3 = YalcoChicken("제주")

print(store_1.intro())
print(store_2.intro())
print(store_3.intro())

pass



class Button:
    dark_mode = False
    
    def __init__(self, imprint, spaces):
        self.imprint = imprint
        self.spaces = spaces
        
    @classmethod
    def toggle_darak_mode(cls):
        cls.dark_mode = not cls.dark_mode
        

buttons = [
    Button("0", 2),
    Button("1", 1),
    Button("=", 3)
]

mode_before = Button.dark_mode
print(mode_before) # False


Button.toggle_darak_mode()
mode_after = Button.dark_mode
print(mode_after) # True