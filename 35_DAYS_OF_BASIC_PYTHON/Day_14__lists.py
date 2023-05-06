# list = used to store multiple items in a single variable

food = ["sushi","burger","nuggets","lasagna","takoyaki"]

food[1] = "pizza"

food.append("ice cream") # append will add an element to the list
#food.remove("nuggets") # remove will remove an element
#food.pop() # pop will remove the last element
food.insert(4,"cake") # insert a value at a given index
food.sort() # will sort a list alphabetically
#food.clear() # clear will remove all the elements of a list


#print(food[1])

for x in food:
    print(x)