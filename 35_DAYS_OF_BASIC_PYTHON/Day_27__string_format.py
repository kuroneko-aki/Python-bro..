#   str.format() = optional method that gives users
#                  more control when displaying output
#       {} = are what's known as format fields
#            they function as a placeholder for a value or a variable

animal = "cat"
item = "moon"

#print("The "+animal+" jumped over the "+item)
#print("The {} jumped over the {}".format(animal, item))
#print("The {1} jumped over the {0}".format(animal, item)) # positional argument
#print("The {animal} jumped over the {item}".format(animal = "cat", item = "moon")) # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal,item))