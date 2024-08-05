1.Function without Parameters:
answeer:def name():
    print(f"hello world")
name()    
#output:hello world

2.      Function with Parameter:
answeer:def square(num):
    result=num*num
    print("result",result)
square(8)
#output:result 64

3.      Function with Default Parameter:
answeer:def my_function(subject="python"):
    print("programing language " +subject)
my_function("java")
my_function("r")
my_function("react")
my_function()
my_function("node.js")

#output:programing language java
#programing language r
#programing language react
#programing language python
#programing language node.js

4.      Function with Return Keyword:
answeer:def add_number(a,b):
    result= a+b
    return result
sum=add_number(10,15)
print(sum)
    
#output:sum 25

5.      Recursion:

          a) WAP to print factorial value of a given number using recursion.
answeer:def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return  n*factorial(n-1)
print(factorial(5))
#output:factorial 120

          b) WAP to display Fibonacci series up to 10 iteration using recursion.
answeer:def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
#output:0
#1
#1
#2
#3
#5
#8
#13
#21
#34

