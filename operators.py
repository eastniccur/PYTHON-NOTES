import math

# --- Variables & Declarations ---
age = 25                      # Ex 1: Integer
height = 5.9                   # Ex 2: Float
complex_num = 1 + 2j          # Ex 3: Complex

# --- Interactive Calculations ---
# Ex 4: Triangle Area
b = float(input("Enter base: "))
h = float(input("Enter height: "))
print(f"The area of the triangle is {0.5 * b * h}")

# Ex 5: Triangle Perimeter
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
print(f"The perimeter of the triangle is {a + b + c}")

# Ex 6: Rectangle Area & Perimeter
length = float(input("Enter length: "))
width = float(input("Enter width: "))
print(f"Area: {length * width}, Perimeter: {2 * (length + width)}")

# Ex 7: Circle Area & Circumference
radius = float(input("Enter radius: "))
pi = 3.14
print(f"Area: {pi * radius ** 2}, Circumference: {2 * pi * radius}")

# --- Slopes & Math ---
# Ex 8: Slope of y = 2x - 2 (y = mx + b -> m = 2)
slope_1 = 2

# Ex 9: Slope & Distance between (2, 2) and (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Slope 2: {slope_2}, Distance: {distance}")

# Ex 10: Compare Slopes
print("Slopes are equal:", slope_1 == slope_2)

# Ex 11: Solve y = x^2 + 6x + 9 for y = 0
# (x + 3)^2 = 0 -> x = -3
x = -3
y = x**2 + 6*x + 9
print(f"At x = {x}, y is {y}")

# --- Logic & Type Checking ---
# Ex 12: Falsy comparison of lengths
print(len('python') != len('dragon'))  # False

# Ex 13: 'on' in both words
print('on' in 'python' and 'on' in 'dragon')  # True

# Ex 14: Check 'jargon' in sentence
sentence = "I hope this course is not full of jargon."
print('jargon' in sentence)  # True

# Ex 15: No 'on' in both (Negation check)
print('on' not in 'python' and 'on' not in 'dragon')  # False

# Ex 16: Type Casting Chain
length_py = len('python')
float_py = float(length_py)
str_py = str(float_py)

# Ex 17: Even number check
num = 4
is_even = (num % 2 == 0)

# Ex 18: Compare Floor division vs Int cast
print(7 // 3 == int(2.7))  # True (2 == 2)

# Ex 19: Check types
print(type('10') == type(10))  # False

# Ex 20: Int cast validation
# int('9.8') throws ValueError because '9.8' is a float string.
# Correct way: int(float('9.8')) == 10
print(int(float('9.8')) == 10)  # False (9 == 10)

# --- Real World Scripts ---
# Ex 21: Weekly Pay
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
print(f"Your weekly earning is {hours * rate}")

# Ex 22: Seconds Lived
years = float(input("Enter number of years you have lived: "))
seconds_in_year = 365.25 * 24 * 60 * 60
print(f"You have lived for {int(years * seconds_in_year)} seconds.")

# Ex 23: Display Table
print("\nTable:")
for i in range(1, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")