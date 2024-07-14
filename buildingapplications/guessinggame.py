# creating a variable with the secret word
secret_word = "giraffe"
# variable to store the users input
guess = ""
# how many times has the user guessed?
guess_count = 0
# this is going to limit the amount of guessses
guess_limit = 3
# boolean to figure out if they have chances
out_of_guesses = False


# while loop to continue to ask the user to guess until they guess correctly
# want to check that they havent used all guesses
# # after each guess the guess count adds one

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
    
    
if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")  
else:
    print ("You win!")
    