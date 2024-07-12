num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# automatically the input is classified as a string so we must be specific with the input we want
# can use int but it doesnt allow decimals but float does
result = float(num1) + float(num2)

print(result)