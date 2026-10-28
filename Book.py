class Book:
    def __init__(self,Name,Author,Date,RemainingQuantity):
        self.Name=Name
        self.Author=Author
        self.__Date=Date
        self.RemainingQuantity=RemainingQuantity
    def more(self):
        more1=int(input("Enter the more + Quantity : "))
        self.RemainingQuantity+=more1
    def loss(self):
        loss1=int(input("Enter the loss - Quantity : "))
        self.RemainingQuantity-=loss1
    def setdate(self,value):
        self.__Date=value
    def getdata(self):
        print(f'Date : {self.__Date}')
    def printinfo(self):
        print(f'Name : {self.Name}\nAuthor: {self.Author}\nDate: {self.__Date}\nRemainingQuantity {self.RemainingQuantity}')


print("Book 1")
book1=Book("python","amgad",2023,50)
# book1.setdate(2026)
book1.printinfo()
book1.more()
book1.loss()
book1.printinfo()
# book1>Book__Date=70            error


'''print("Book 2")
book2=Book("c++","eaid",2025,120)
# book2.setdate(2018)
book2.printinfo()
book2.more()
book2.loss()
book2.printinfo()


print("Book 3")
book3=Book("php","said",2020,5)
# book3.setdate(2020)
book3.printinfo()
book3.more()
book3.loss()
book3.printinfo()

print("Book 4")
book4=Book("Network","Ahmed",1999,300)
book4.setdate(1999)
book4.printinfo()
book4.more()
book4.loss()
book4.printinfo()


print("Book 5")
book5=Book("html","awab",1980,10)
book5.setdate(1980)
book5.printinfo()
book5.more()
book5.loss()
book5.printinfo()'''