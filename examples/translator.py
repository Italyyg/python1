# function that grabs the phrase thtat the user inputs and runs a loop through
# it to seperate the letter and check is that letter is in the string of vowels
# if so make that letter into a g then return in


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
             translation = translation + "g"
        else:
            translation = translation +letter
    return translation


print(translate(input("Enter a phrase: ")))

