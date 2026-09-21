# --- STANDARD FOR LOOP ---
# numbers = [1, 2, 3, 4, 5, 6]
# squares = []

# for x in numbers:
#     if x % 2 == 0:
#         squares.append(x * x)

# print(squares)

numbers = [1, 2, 3, 4, 5, 6,8]
# --- LIST COMPREHENSION ---
#          [Output   | Loop             | Condition]
squares = [  x * x   for x in numbers   if x % 2 == 0  ]

print(squares)