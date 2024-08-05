Q.1 Write a program for arithmatic operators
answeer:
a=12
b=5

#addition 
print("addition",a+b)

#subtraction
print("subtration",a-b)

#multiply
print("multiply",a*b)
print("Exponentiation",a**b)# (a)^b

#division
print("division",a/b)
print("Floor division",a//b)

#Modulus
print("Modulus",a%b)


#output:addition 17
#subtration 7
#multiply 60
#Exponentiation 248832
#division 2.4
#Floor division 2
#Modulus 2

Q.2 Write a program for assignment operators
answeer:#
1 basic assign
x=10
print("basic assign",x)
#2 add and assign operator
x=10
x+=5
print("add assign operator",x)

# 3 sub and assign operator
x=10
x-=5
print("sub assign operator",x)


#output:basic assign 10
#add assign operator 15
#sub assign operator 5
Q.3Write a program for Bitwise operators 
answeer:
# bitwise operator 
#and operator AND(&)
x = 4
y = 6

result = x and y
print("AND operator (&)",result)

# OR(|)
x = 4
y = 8

result = x or y
print("OR operator (|)",result)  
# nor operator(not)
x = 6

result = not x
print("not operator",result) 
#  xor(^)
x=8
y =9

result=x^y
print("XOR operstor",result) 


#output:AND operator (&) 6
#OR operator (|) 4
#not operator False
#XOR operstor 1
Q.4 Write a program to calculate greatest of three numbers.
answeer:a=5
b=8
c=9
if(a>b)&(a>c):
 print("a is largest")
elif(b>a)&(b>c):
 print("b is largest")
elif(c>a)&(c>b):
 print("c is largest")
else:
 print("are equal the value of a,b,c")

#output:c is largest
1.      Calculate the area of a circle.
answeer:
#area of circle
PI = 3.14
r = float(input("Enter the radius of a circle:"))
area = PI * r * r
print("Area of a circle = %.2f" %area)

#output:Enter the radius of a circle:6
#Area of a circle = 113.04
2.      Calculate the area of a triangle.
answeer:# # area of triangle 
base=4

height=6
print("area of triangle",(base*height)/2)


#output:area of triangle 12.0
3.      Calculate the area of a rectangle.
answeer:
def calculate_area_of_rectangle(length, width):
  area = length * width
  return area
length = 7
width = 4
area_rectangle = calculate_area_of_rectangle(length, width)
print(f"The area of the rectangle with length {length} and width {width} is: {area_rectangle}")


#output:The area of the rectangle with length 7 and width 4 is: 28

4.      Calculate the area of a square.
answeer:def calculate_area_of_square(side):
    area = side * side
    return area

def main():
    
    side = float(input("Enter the side length of the square: "))
    area = calculate_area_of_square(side)
    
    print(f"The area of a square with side length {side} is: {area}")
if __name__ == "__main__":
    main()


#output:Enter the side length of the square: 5
#The area of a square with side length 5.0 is: 25.0