# creating a variable for the string
phrase = "Giraffe Academy"

# this function converts the string into lower case
print(phrase.lower())

# converts string into uppercase
print(phrase.upper())

# we can also check if a string is in all uppercase or lower
print(phrase.isupper())

# you can use both together
print(phrase.upper().isupper())

# want to know how many characters are in a string?
print(len(phrase)) 

# lets get individual characters, strings index at 0
print(phrase[3])

# tell us where a specific string or character is in out string
print(phrase.index("G"))
print(phrase.index("Acad"))

# replaces certain words or letters in our strings
print(phrase.replace("Giraffe","Elephant"))