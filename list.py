# Exercises: Level 1
# Declare an empty list

# Declare a list with more than 5 items

# Find the length of your list

# Get the first item, the middle item and the last item of the list

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

# Print the list using print()

# Print the number of companies in the list

# Print the first, middle and last company

# Print the list after modifying one of the companies

# Add an IT company to it_companies

# Insert an IT company in the middle of the companies list

# Change one of the it_companies names to uppercase (IBM excluded!)

# Join the it_companies with a string '#;  '

# Check if a certain company exists in the it_companies list.

# Sort the list using sort() method

# Reverse the list in descending order using reverse() method

# Slice out the first 3 companies from the list

# Slice out the last 3 companies from the list

# Slice out the middle IT company or companies from the list

# Remove the first IT company from the list

# Remove the middle IT company or companies from the list

# Remove the last IT company from the list

# Remove all IT companies from the list

# Destroy the IT companies list

# Join the following lists:

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

# 1. Empty list
empty_list = []

# 2, 3, 4. List > 5 items & metadata
items = ['laptop', 'keyboard', 'mouse', 'monitor', 'desk', 'chair']
length = len(items)
first = items[0]
middle = items[length // 2]
last = items[-1]

# 5. Mixed data types
mixed_data_types = ['Zakaria', 22, 1.75, 'Single', 'Nairobi']

# 6, 7, 8, 9. IT Companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("IT Companies:", it_companies)
print("Count:", len(it_companies))

comp_len = len(it_companies)
print(f"First: {it_companies[0]}, Middle: {it_companies[comp_len // 2]}, Last: {it_companies[-1]}")

# 10. Modify a company
it_companies[0] = 'Meta'

# 11. Add an IT company
it_companies.append('Twitter')

# 12. Insert in middle
mid_idx = len(it_companies) // 2
print("Middle index:", mid_idx)
it_companies.insert(mid_idx, 'Netflix')
print("After insertion:", it_companies)

# 13. Uppercase one name (excluding IBM)
it_companies[1] = it_companies[1].upper()  # 'GOOGLE'

# 14. Join with string
joined_str = '#;  '.join(it_companies)
print("Joined string:", joined_str)

# 15. Check existence
print("Is Apple in list?", 'Apple' in it_companies)

# 16 & 17. Sort and Reverse
it_companies.sort()
print("Sorted:", it_companies)
it_companies.sort(reverse=True)
print("Descending:", it_companies)

# 18, 19, 20. Slicing
first_3 = it_companies[:3]
last_3 = it_companies[-3:]
print("First 3:", first_3)
print("Last 3:", last_3)

# Middle company slice logic (handles even/odd lengths)
mid_start = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[mid_start - 1 : mid_start + 1]
else:
    middle_companies = [it_companies[mid_start]]

# 21, 22, 23. Removals
it_companies.pop(0)  # Remove first
print("After removing first:", it_companies)
mid_idx = len(it_companies) // 2
it_companies.pop(mid_idx)  # Remove middle
print("After removing middle:", it_companies)

it_companies.pop()  # Remove last
print("After removing last:", it_companies)

# 24 & 25. Clear and Destroy
it_companies.clear()
del it_companies

# 26 & 27. Front-end / Back-end Stack Assembly
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_stack = front_end + back_end
print("Joined Stack:", joined_stack)

full_stack = joined_stack.copy()
redux_idx = full_stack.index('Redux')
print("Redux index:", redux_idx)
full_stack.insert(redux_idx + 1, 'Python')
full_stack.insert(redux_idx + 2, 'SQL')