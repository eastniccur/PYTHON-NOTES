# Exercises: Level 1
# Write a function which generates a six digit/character random_user_id.
#   print(random_user_id()) 
#   '1ee33d'
# Modify the previous task. Declare a function named user_id_gen_by_user.
# --> It doesn’t take any parameters but it takes two inputs using input(). 
# -->One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

import random
import string

def random_user_id():
    random_char=string.ascii_lowercase + string.digits
    
    return ''.join(random.choices(random_char, k=6));
result=random_user_id()
print(result)

def user_id_gen_by_user():
    num_chars=int(input("Enter your numbers"))
    num_ids=int(input("Enter your ids"))
    chars=string.ascii_lowercase + string.digits
    id_generated=[]
    for _ in range(num_ids):
        user_id=''.join(random.choices(chars, k=num_chars))
        id_generated.append(user_id)
    return '\n'.join(id_generated)
print(user_id_gen_by_user())


def rgb_gen():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return f'rgb({r},{g},{b})'
print(rgb_gen())
