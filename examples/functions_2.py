# help you organize your code
# def tells the program you are creating a funtion, and now we name the function with a variable
#code that goes in the function must be indented
# add a parameter, something to pass through and can be more than one
def say_hi(name, age):
    print("Hello "+ name + ", you are " + str(age))
    
# call the funtion, pass parameters
say_hi("Mike",35)
say_hi("Steve", 70)


# USING RETURN STATEMENTS, getting information back from the function
# function that cubes a number
# you cannot place code after a return satement, it breaks out of the function
def cube(num):
   return num*num*num

result = cube(4)    
# this wont work without return statement
print(cube(5))
print(result)