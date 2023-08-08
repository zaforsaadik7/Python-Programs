class employee:
    raiseAmount= 1.05
    #Regular methods: 
    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.pay= pay
    def applyRaise(self, pay):
        self.pay= self.pay* self.raiseAmount
    #Class mehtod:
    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raiseAmount= amount
    #You can use class methods inorder to provide multiple ways of creating objects
    @classmethod
    def fromString(cls, empStr):
        first, last, pay= empStr.split('-')
        return employee(first, last, pay) 
    @staticmethod
    def isWorkday(date):
        if date.weekday()== 5 or  date.weekday()== 6:
            return False
        return True
    
emp1= employee('Corey', 'Schefer', 150000)
emp2= employee('Zafor', 'Saadik', 160000)
employee.setRaiseAmount(1.02)
print(employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount)

emp1Str= 'John-Doe-150000'
emp2Str= 'Steven-Smith-250000'
emp3Str= 'Jane-Doe-300000'
newEmp1=employee.fromString(emp1Str)
newEmp2=employee.fromString(emp2Str)
newEmp3=employee.fromString(emp3Str)
print(newEmp1.__dict__)
print(newEmp2.__dict__)
print(newEmp3.__dict__)

import datetime
myDate=datetime.date(2023, 8, 8)
print(employee.isWorkday(myDate))
