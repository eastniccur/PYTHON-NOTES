# --- Concatenation & Assignment ---
# Ex 1 & 2: Concatenation
thirty_days = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
coding_all = ' '.join(['Coding', 'For', 'All'])

# Ex 3, 4, 5: Variable & Metadata
company = "Coding For All"
print(company)
print(f"Length: {len(company)}")

# Ex 6, 7, 8: Formatting Transformations
print(company.upper()) #ALL UPPERCASE
print(company.lower()) #all lowercase
print(company.capitalize()) #First letter uppercase
print(company.title()) #Title Case capitalizes the first letter of each word
print(company.swapcase()) #Swap Case makes the first letter of each word lowercase and the rest uppercase

# Ex 9: Slice out first word ("Coding")
first_word = company.split()[0]  # or company[0:6]

# Ex 10, 11, 12: Searching & Replacing
print("Contains 'Coding':", company.find('Coding') != -1)
print(company.replace('Coding', 'Python'))
print("Python for Everyone".replace("Everyone", "All"))

# Ex 13, 14: Splitting Sequences
print(company.split())
tech_str = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_str.split(', '))

# Ex 15, 16, 17: Indexing
print(f"Index 0: {company[0]}")
print(f"Last Index: {len(company) - 1}")
print(f"Index 10: {company[10]}")  # ' ' (space)

# Ex 18, 19: Acronym Generation (Engineered approach)
pfe = 'Python For Everyone'
cfa = 'Coding For All'
acronym_pfe = ''.join([word[0] for word in pfe.split()])
acronym_cfa = ''.join([word[0] for word in cfa.split()])
print(f"Acronym PFE: {acronym_pfe}")  # PFE
print(f"Acronym CFA: {acronym_cfa}")  # CFA

# Ex 20, 21, 22: Index Searches
print("Index of 'C':", company.index('C'))
print("Index of 'F':", company.index('F'))
print("Last index of 'l':", "Coding For All People".rfind('l'))

# Ex 23 - 27: Sentence Manipulation
sentence = 'You cannot end a sentence with because because because is a conjunction'
first_because = sentence.find('because')
last_because = sentence.rfind('because')

print(f"First 'because' index: {first_because}")
print(f"Last 'because' index: {last_because}")

# Slicing out 'because because because'
phrase = 'because because because'
start_idx = sentence.find(phrase)
sliced_sentence = sentence[:start_idx] + sentence[start_idx + len(phrase) + 1:]
print(f"Sliced sentence: {sliced_sentence}")

# Ex 28, 29, 30: Prefix, Suffix, Whitespace
print(company.startswith('Coding'))   # True
print(company.endswith('coding'))     # False
print('   Coding For All      '.strip())

# Ex 31: Identifiers
print("30DaysOfPython is identifier:", "30DaysOfPython".isidentifier())         # False
print("thirty_days_of_python is identifier:", "thirty_days_of_python".isidentifier()) # True

# Ex 32: Joining Libraries
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libs))

# Ex 33 & 34: Escape Sequences
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# Ex 35 & 36: Formatting Calculations
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")

a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")