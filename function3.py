#function3.py
#가변 인자 처리
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#함수를 호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

#람다함수(이름이 없는 간단한 함수정의)
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())

print("---필터함수---")
lst = [10,25,30]
iterL = filter(None,lst)
for item in iterL:
    print(item)

print("---람다함수정의---")    
iterL = filter(lambda x:x>20,lst)
for item in iterL:
    print(item)