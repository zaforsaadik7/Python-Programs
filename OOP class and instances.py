class employee:
    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.pay= pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
emp1= employee('Corey', 'Schefer', 5000)
emp2= employee('Zafor', 'Saadik', 6000)
print(emp1)
print(emp2)
print(emp1.first)
print(emp2.first)
print(emp1.fullname())
print(emp2.fullname())
