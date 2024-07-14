# want to add new line to text file
# "w"-create a new file and overrides a file if you link it 
employees_file = open("employees.txt","a")

employees_file.write("\nKelly - Customer Service")

employees_file.close()

# employee_file = open("index.html","w")
# employee_file.write("<p>This is HTML</p>")
# employee_file.close()
