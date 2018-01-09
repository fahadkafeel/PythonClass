# Exercise: 6.1 (PYTHON CRASH COURSE BOOK)
# Use a dictionary to store information about a person you know .
# Store their first name, last name, age, and the city in which they live .
# You should have keys such as first_name, last_name, age, and city .
# Print each piece of information stored in your dictionary .

user_info = {
                'First Name' : 'Muhammad',
                'Last Name': 'Kafeel',
                'Age' : 35 ,
                'City' : 'Karachi'
            }
for i,j in user_info.items():
    print(i,j)

print("-----END-----")

#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
#Think of five names, and use them as keys in your dictionary. Think of a favorite
#number for each person, and store each as a value in your dictionary. Print
#each person’s name and their favorite number. For even more fun, poll a few
#friends and get some actual data for your program

people_favourite_number ={
        'Salman': 200,
        'Ali' : 539,
        'Iqbal': 500,
        'Noman' : 60,
        'Ahmed'  : 229
    }
for i,j in people_favourite_number.items():
     print('Person_name:'+ i.title() + ' favourite number: '+ str(j) +'\n')


print("-----END-----")

#6-3. Glossar y: A Python dictionary can be used to model an actual dictionary.
#However, to avoid confusion, let’s call it a glossary.
#•	 Think of five programming words you’ve learned about in the previous
#chapters. Use these words as the keys in your glossary, and store their
#meanings as values.
#•	 Print each word and its meaning as neatly formatted output. You might
#print the word followed by a colon and then its meaning, or print the word
#on one line and then print its meaning indented on a second line. Use the
#newline character (\n) to insert a blank line between each word-meaning
#pair in your output.

programming_words = {
                        'variables': 'a variable store a value',
                        'integers' : 'it is a numeric data type',
                        'list' : 'list store a multiple value',
                        'tuple': 'tuple is a constant',
                        'if_statement': 'it is a condition',
}

for keys, values in programming_words.items():
    print(keys.title() +':\n\t\t' + values.title())

print("-----END-----")

#6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
#up the code from Exercise 6-3 (page 102) by replacing your series of print
#statements with a loop that runs through the dictionary’s keys and values.
#When you’re sure that your loop works, add five more Python terms to your
#glossary. When you run your program again, these new words and meanings
#should automatically be included in the output.

programming_words['dictionary'] = 'it is key values pair value'
programming_words['input'] = 'it is input a value'
programming_words['string']= 'it is store alphabetic value'
programming_words['forloop'] = 'it is iteration '
programming_words['functions'] = 'it is store defination'

for keys, values in programming_words.items():
    print(keys.title() +':\n\t\t' + values.title())

print("-----END-----")

#6-5. Rivers: Make a dictionary containing three major rivers and the country
#each river runs through. One key-value pair might be 'nile': 'egypt'.
#•	 Use a loop to print a sentence about each river, such as The Nile runs
#through Egypt.
#•	 Use a loop to print the name of each river included in the dictionary.
#•	 Use a loop to print the name of each country included in the dictionary.

river = {
            'nile':'egypt',
            'indus':'pakistan',
            'amazon':'south america',
            'Tigris River':'turkey',
            'Chang Jiang':'china'
}
for k,v in river.items():
    print('The '+k.title() +' runs through ' +v.title())
print("-----END-----")

#6-6. Polling: Use the code in favorite_languages.py (page 104)
#•	 Make a list of people who should take the favorite languages poll. Include
#some names that are already in the dictionary and some that are not.
#•	 Loop through the list of people who should take the poll. If they have
#already taken the poll, print a message thanking them for responding.
#If they have not yet taken the poll, print a message inviting them to take
#the poll.
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("-----END-----")

# Exercise : 6.8  (PYTHON CRASH COURSE BOOK)
# Make several dictionaries, where the name of each dictionary is the name of a pet .
# In each dictionary, include the kind of animal and the owner’s name .
# Store these dictionaries in a list called pets .
# Next, loop through your list and as you do print everything you know about each pet .


cat = {"Persian"  ,  "Sarah"}
dog = {"Bull Dog"  ,  "Peter"}
snake = {"Python"  , "Harry"}
parrot = {"Macaw"  ,  "Suzain"}
pets = [ cat  ,  dog  ,  snake  ,  parrot]
for info in pets :
    print (info)
print("-----END-----")



# Exercise : 6.9  (PYTHON CRASH COURSE BOOK)
# Make a dictionary called favorite_places .
# Think of three names to use as keys in the dictionary,
# and store one to three favorite places for each person .
# To make this exercise a bit more interesting, ask some friends to name a few of their favorite places .
# Loop through the dictionary, and print each person’s name and their favorite places .


