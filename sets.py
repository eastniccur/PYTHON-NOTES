# Exercises: Level 1
# Find the length of the set it_companies
# Add 'Twitter' to it_companies
# Insert multiple IT companies at once to the set it_companies
# Remove one of the companies from the set it_companies
# What is the difference between remove and discard

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Length of set
print("Number of companies:", len(it_companies))

# 2. Add 'Twitter'
it_companies.add('Twitter')
print("Companies after adding Twitter:", it_companies)
# 3. Add multiple companies at once
it_companies.update(['Netflix', 'Tesla', 'Spotify'])
print("Companies after adding multiple:", it_companies)
# 4. Remove one company
it_companies.remove('IBM')
print("Companies after removing IBM:", it_companies)


# 5. Difference between remove() and discard():
# it_companies.remove('NonExistentCompany')  # This will raise a KeyError
# .remove('X') raises a KeyError if 'X' is not in the set.
it_companies.discard('NonExistentCompany')  # This will not raise an error
# .discard('X') quietly does nothing if 'X' is not found (safer when uncertain).