1.     Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.
answeer:a=int(input("enter your number"))
if(a%2==0):
    print("even number")
else:
    print("odd number")
    
#output:enter your number5
#odd number
2.      Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
answeer:a=int(input("enter your age"))
if (a>=18):
    print("are u eligible for vote")
else:
    print(" are not eligible for vote ")
#output:enter your age18
#are u eligible for vote

3.      Write a Python program that determines if a given year is a leap year or not.
answeer:year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")
#output:Enter year to be checked:2012
#The year is a leap year!

4.      Create a Python program that checks if a user-given number is positive, negative, or zero.
answeer:n=float(input("enter your number"))
if n>0:
    print("possitve")
elif n==0:
    print("zero")
else:
    print("negative")
    
#output:enter your number5
#possitve

5.      Write a Python program that determines the largest of three numbers entered by the user.
answeer:a=int(input("enter 1st number "))
b=int(input("enter 2nd number "))
c=int(input("enter 3rd number "))
if a>b and a>c:
    print("a is largest number")
elif b>a and b>c :
    print("b is largest number")
elif c>a and c>b:
    print("c is largest")
else:
    print ("code error")
#output:enter 1st number 6
#enter 2nd number 8
#enter 3rd number 9
#c is largest

