# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world

countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
    'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan',
    'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria',
    'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde',
    'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros',
    'Congo', 'Costa Rica', 'Cote d\'Ivoire', 'Croatia', 'Cuba', 'Cyprus',
    'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
    'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea',
    'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia',
    'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea',
    'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India',
    'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan',
    'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South',
    'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia',
    'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar',
    'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands',
    'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco',
    'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia',
    'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger',
    'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea',
    'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania',
    'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent',
    'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal',
    'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
    'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan',
    'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan',
    'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia',
    'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
    'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu',
    'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
]

m_countries = []
for country in countries:
    # if i want countries starting with 'M' i can use the following code
    if country.startswith('M'):
        m_countries.append(country)
 
print(m_countries)

fruits=['banana', 'orange', 'mango', 'lemon']
reversed_fruits=[]
for i in range(len(fruits)-1, -1, -1):
    reversed_fruits.append(fruits[i])
print(reversed_fruits)

countries_data = [
    {"name": "China", "population": 1377422166, "languages": ["Chinese"]},
    {"name": "India", "population": 1295210000, "languages": ["Hindi", "English"]},
    {"name": "United States of America", "population": 323947000, "languages": ["English"]},
    {"name": "Indonesia", "population": 258705000, "languages": ["Indonesian"]},
    {"name": "Brazil", "population": 206135893, "languages": ["Portuguese"]},
    {"name": "Pakistan", "population": 194125062, "languages": ["Urdu", "English"]},
    {"name": "Nigeria", "population": 186988000, "languages": ["English"]},
    {"name": "Bangladesh", "population": 161006790, "languages": ["Bengali"]},
    {"name": "Russian Federation", "population": 146599183, "languages": ["Russian"]},
    {"name": "Japan", "population": 126960000, "languages": ["Japanese"]}
]

# Total number of languages in the data
all_languages=set()
for country in countries_data:
    all_languages.update(country["languages"])
    # update() method is used to add the elements of a set (or any iterable), to the end of the current set. It is similar to append(), but instead of adding a single element, it adds multiple elements from an iterable.
print(len(all_languages))


# Find the ten most spoken languages from the data
language_count={}
for country in countries_data:
    for language in country["languages"]:
        if language in language_count:
            language_count[language]+=1
        else:
            language_count[language]=1

    
print(sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10])

# most populated  countries
most_populated_countries=sorted(countries_data, key=lambda x: x["population"], reverse=True)[:10]
print(most_populated_countries)