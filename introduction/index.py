# Introduction to Python
print("Hello, World!")

#Variables
name = "André"
age = 22
is_developer = True

#Data types
integer_num = 10      # int
float_num = 3.14      # float
string_text = "Python"  # str
boolean_val = False   # bool

# arithmetic operators
x = 10
y = 3

print(x + y)   # 13
print(x - y)   # 7
print(x * y)   # 30
print(x / y)   # 3.333... (always float)
print(x // y)  # 3 (integer division)
print(x % y)   # 1
print(x ** y)  # 1000 (power)


#Conditional operators
print(5 == 5)     # True
print(5 != 3)     # True
print(5 > 3)      # True
print(5 <= 5)     # True

#Logical operators
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False

#String concatenation
print("Hello" + " " + "World")  # Hello World
print("2" + str(2))  # "22"
print(2 + int("2"))  # 4

#Control flow
#IF ELSE
age = 18

if age < 18:
    print("Minor")
elif age == 18:
    print("Exactly 18")
else:
    print("Adult")

#LOOPS
for i in range(5):
    print(i)  # 0..4

count = 0
while count < 3:
    print(count)
    count += 1

#Truthy and Falsy values
if 0: print("won't run")
if "": print("won't run")
if []: print("won't run")

if 1: print("runs")
if "hi": print("runs")
if [1,2,3]: print("runs")

#Functions
def greet(name):
    return f"Hello, {name}"

print(greet("André"))

