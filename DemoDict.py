# DemoDict.py
colors = {"apple":"red", "banana":"yellow"}
print(len(colors))
#입력
colors["kiwi"] = "green"
#검색
print(colors["apple"])

for item in colors.items():
    print(item)

phone = {"kim":"111", "lee":"222", "park":"333"}
print("kim" in phone)
print("kang" not in phone)
p = phone
print(p)
print(phone)
print(id(phone), id(p))
p["kang"] = "1234"
print(p)
print(phone)
print(id(phone), id(p))
print(phone["kim"])

#원본과 별도의 복사본을 생성하는 경우
import copy
device = {"아이폰":5, "아이패드":10}
# 별도의 복사본을 생성
device2 = copy.deepcopy(device)
# 선택한 블록 주석 처리 : ctrl + /
device2["맥북"] = 20
print(device)
print(device2)
