class people:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def display(self):
        print(self.name,self.age,self.gender)
myobj=people("kate",19,"Female")
myobj.display()
myobj=people("Jason",22,"Male")
myobj.display()
myobj=people("Janet",18,"Female")
myobj.display()
