Q.1 print helloworld
Answeer:
print("helloworld")


#output: helloworld

Q.2 describe local variable and global variable code
Answeer:
x=10 #global variable
def local():
    x=100
    print(x)


print(x)  
local()  


#output: global 10
#local 100

Q.3 Write a code that describe Indentation error
Answeer:
s= 10
if(s>5):
 print(f"s is greater than 5")#  A string prefixed with 'f',formated string
 print("This line is properly indented")

#output: s is greater than 5
#This line is properly indented

Q.4 write a code that describe local and global variable with same name
Answeer:
x="global"
 
def my_function():
    x="local"
    print("the inside value is ",x)
    
      
my_function()
print("this outside value is",x)


#output:the inside value is  local
#this outside value is global

Q.5 Write a code for string, int and float input.
Answeer:
int= int(input("enter ur data type"))
float= float(input("enter ur data type"))
str= str(input("enter ur data type"))

print(type(int))
print(type(float))
print(type(str))


#output: enter ur data type 56
#enter ur data type 76
#enter ur data type india
#<class 'int'>
#<class 'float'>
#<class 'str'>