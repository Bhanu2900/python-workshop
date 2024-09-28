from itertools import filterfalse
from turtle import TurtleGraphicsError

list = [1,34,35,465,56, 0, 65, 65,6 ,65, 6, 6,56 ]

print(min(list))
print(max(list))
int = 3 + 19j
print(abs(int))


pi = 3.141383237234465353255326
print(round(pi, 3))


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
for i, value in enumerate(list1):
    print(f"{i}-{value}")

print(f"{pi: 2f}")

# square = lambda x, y: x*y
# print (f"{square(int(input('please enter the number :')), int(input('please enter the number :')))}")

#class xyz:
#    def __init__(self):
#        self.ABC = "123"

#    def get(self):
#        return self.ABC

#declare_class = xyz()
#value = declare_class.get()
#print(value)

class xyz:
    def __init__(self):
        self.__balence__= 0
        
        def deposite(self, amount):
            self.__balance__ += amount
            return True
        
        def withdraw(swlf, amount):
            if 0 < amount <= self.__balance__:
                self.__blance__-= amount
                return Ture 
            else:
                return false 
            def get(self):
                return self.__blance__
            
            abc = xyz()
            print(abc.get())
            abc.deposit(10000)
            
        
                
                
            
            
            
            
            
            
        

    
