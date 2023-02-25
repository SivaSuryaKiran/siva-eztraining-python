'''def happy(n):
    s=r=0
    while(n>=0):
        for i in range(0,len(str(n))+1):
            r=n%10
            s=s+r**2
            n=n//10
        return s

n = int(input("enter the number: "))
res = n
while (res!=1 and res!=4):
    res = happy(res)
if res==1:
    print("happy number")

else:
    print("not a happy number")'''


'''#protected _

class encap:
    _a=10
    c=30

    def encapfunction(self):
        _b=100
        print("encap function accessing protected")
        print(self._a+10)
        print(self)

obj = encap()
print(obj._a)
obj.encapfunction()
print(obj.c)'''
'''class encaps:
    __a=10
    print(__a)
    def encapfunc(self):
         print(self.__a-6)

obj1 = encaps()
obj1.encapfunc()
print(obj1.__a)'''

# types
'''1.overloading
        operator overloading
        method overloading
   2. overriding - if a method is present in parent class as well as child class'''



'''class methodoverload:
    def display(self,a=None,b=None):
        print(a,b)
obj = methodoverload()

print("without arguments")
obj.display()

print("with all arguments")
obj.display(55,56)

print("with one arguments")
obj.display(100)'''


class vijayawada:
    def placename(self):
        print("vijayawada palcename is KLU")
    def students(self):
        print("yes - vijayawada")
    def which_year(self):
        print("3rd year")
class hyderabad:
    def placename(self):
        print("HYD palcename is HYD-KLU")
    def students(self):
        print("yes - HYD")
    def which_year(self):
        print("3rd year")

vjy = vijayawada()
hyd = hyderabad()

for details in (vjy,hyd):
    details.placename()
    details.students()
    details.which_year()
