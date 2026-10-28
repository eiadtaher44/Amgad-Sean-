class MyAge:
    def __init__(self,age):
        if (age < 0):
            raise ValueError("age <0 ")
        self.__age=age
    def SetAge(self,a):
        if a<0:
            raise ValueError("age <0 ")
        self.__age=a

    def GetAge(self):
        print(f'the age is({self.__age})')
    def printinfo(self):
        print(f'the age is({self.__age})')


obj1=MyAge(21)
# obj1.SetAge(-55)
# obj1.GetAge()
obj1.printinfo()