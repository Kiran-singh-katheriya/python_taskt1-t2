'''TASK-ONE
1-->Create three variables in a single line and assign values to them in such a manner that each one of
them belongs to a different data type.
E.g. :
a = 1,
b = 2.01,
c = 'string'

#Solution
a,b,c = 1,2.01,'Kiran'
print(a)
print(b)
print(c)'''

'''
2. Create a variable of type complex and swap it with another variable of type integer.

#soltion
x=1+2j
y=5
print("value of x is:", x,"and y is :", y)

#after swapping two values

x,y=y,x
print("value of x is:", x,"and y is :", y)'''


'''
3. Swap two numbers using a third variable and do the same task without using any third variable.

#soltion
#using third variable
x=5
y=100
temp_var=x
x=y
y=temp_var
print(x)
print(y)

#without using third varible
a=50
b=20
a,b=b,a
print("value of a:",a,"value of b now is:",b)'''


'''
4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x

#soltion
x=int(input("Enter a number"))
#using python2
print "Value of x in python2 is:",x
#using python3
print("Value of x in python3 is:",x)'''

"""
5.Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output'''

#soltion
x=int(input("Enter the number between 1 to 10"))
y=int(input("Enter the number between 1 to 10"))
z=x+y
print(z)

#adding 30 to z
new_value=z+30
print(new_value)"""

'''
6.Write a program to check the data type of the entered values.
HINT: Printed output should say - The data type of the input value is : int/float/string

#soltion
a=int(input("Enter a int value"))
b=input("Enter a string value")
c=float(input("Enter a float value"))

print("data type of the input:4",type(a),type(b),type(c))'''

"""
7.Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
UPPERCAS

var_name="python is opps language"
lowerCamel="pythonIsOppsLanguage"
UpperCamel="PythonIsOppsLanguage"
snake_case="python_is_opps_language"
print(var_name.upper())"""

"""
8--If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
again. Will it change the value? If Yes then Why

#Solution:
a=int(5)
a=str(5)
print(type(a))
print(a)

It will change the value and also the datatype is changed, because typecasting of particular datatype will hold different position in memory.
"""





#TASK TWO

'''
1. Write a program in Python to perform the following operation:
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “Python Training” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a

#solution
x=(1,2,3,4,5,6,7,8,9,10,11,12,15,30)

for i in x:
    if ((i%3==0) and (i%5==0)):
        print(i,"is","Consultadd Python Training")
    elif i%3 ==0:
        print(i,"is","Consultadd")
    elif(i%5==0):
        print(i,"is","Python Training")
    else:
        print(i,"is","number is neither divisible by 3 and 5")'''

'''
2. Write a program in Python to perform the following operator based task:
If User Enter 1 - Addition
If User Enter 2 - Subtraction
If User Enter 3 - Division
If User Enter 4 - Multiplication
If User Enter 5 - Average

#solution
x =int(input("User choose Enter 1 - Addition\nUser choose Enter 2 - Subtraction\nUser choose Enter 3 - Division\nUser choose Enter 4 - Multiplication\nUser choose Enter 5 - Average\n"))
if x==1:
    num1=int(input("Enter num1 value:"))
    num2=int(input("Enter num2 value:"))
    print("Addition of both num:" ,num1+num2)
elif x==2:
    num1=int(input("Enter num1 value:"))
    num2=int(input("Enter num2 value:"))
    new=num1-num2
    if new<1:
        print("Negative")
    else:
        print(new)
elif x==3:
    num1=int(input("Enter num1 value:"))
    num2=int(input("Enter num2 value:"))
    print("Division of both num: ", num1/num2)
elif x==4:
    num1=int(input("Enter num1 value:"))
    num2=int(input("Enter num2 value:"))
    print("Multiplication of both num: ",num1*num2)
elif x==5:
    num1=int(input("Enter num1 value:"))
    num2=int(input("Enter num2 value:"))
    first=int(input("Enter the first value:"))
    second=int(input("Enter the second value:"))
    avg=num1+num2+first+second
    print("Average of above value is:",avg/4)
else:
    print("User has entered invalid choice")'''


"""3. Write a program in Python to implement the given flowchart:
#solution
a,b,c=(10,20,30)
avg=(a+b+c)/3
print(avg)

if ((avg>a and avg>b) and (avg>b and avg>c)):
    print("average is higher than a and b,so c greater than a and b")
elif (avg>a and avg>b):
    print("avg is greater than a,so b is greater than a,")
elif (avg>a and avg>c):
    print("avg is greater than a but not greater than c")
elif (avg>b and avg>c):
    print("avg is not greater to b and c")
elif avg>a:
    print("average is higher than a")"""



"""4. Write a program in Python to break and continue if the following cases occurs:
If user enters a negative number just break the loop and print “It’s Over”
If user enters a positive number just continue in the loop and print “Good Going”

#solution
x=int(input("User enter a number"))
while True:
    if x<1:
        print("good going")
        break
    elif x>=1:
        print("game")"""


"""5.Write a program in Python which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200

#solution
n1=2000
n2=3200
res=[]
for i in range(n1,n2+1):
    if (i%7==0) and (i%5==0):
        res.append(i)
print(res)."""


"""6. What is the output of the following code examples?
x=123
for i in x:
    print(i)

output:
TypeError: object is not iterable in x

i=0
while i<5:
    print(i)
    i+=1
    if i==3:
        break
    else:
        print("error")

output:
0
error
1
error
2


count=0
while True:
    print(count)
    count+=1
    if count>=5:
        break

output:
0
1
2
3
4

"""
"""
7. Write a program that prints all the numbers from 0 to 6 except 3 and 6. 
Expected output: 0 1 2 4 5


for i in range(0,6):
    if (i==3 or i==6):
        continue
    print(i, end=" ")

"""
"""8. Write a program that accepts a string as an input from the user and calculate the number of digits and letters. 
Sample input: consul72 
Expected output: Letters 6 Digits 2

from curses.ascii import isalpha
from curses.ascii import isdigit

x=input("Enter any string value:")
str_value=0
digit=0
for i in x:
    if i.isdigit():
        digit=digit+1
    elif i.isalpha():
        str_value=str_value+1
    else:
        pass
print("Letters",str_value)
print("digit",digit)
 """   
"""9.Write a program such that it asks users to “guess the lucky number”. If the correct number is
guessed the program stops, otherwise it continues forever.

Modify the program so that it asks users whether they want to guess again each time. Use two
variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
The program continues as long as a user has not answered “no” and has not guessed the correct
number"""
"""
while True:
    lucky_num=3
    number = input("User has to guess the lucky number ")
    new=int(number)
    if new!=lucky_num:
        print("You lost!")
    elif new==lucky_num:
        print("Hey! you are lucky")
        break

"""
"""

10.The program asks for five guesses (no matter whether the correct number was guessed or not). If the
correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
After the fifth guess it stops and prints “Game over!”

count=1
while count<= 5:
   number = input("Guess the" + str(count)+ ".number ")
   if number != 5:
       print("Try again")
   else:
       print("Good guess!")
   count = count +1
else:
   print("Game over")
"""

