# Creating a New Dictionary
'''d = {n:n*n for n in range(1,5)}
print(d)'''

# calculating Total Bill
'''old = {"rice":60,"dhaal":120,"oil":190}
sum=0
new = {product:price for(product,price) in old.items()}

for i in new.values():
    sum+=i
print(new)
print(sum,"Total bill")'''


# Create a list with 8 customer names display a dictionary which has customer's names along with discounts for them from  a particular shop

'''import random
cust_name = ['Siva','Sanjiv','Rohit','Abhilash','Sampath','Lakshman','Surya','Pradeep']
Dict_disc = {names:random.randint(1,100) for names in cust_name}
print(Dict_disc)'''

# 1. create two list,1st have 5 stu names and 2 have total marks betw 1 to 500 create dict stu names as keys and percentage as values.

'''stu_name = ['Siva','Sanjiv','Rohit','Abhilash','Sampath']
stu_marks = [300,420,450,490,360]
Dict = {name:(perc/500)*100  for (name,perc) in zip(stu_name,stu_marks)}
print(Dict)'''

#S = "HI I'AM "VEERAYYA""
s = "  HELLO VEERAYYA  "
print(s)
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.replace("H","G"))
print(s.strip())
print(s.split(","))
print(s.center(50,'!'))
print(s.startswith('HELLO'))
print(s.endswith('A'))
print(s.find('R'))
print(s.count('E'))
print(s.index('R'))
print(s.count('E',5,len(s)))
print(s.index('R',5,len(s)))
print(s.find('R',5,len(s)))
