# reading files outside of your python files,how you place it depends on directory
# Read, Write, Append-add new, R+-read and write
# opening the file
employee_file = open("employees.txt","r")

# prints all the info in the file
print(employee_file.read())

# can use a for loop to go through the file
  # for employee in employee_file.readlines():
   #     print(employee)


# individually reads line by the top
   # print(employee_file.readlines())

# allows you to see if the file is readable
   # print(employee_file.readable())

# to close a file,good practice
employee_file.close()