favorite_places = {
                    "Fahad" : ["Madina" , "Switzerland" , "Canada"] ,
                    "Ali" : ["Dubai" , "Chitral" , "Paris"] ,
                    "Ahmed" : ["England" , "NewYork" , "Saif ul Malook"] ,
                    "Salman" : ["Irland" , "Zaiyarat" , "Oman"]
                  }
for key , value in favorite_places.items() :
    print (key+ "  = " +str(value))

print("-----END-----")


# Exercise : 6.10 (PYTHON CRASH COURSE BOOK)
# Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number .
# Then print each person’s name along with their favorite numbers .


fav_no = {

    "Fahad" : [ 1 , 2 ] ,
    "Ali" : [ 4 , 5 ] ,
    "Salman" : [ 3 , 17 ] ,
    "Noman" : [ 18 , 0 ] ,
    "Iqbal" : [ 2, 1 ]
}

for keys , values in fav_no.items() :
    print (keys+ "'s favorite numbers are : ")
    for value in values:
        print (value)

print("-----END-----")


# Exercise : 6.11 (PYTHON CRASH COURSE BOOK)
# Make a dictionary called cities . Use the names of three cities as keys in your dictionary .
# Create a dictionary of information about each city and include the country that the city is in,
# its approximate population, and one fact about that city .
# The keys for each city’s dictionary should be something like country, population, and fact .
# Print the name of each city and all of the information you have stored about it .


cities = {

    "lahore": {

        "country": "Pakistan", "population": "11.13 million", "fact": "Heart of Pakistan",
    },

    "karachi": {

        "country": "Pakistan" , "population": "21.2 million", "fact": "Ecnomical Hub",
    },

    "islamabad": {

        "country": "Pakistan" , "population": "1.152 million", "fact": "Capital city of Pakistan",
    },

    }
for key, value in cities.items():

    a = value["country"]
    b = value["population"]
    c = value["fact"]
    print("City = " +key.title()+ " , Country : " +a+ " , Population " +b+ " , Fact  " +c)

print("-----END-----")


# -------- OUTPUT -------
# First Name Muhammad
# Last Name Kafeel
# Age 35
# City Karachi
# -----END-----
# Person_name:Salman favourite number: 200
#
# Person_name:Ali favourite number: 539
#
# Person_name:Iqbal favourite number: 500
#
# Person_name:Noman favourite number: 60
#
# Person_name:Ahmed favourite number: 229
#
# -----END-----
# Variables:
# 		A Variable Store A Value
# Integers:
# 		It Is A Numeric Data Type
# List:
# 		List Store A Multiple Value
# Tuple:
# 		Tuple Is A Constant
# If_Statement:
# 		It Is A Condition
# -----END-----
# Variables:
# 		A Variable Store A Value
# Integers:
# 		It Is A Numeric Data Type
# List:
# 		List Store A Multiple Value
# Tuple:
# 		Tuple Is A Constant
# If_Statement:
# 		It Is A Condition
# Dictionary:
# 		It Is Key Values Pair Value
# Input:
# 		It Is Input A Value
# String:
# 		It Is Store Alphabetic Value
# Forloop:
# 		It Is Iteration
# Functions:
# 		It Is Store Defination
# -----END-----
# The Nile runs through Egypt
# The Indus runs through Pakistan
# The Amazon runs through South America
# The Tigris River runs through Turkey
# The Chang Jiang runs through China
# -----END-----
# -----END-----
# {'Sarah', 'Persian'}
# {'Peter', 'Bull Dog'}
# {'Python', 'Harry'}
# {'Macaw', 'Suzain'}
# -----END-----
# Fahad  = ['Madina', 'Switzerland', 'Canada']
# Ali  = ['Dubai', 'Chitral', 'Paris']
# Ahmed  = ['England', 'NewYork', 'Saif ul Malook']
# Salman  = ['Irland', 'Zaiyarat', 'Oman']
# -----END-----
# Fahad's favorite numbers are :
# 1
# 2
# Ali's favorite numbers are :
# 4
# 5
# Salman's favorite numbers are :
# 3
# 17
# Noman's favorite numbers are :
# 18
# 0
# Iqbal's favorite numbers are :
# 2
# 1
# -----END-----
# City = Lahore , Country : Pakistan , Population 11.13 million , Fact  Heart of Pakistan
# City = Karachi , Country : Pakistan , Population 21.2 million , Fact  Ecnomical Hub
# City = Islamabad , Country : Pakistan , Population 1.152 million , Fact  Capital city of Pakistan
# -----END-----
