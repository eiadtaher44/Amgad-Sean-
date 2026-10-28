class Device:
    def __init__(self,brand,):
        self.brand=brand
        def showBrand(self):
            print("brand is :",self.brand)

class Phone(Device):
    def __init__(self,brand,screensize):
        Device.__init__(self,brand)
        self.screensize=screensize
    def makecall(self):
        print("screensize :",self.screensize)


class Camera(Device):
    def __init__(self,brand,resulation):
        Device.__init__(self,brand)
        self.resulation=resulation
        def takephoto(self):
            print("resulation :",self.resulation)

class smartPhone(Phone,Camera):
    def __init__(self,brand,screensize,resulation):
        Phone.__init__(self,brand,screensize)
        Camera.__init__(self,brand,resulation)
    def showsmartphonedetails(self):
            print(f'brand : ({self.brand})\nscreensize: ({self.screensize})\nresulation: ({self.resulation})')

obj1=smartPhone("Samsung",6.5,"1080mp")
obj1.showsmartphonedetails()