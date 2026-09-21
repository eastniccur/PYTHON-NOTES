# Exercises: Level 1
# Create an empty tuple
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# Join brothers and sisters tuples and assign it to siblings
# How many siblings do you have?
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

# 1. Empty tuple
empty_tpl = ()

# 2. Brothers and Sisters tuples
brothers = ('Ali', 'Hassan')
sisters = ('Amina', 'Fatima')

# 3. Join brothers and sisters
siblings = brothers + sisters
print("Siblings:", siblings)

# 4. Count siblings
print("Number of siblings:", len(siblings))

# 5. Add father and mother (convert to list first, then back to tuple)
siblings_list = list(siblings)
print("Siblings as list:", siblings_list)
siblings_list.append('ALI')
siblings_list.append('FATUMA')
print("Siblings with parents:", siblings_list)
family_members = tuple(siblings_list)
print("Family Members:", family_members)


# Exercises: Level 2
# Unpack siblings and parents from family_members
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
# Change the about food_stuff_tp tuple to a food_stuff_lt list
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# Slice out the first three items and the last three items from food_stuff_lt list
# Delete the food_stuff_tp tuple completely
# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country

# Check if 'Iceland' is a nordic country

# 1. Unpack siblings and parents
*siblings_unpacked, father, mother = family_members
print("Unpacked Siblings:", siblings_unpacked)
print("Parents:", father, mother)

# 2. Join three tuples
fruits = ('banana', 'orange', 'mango')
vegetables = ('Tomato', 'Potato', 'Onion')
animal_products = ('milk', 'meat', 'eggs')

food_stuff_tp = fruits + vegetables + animal_products
print("Food Stuff Tuple:", food_stuff_tp)

# 3. Convert tuple to list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out middle item(s)
n = len(food_stuff_lt)
print("Length of food_stuff_lt:", n)
mid_start = n // 2
print("Middle index:", mid_start)

if n % 2 == 0:
    middle_items = food_stuff_lt[mid_start - 1 : mid_start + 1]
else:
    middle_items = [food_stuff_lt[mid_start]]

print("Middle item(s):", middle_items)

# 5. Slice first 3 and last 3 items from list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First 3:", first_three)
print("Last 3:", last_three)

# 6. Delete tuple completely
del food_stuff_tp

# 7. Check country existence in tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print("Is Estonia a nordic country?", 'Estonia' in nordic_countries)  # False
print("Is Iceland a nordic country?", 'Iceland' in nordic_countries)  # True

