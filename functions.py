# A prime number is any integer greater than 1 divisible only by 1 and itself
def is_prime(n):
    if n <=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
result=[]
for num in range(1, 101):
    if is_prime(num):
        result.append(num)
print(result)

# Write a functions which checks if all items are unique in the list.
# Write a function which checks if all the items of the list are of the same data type.
# Write a function which check if provided variable is a valid python variable
# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

def all_unique(list):
    return len(list) == len(set(list))
result = all_unique([1, 2, 3,3,4, 4, 5])
print(result)  # Output: False

def all_same_type(list):
    if not list:
        return True
    first_type =type(list[0])
    return all(isinstance(item, first_type) for item in list)
result = all_same_type([1, 2, 3, 4, 5])
print(result)  # Output: True

# isinstance() function is used to check if a variable is of a specific type.
# all() function is used to check if all items in an iterable are true.

def most_spoken_languages(languages_data, top_n=10):
    sorted_languages = sorted(languages_data.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:top_n]

result = most_spoken_languages({'English': 1500, 'Mandarin': 1100, 'Hindi': 600, 'Spanish': 500, 'French': 300})
print(result)  # Output: [('English', 1500), ('Mandarin',
    

def most_populated_countries(countries_data, top_n=10):
    sorted_countries = sorted(countries_data.items(), key= lambda x: x[1], reverse=True)
    return sorted_countries[:top_n]
result = most_populated_countries({'China': 1400, 'India': 1300, 'USA': 330, 'Indonesia': 270, 'Pakistan': 220})
print(result)  # Output: [('China', 1400), ('India', 1300), ('USA', 330), ('Indonesia', 270), ('Pakistan', 220)]