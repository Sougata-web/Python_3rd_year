# largest btn three numbers
# def find_largest(a,b,c):
#     return max(a,b,c)
# print(find_largest(1,2,3))

#print fibonacci
# def fib(n):
#     a,b=0,1
#     for _ in range(n):
#         print(a, end=' ')
#         a,b=b,a+b

# fib(7)
# n=int(input('Enter value for summation: '))
# sum_even=sum(i for i in range(2,2*n+1,2))
# print(sum_even)

#prime numbers
# def prime_nums(start,end):
#     primes=[]
#     for val in range(start,end+1):
#         if val > 1:
#             for i in range(2,int(val**0.5)+1):
#                 if(val%i)==0:
#                     break
#             else:
#                 primes.append(val)
#     return primes
# print(prime_nums(10,20))

# reverse a given number
# num=int(input('Enter a number '))
# reversed_num=int(str(num)[::-1])
# print(reversed_num)

#palindrome or not
# num='12321'
# if num == num[::-1]:
#     print('Palindrome')
# else:
#     print('Not Palindrome')

#armstrong number
# num=153
# sum_powers=sum(int(digit)**len(str(num))for digit in str(num))
# print('Armstrong' if sum_powers == num else 'Not Armstrong')

#spy number or not
# import math
# num=1124
# digits=[int(x) for x in str(num)]
# print('spy' if sum(digits)==math.prod(digits) else 'not spy')

#Write a python program to input N items from the user then turn every item of a list into its square then reverse the list and then delete the maximum and minimum elements from the list and display the final list to  the user.

# lst=[2,4,1,5,3]
# squared=[x**2 for x in lst]
# squared.reverse()
# squared.remove(max(squared))
# squared.remove(min(squared))
# print(squared)

# Write a python program to input N items from the user then find the occurrence count of each object and show that to the user as item, occurrence value, and then show the sorted list with only unique values to the user.

# from collections import Counter
# items=[1,2,3,3,2,1,2]
# counts=Counter(items)
# for k,v in counts.items():
#     print(f'Items:{k}, Occurrence:{v}')
# print(sorted(list(set(items))))

# Write a python program to get different inputs from the user and do something to store it into a tuple and then pass that tuple into a function. The function will return a list with the occurrence count of values and values passed to the function. Ex: [('2',3), ('m',2)]. 

# from collections import Counter
# def process_tuple(t):
#     return list(Counter(t).items())

# user_tuple=('2','2','m','m','3')
# print(process_tuple(user_tuple))

# Write a python program to get N students information from the user 
# and store them into nested tuples as (name, (roll, dept), (marks of 5 
# subjects)). Now print the roll, name, department of the student along 
# with marks in descending order to the user when the user searches for 
# any student information using their roll. 

# def get_students():
#     students = []
#     n = int(input("Enter number of students: "))

#     for _ in range(n):
#         name = input("Enter name: ")
#         roll = int(input("Enter roll number: "))
#         dept = input("Enter department: ")

#         marks = []
#         print("Enter marks of 5 subjects:")
#         for i in range(5):
#             m = int(input(f"Subject {i+1}: "))
#             marks.append(m)

#         students.append((name, (roll, dept), tuple(marks)))

#     return students


# def search_student(students):
#     search_roll = int(input("\nEnter roll number to search: "))

#     for s in students:
#         if s[1][0] == search_roll:
#             print(f"\nRoll: {s[1][0]}, Name: {s[0]}, Dept: {s[1][1]}")
#             print("Marks (Desc):", sorted(s[2], reverse=True))
#             return

#     print("Student not found!")


# # Main program
# students = get_students()
# search_student(students)

#  Write a python program to Perform Union, Intersection, Difference, Symmetric Difference of two sets.

# a={1,2,3,4}
# b={3,4,5,6}
# print('union',a|b)
# print('intersection',a&b)
# print('diff',a-b)
# print('symm diff',a^b)

# Write a python program to Convert two python list into a dictionary 
# where elements from the first list become keys and elements from the 
# second list become values. 

# keys=['name','age','dept']
# values=['amit',21,'cse']
# dictionary=dict(zip(keys,values))
# print(dictionary)


# Write a python program to create a class representing a binary search 
# tree. Include methods for inserting and searching elements in the binary 
# tree. 

