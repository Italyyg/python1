# create boolean variable
is_male = True
is_tall = True

# creating a if statement, then a condition to check,needs a indintation
# adding a else to respond to the opposite of the condition
# "or" works when one or both coditions are true
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male or tall")
    
# "and" work only if both conditions are true    
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are neither male or tall or both")
  
  
  
    
# elseif, another condition can be added
# else is let us respond to every combination of the variables
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and are not tall")


# IF STATEMENTS WITH COMPARISONS
# Function that takes 3 paraments and returns the highest numeber
def max_num(num1,num2,num3):
    # number 1 is greater than other variable return num1 is it is not go down the list and check other parameters
    if num1>= num2 and num1>=num3:
        return num1
    elif num2>= num1 and num2>= num3:
        return num2
    else:
        return num3

print(max_num(347,44,51))