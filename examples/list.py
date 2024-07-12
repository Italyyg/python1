# making a list, like a JS array
# a variable that stores multiple characters
lucky_numbers = [ 4, 8, 15, 16, 23, 42]
friends =  ["Kevin","Karen","Jim","Pam"]
            # 0     #1      #2    #3
  
#   make copies of list
friends2 = friends.copy()
print(friends2)
   
# you can change the elements in the list 
friends[1]="Michael"   
  
# We can access certain elements in the list by index, negative starts backwards from the list
print(friends[2])

# will grab starting from that index and the rest after
print(friends[1:])

# grab these from 1, grab 2 but not include 3
print(friends[1:3])

# you can use functions to group two list together
    # friends.extend(lucky_numbers)
    # print(friends)

# append individual elements onto a list
friends.append("Pam")
print(friends)

# adding to the middle of the list
friends.insert(1,"Kelly")
print(friends)

# remove an element from the list 
friends.remove("Jim")
print(friends)

# want to find an element? this returns the index 
print(friends.index("Michael"))

# finding similar elements in a list
print(friends.count("Pam"))

# to sort a list, in ascendind A-Z
friends.sort()
print(friends)

# reverse order of list
lucky_numbers.reverse()
print(lucky_numbers)

# to delete everything on the list
    # friends.clear()

# pop the last element off the list 
    # friends.pop()