class Node:
    def __init__(self,value):
        self.left,self.right,self.value=None,None,value
        
    def insert(self,value):
        if value < self.value:
            if self.left is None:
                self.left=Node(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right=Node(value)
            else:
                self.right.insert(value)

    def find(self,value):
        if value<self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value>self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True
        
tree=Node(10)
tree.insert(1)
tree.insert(4)
tree.insert(45)
tree.insert(19)
print(tree.find(4))
            

# Write a python program to create a class representing a stack data 
# structure. Include methods for pushing and popping elements. 

# class Stack:
#     def __init__(self):self.items=[]
#     def push(self,item):self.items.append(item)
#     def pop(self):
#         if not self.is_empty():return self.items.pop()
#     def is_empty(self):return len(self.items)==0
# s=Stack()
# s.push(10);s.push(30)
# print('popped',s.pop())

# Write a python program that prompts the user to input an integer and 
# raises a value error exception if the input is not a valid integer. 

# try:
#     val=int('abc')
# except ValueError as e:
#     print('Value Error not a valid integer')
    
# Write a python program that opens a file and handle a file not found 
# error exception if the file doesn't exist. 

# try:
#     with open('mmissing.txt','r') as f:
#         content=f.read()
# except FileNotFoundError:
#     print('File Not Found')
    
#  Write a python program that execute an operation on a list and 
# handles an index error exception if the index is out of range. 
# lst=[1,2,3]
# try:
#     print(lst[5])
# except IndexError:
#     print('Index Error. Index Out Of Bound.')

#  Write a python program using thread locks to solve a producer 
# consumer problem where the producer will produce a list of arbitrary 
# values and the consumer will consume that list to make that empty. 

# import threading, time
# buf , lock=[], threading.Lock()
# def producer():
#     with lock:
#         buf.append(1)
#         print('Produced 1')
# def consumer():
#     with lock:
#         if buf:
#             print('Consumed', buf.pop())
# t1,t2=threading.Thread(target=producer),threading.Thread(target=consumer)
# t1.start()
# time.sleep(0.1)
# t2.start()
# t1.join;t2.join()

# Write a python program to create your own copy file program where 
# in command line two file names will be passed as input. The program will 
# copy the content of one file into another with a suitable message to the 
# user. 

# import sys,shutil
# try:
#     shutil.copy(sys.argv[1],sys.argv[2])
#     print('File Copied Successfully')
# except Exception  as e:
#     print(e)

#  24. Write a python program to build basic chat interface using python GUI 

# import tkinter as tk
# root=tk.Tk()
# chat_box=tk.Text(root)
# chat_box.pack()
# root.mainloop()
# print('Chat GUI Initialized')

#  Write a Python program to read student data from a CSV or Excel file 
# then perform data analysis on the dataset like calculate mean of marks, 
# find maximum and minimum marks, compute standard deviation. 
# Visualize the data using different types of charts and plots like Line Plot 
# (Name vs Marks) Bar Chart (Name vs Marks) Histogram (Marks 
# Distribution) Scatter Plot (Age vs Marks). Also create Heatmap 
# (Correlation between numerical variables) Pair Plot (Relationship 
# between all variables).

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# df=pd.read_csv('data.csv') 

# print(df['marks'].mean())
# print(df['marks'].max())

# print(df['marks'].min())
# print(df['marks'].std())
# plt.plot(df['name'],df['marks'])
# sns.barplot(x='name',y='marks',data=df)
# sns.histplot(df['marks'])
# sns.scatterplot(x='age',y='marks',data=df)
# sns.heatmap(df.corr(),annot=True)
# sns.pairplot(df)
# plt.show()


# 15. Write a python program to create a class that represent a shape. 
# Include methods to calculate the area & perimeter. Implement subclasses 
# for different shapes like circle, triangle and square.

# import math
# class Shape:
#     def area(self):pass
#     def perimeter(self):pass
    
# class Square(Shape):
#     def __init__(self,side):self.side=side
#     def area(self):return self.side**2
#     def perimeter(self):
#         return self.side*4 
# class Circle(Shape):
#     def __init__(self,radius):self.radius=radius
#     def area(self):
#         return round(math.pi*self.radius*self.radius,2)
#     def perimeter(self):
#         return round(2*math.pi*self.radius,2)
# sq=Square(4)
# print(sq.area(),' ',sq.perimeter())
# cr=Circle(4)
# print(cr.area(),' ',cr.perimeter())
