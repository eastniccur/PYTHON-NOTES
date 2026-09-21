# Exercises: Day 8
# Create an empty dictionary called dog
# Add name, color, breed, legs, age to the dog dictionary
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# Get the length of the student dictionary
# Get the value of skills and check the data type, it should be a list
# Modify the skills values by adding one or two skills
# Get the dictionary keys as a list
# Get the dictionary values as a list
# Change the dictionary to a list of tuples using items() method
# Delete one of the items in the dictionary
# Delete one of the dictionaries

# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'German Shepherd'
dog['legs'] = 4
dog['age'] = 3

print("Dog dictionary:", dog)

# 3. Create a student dictionary
student = {
    'first_name': 'Zakaria',
    'last_name': 'Sheikh',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['HTML', 'CSS', 'JavaScript', 'React', 'Python'],
    'country': 'Kenya',
    'city': 'Nairobi',
    'address': {
        'street': 'Main St',
        'zipcode': '00100'
    }
}

print("Student dictionary:", student)

# 4. Get the length of the student dictionary
student_length = len(student)
print("Student dict length:", student_length)

# 5. Get skills value and check data type
skills_val = student['skills']
print("Skills data type:", type(skills_val))  # <class 'list'>

# 6. Modify the skills value by adding one or two skills
student['skills'].append('Flask')
student['skills'].append('SQL')
print(student['skills'])  # ['HTML', 'CSS', 'JavaScript', 'React', 'Python', 'Flask', 'SQL']

# 7. Get dictionary keys as a list
student_keys = list(student.keys())
print("Keys:", student_keys)

# 8. Get dictionary values as a list
student_values = list(student.values())
print("Values:", student_values)

# 9. Change dictionary to a list of tuples using items()
student_tuples = list(student.items())
# items() method returns a view object that displays a list of a given dictionary's (key, value) tuple pairs.
print("Items as tuples:", student_tuples)

# 10. Delete one item in the dictionary
del student['marital_status']
# Or using pop: student.pop('marital_status')

# 11. Delete one of the dictionaries
del dog
