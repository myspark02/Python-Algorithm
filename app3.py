from ChineseChef import ChineseChef
from Chef import Chef
from ChineseChef import ChineseChef
myChef = Chef("홍길동")
myChef.make_chicken()

myChineseChef = ChineseChef("일지매")
print("중국세프 이름: " + myChineseChef.name)
myChineseChef.make_fried_rice()
myChineseChef.make_salad()
myChineseChef.make_special_dish()