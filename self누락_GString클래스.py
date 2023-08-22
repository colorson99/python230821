str = "Not Class Member"
class GString:
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #버그(모호한 것보다는 명시적인 것이 좋다)
        print(str)

g = GString()
g.set("First Message")
g.print()
