import re

pattern = r'^\d{6}-[1-4]\d{7}$'

def validate_resident_number(number):
    return re.match(pattern, number) is not None

# 테스트 케이스
test_numbers = [
    "910101-1123456",   # 유효: 형식이 올바르고 마지막 숫자가 1, 7개의 숫자가 이어짐
    "960304-23456789",  # 무효: 마지막 숫자가 9 (범위를 벗어남)
    "750513-3123456",   # 유효: 형식이 올바르고 마지막 숫자가 3, 7개의 숫자가 이어짐
    "820601-4123456",   # 유효: 형식이 올바르고 마지막 숫자가 4, 7개의 숫자가 이어짐
    "990812-1234567",   # 무효: 마지막 숫자가 7 (범위를 벗어남)
    "123456-1234567",   # 무효: 잘못된 형식
    "910101-123456",    # 무효: 숫자가 7개가 아님
    "910101-12345678",  # 무효: 숫자가 7개가 아님
]

for number in test_numbers:
    if validate_resident_number(number):
        print(f"{number}는(은) 유효한 주민등록번호입니다.")
    else:
        print(f"{number}는(은) 유효하지 않은 주민등록번호입니다.")
