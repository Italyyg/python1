from classes_objects import Student
# importing the class file we made

# objects created based on the class we imported
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 3.8, False)

# now we can call the certain values we want from each student
print(student1.name)

print(student2.on_honor_roll())