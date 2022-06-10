 # Q.1


def DecimalBinary(n):
    if n >= 1:
        DecimalBinary(n // 2)
    print(n % 2, end='')


num = int(input("Enter a number to convert it into its binary equivalent:"))

print(" Its Binary value:")
DecimalBinary(num)

# Q.2
print("Select an operation to perform : ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()
if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is :" + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The difference is :" + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The product is :" + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The division is :" + str(int(num1) / int(num2)))
else:
    print("Invalid Entry")

# Q3.a
import math

a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
c = int(input("Enter the value of c :"))
Ans = (a + b) * (c)
print("Ans =", Ans)

# Q3.b
n = int(input("Enter the value of n :"))
Ans = n * (n - 1) / 2
print("Ans =", Ans)

# Q3.c
r = str("radius_of_sphere")
Ans = str("4*math.pi*r**2")
print("Ans =", Ans)

# Q3.d
r = str("radius")
Ans = str("math.sqrt(r*(math.cos(a))*2+r(math.sin(a))**2")
print("Ans =", Ans)

# Q3.e
y1 = str("variable 1")
y2 = str("variable 2")
x1 = str("variable 3")
x2 = str("variable 4")
Ans = str("y2-y1)/(x2-x1")
print("Ans =", Ans)

# Q4.a
for i in range(5):
    print(i, end=" ")
print()

# Q4.b
for i in range(3, 10):
    print(i, end=" ")
print()

# Q4.c
for i in range(4, 13, 3):
    print(i, end=" ")
print()

# Q4.d
for i in range(15, 5, -2):
    print(i, end=" ")
print()

# Q4.e
for i in range(5, 3):
    print(i, end=" ")
print(i)

# Q.5
print("This program finds the total molecular weight of a combination of hydrogen, carbon and oxygen atoms :")
h = eval(input("How many hydrogen atoms? "))
c = eval(input("Carbon? "))
o = eval(input("Oxygen? "))
total = (h * 1.00794) + (c * 12.0107) + (o * 15.9994)
print("The total molecular weight is", total)