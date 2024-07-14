# allows us to loop from diffrent collections of items
# for every single item in this specific array,string, number, etc..
# letter can be anything, make it fit what you are doing but it could be like potato
# loops thorugh the string and grabs the individual parts of it until there is no more to pull
for letter in "Giraffe Academy":
    print(letter)
    

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)
    
for index in range(len(friends)):
    print(friends[index])    
    
for index in range(5):
    if index == 0:
        print ("first Iteration")
    else:
        print("Not first iteration")