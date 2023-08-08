class employee:
    numEmployee= 0
    raiseAmount= 1.04
    def __init__(self, name, pay):
        self.name= name
        self.pay= pay
        employee.numEmployee+= 1
        
    def applyRaise(self):
        self.pay=int(self.pay* self.raiseAmount)

emp1= employee('corey', 50000)
emp2= employee('max', 25000)

print (emp1.__dict__)
emp1.raiseAmount= 1.05
print (emp1.__dict__)
print(emp1.raiseAmount)
print(emp2.raiseAmount)
print(employee.raiseAmount)

employee.raiseAmount= 1.02
print (employee.__dict__)
print(emp1.raiseAmount)
print(emp2.raiseAmount)
print(employee.raiseAmount)
#here I'm having a problem. After setting the value raiseAmount for emp1 it creates an new attribute with the same name 'raiseAmount' so when agian I change the 'raiseAmount' value for the whole class
#it won't change the value for that emp1 instance and I don't know a  way to avoid creating that new variable.
