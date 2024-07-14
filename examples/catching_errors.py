# this allows you to catch errors and wont break 
# you can specify what you want to catch depending on what breaks

try:   
    # answer = 10/0 
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
