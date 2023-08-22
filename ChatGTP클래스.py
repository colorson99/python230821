#ChatGTP클래스.py

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def printInfo(self):
        print(f"ID: {self.id}, 이름: {self.name}")

class Manager(Person):
    def __init__(self, id, name, skill, role):
        super().__init__(id, name)
        self.skill = skill
        self.role = role

class Employee(Person):
    def __init__(self, id, name, role):
        super().__init__(id, name)
        self.role = role

# 테스트 케이스
manager = Manager(id=1, name="John Doe", skill="리더십", role="매니저")
employee = Employee(id=2, name="Jane Smith", role="개발자")

manager.printInfo()
print(f"기술: {manager.skill}, 역할: {manager.role}")

employee.printInfo()
print(f"역할: {employee.role}")

manager2 = Manager(id=3, name="Alice Johnson", skill="커뮤니케이션", role="슈퍼바이저")
manager2.printInfo()
print(f"기술: {manager2.skill}, 역할: {manager2.role}")

employee2 = Employee(id=4, name="Bob Brown", role="디자이너")
employee2.printInfo()
print(f"역할: {employee2.role}")

manager3 = Manager(id=5, name="Eva Garcia", skill="문제 해결", role="디렉터")
manager3.printInfo()
print(f"기술: {manager3.skill}, 역할: {manager3.role}")

employee3 = Employee(id=6, name="Sam Wilson", role="품질 관리 엔지니어")
employee3.printInfo()
print(f"역할: {employee3.role}")

manager4 = Manager(id=7, name="Max Roberts", skill="팀 빌딩", role="리드 매니저")
manager4.printInfo()
print(f"기술: {manager4.skill}, 역할: {manager4.role}")

employee4 = Employee(id=8, name="Emily Davis", role="데이터 분석가")
employee4.printInfo()
print(f"역할: {employee4.role}")

manager5 = Manager(id=9, name="Chris Lee", skill="의사 결정", role="프로젝트 매니저")
manager5.printInfo()
print(f"기술: {manager5.skill}, 역할: {manager5.role}")

employee5 = Employee(id=10, name="Alex Turner", role="마케팅 전문가")
employee5.printInfo()
print(f"역할: {employee5.role}")
