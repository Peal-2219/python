# a= int(input("enter no1:21"))
# b= int(input("enter no2:"))
# sum= a+b
# print(sum)

# a= int(input("enter the side of area:"))
# area= a*a
# print(area)

# name=str(input("enter the name"))
# l=len(name)
# print(l)

# list1=[1,2,1]
# # list2=[1,2,3]
# copy_list1=list1.copy()
# copy_list1.reverse()

# movies=[]
# movies.append(input("enter 1st movie:"))
# movies.append(input("enter 2nd movie:"))
# movies.append(input("enter 3rd movie:"))
# print(movies)

# grade=("C","D","A","A","B","B","A")
# print(grade.count("A"))

# grade=["C","D","A","A","B","B","A"]
# grade.sort()
# print(grade)

# if(copy_list1 == list1):
#     print("palindrome")
# else:
#     print("not palindrome")

# dictionary={
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture","list of facts and figures"]
# }
# print(dictionary)

# subjects={"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(len(subjects))

# marks={}
# x=int(input("enter phy: "))
# marks.update({"phy":x})
# x=int(input("enter math: "))
# marks.update({"math":x})
# x=int(input("enter chem: "))
# marks.update({"chem":x})
# print(marks)


# # loops
# i=1
# while i<=100:
#     print(i)
#     i += 1

# i=100
# while i>=1:
#     print(i)
#     i -= 1

# n=int(input("enter number for table"))
# i=1
# while i<=10:
#     print(n*i)
#     i += 1

# num=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i < len(num):
#     print(num[i])
#     i += 1

# num=(1,4,9,16,25,36,49,64,81,100)
# x=36
# i=0
# while i < len(num):
#     if(num[i]==x):
#         print("found at",i)
#     else:
#         print("finding")
#     i += 1

# num=[1,4,9,16,25,36,49,64,81,100]
# for el in num:
#     print(el)

# num=(1,4,9,16,25,36,49,64,81,100)
# x=49
# i=0
# for el in num:
#     if (el == x):
#         print("found at",i)
#     i += 1

# for i in range(1,101):
#     print(i)

# for i in range(100,0,-1):
#     print(i)

# n=int(input("enter the number"))
# for i in range(1,11):
#     print(n*i)

# n=5
# sum=0
# i=1
# while i<=n:
#     sum += i
#     i+=1
# print("total sum =", sum)

# n=5
# fact=1
# for i in range(1,n+1):
#     fact *= i
# print("factorial",fact)

# # average of 3 numbers
# def calc_avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
# calc_avg(43,54,65)

# cities=["delhi","gurgaon","noida","pune","ahmedabad"]
# heroes=["thor","ironman","captain america","shaktiman"]
# def print_len(list):
#     print(len(list))
# print_len(cities)
# print_len(heroes)

# heroes=["thor","ironman","captain america","shaktiman"]
# def print_len(list):
#     print(len(list))
# def print_list(list):
#     for item in list:
#         print(item,end=" ")
# print_list(heroes)
# print()

# def calc_fact(n):
#     fact=1
#     for i in range (1,n+1):
#         fact *= i
#     print(fact)
# calc_fact(5)

# def convertor(usd_val):
#     inr_val=usd_val *83
#     print(usd_val,"USD =",inr_val,"INR")
# convertor(54)

# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return fact(n-1)*n
# print(fact(5))

# def calc_sum(n):
#     if (n==0):
#         return 0
#     return calc_sum(n-1) + n
# sum =calc_sum(5)
# print(sum)

# def print_list(list,idx=0):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)
# fruits=["mango","litchi","apple","banana"]
# print_list(fruits)

# with open("practice.txt","r") as f:
#     data=f.read()
# new_data=data.replace("java","python")
# print(new_data)
# with open("practice.txt","w") as f:
#     f.write(new_data)

# def check_for_word():
#     word="learning"
#     with open("practice.txt","r") as f:
#         data=f.read()
#         if(data.find(word)!= -1):
#             print("found")
#         else:
#             print("not found")
# check_for_word()

# def check_for_line():
#     word="programming"
#     data=True
#     line_no=1
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# print(check_for_line())

# count=0
# with open("practice.txt","r") as f:
#     data=f.read()
#     num=data.split(",")
#     for val in num:
#         if(int(val) % 2 == 0):
#             count += 1
# print(count)

# class Student:
#     college_name="ABC college" 
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("adding new student in database")
# s1=Student("peal",98)
# print(s1.name,s1.marks)
# s2=Student("Krish",87)
# print(s2.name,s2.marks)
# print(s2.college_name)

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum += val
#         print(self.name,"your avg score is:", sum/3)
# s1=Student("peal",[76,87,97])
# s1.get_avg()

# class Account:
#     def __init__(self,bal,acc):
#         self.balance=bal
#         self.account_no=acc
#     def debit(self,amount):
#         self.balance -= amount
#         print("RS.",amount,"was debited")
#         print("total balance =", self.get_balance())
#     def credit(self,amount):
#         self.balance+=amount
#         print("RS.",amount,"was credited")
#         print("total balance=", self.get_balance())
#     def get_balance(self):
#         return self.balance
# acc1=Account(10000,12345)
# acc1.debit(435)
# acc1.credit(78548)
# acc1.debit(5483)
        
# class car:
#     color="black"
#     @staticmethod
#     def start():
#         print("car started")
#     @staticmethod
#     def stop():
#         print("car stopped")
# class toyotacar(car):
#     def __init__(self,name):
#         self.name=name
# car1=toyotacar("fortuner")
# car2=toyotacar("prius")
# print(car1.color)

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math)/3)+ "%"
# stu1=Student(98,65,87)
# print(stu1.percentage)
        
# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def shownumber(self):
#         print(self.real,"i +",self.img,"j")
#     def add(self,num2):
#         newreal=self.real+num2.real
#         newimg=self.img+num2.img
#         return complex(newreal,newimg)
# num1=complex(1,3)
# num1.shownumber()
# num2=complex(4,6)
# num2.shownumber()
# num3=num1.add(num2)
# num3.shownumber()

# class circle():
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius ** 2
#     def perimeter(self):
#         return 2*3.14*self.radius
# c1= circle(5)
# print(c1.area())
# print(c1.perimeter())
        
# class employee:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary
#     def showdetails(self):
#         print("role=",self.role)
#         print("dept:",self.dept)
#         print("salary:",self.salary)
# class engineer(employee):
#     def __init__(self, name,age):
#         self.name=name
#         self.age=age
#         super().__init__("engineer","IT","75000")
# eng=engineer("peal",21)
# eng.showdetails()

class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,odr2):
        return self.price>odr2.price
odr1=order("chips",20)
odr2=order("tea",50)
print(odr1>odr2)