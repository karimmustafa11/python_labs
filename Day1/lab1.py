# 1. Write a Python program which accepts the user’s first and last name and print them in reverse order with a space between them

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name + " " + first_name)

#..........................................................................


#2. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = int(input("Enter an integer (n): "))
nn = int(str(n) + str(n))  
nnn = int(str(n) + str(n) + str(n))

result = n + nn + nnn
print("Result:", result)

#.............................................................................

#3. Write a Python program to print the following here document

print("""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""")

#...............................................................................


#4. Write a Python program to get the volume of a sphere with radius 6.

import math
radius = 6
volume = (4/3) * math.pi * (radius ** 3)
print("Volume of the sphere with radius 6 is:", volume)

#...............................................................................

#5. Write a Python program that will accept the base and height of a triangle and compute the area

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = (1/2) * base * height
print("Area of the triangle is:", area)

#............................................................................

#6. Write a Python program to construct the following pattern, using a nested for loop.

for i in range(1, 6):
    print("* " * i)

for i in range(4, 0, -1):  
    print("* " * i)

#.............................................................................

#7. Write a Python program that accepts a word from the user and reverse it.

word = input("Enter a word: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

#...............................................................................

#8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

for num in range(0, 7):
    if num == 3 or num == 6:
        continue
    print(num, end=" ")

#...............................................................................

#9. Write a Python program to get the Fibonacci series between 0 to 50.

# Initialize the first two numbers of the Fibonacci series
a, b = 0, 1

while a <= 50:
    if a != 0: 
        print(a, end=" ")
    a, b = b, a + b

#............................................................................


#10. Write a Python program that accepts a string and calculates the number of digits and letters.

# Accept a string from the user
user_input = input("Enter a string: ")

digit_count = 0
letter_count = 0

for char in user_input:
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
        letter_count += 1

print("Number of digits:", digit_count)
print("Number of letters:", letter_count)