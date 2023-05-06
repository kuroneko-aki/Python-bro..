# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguments that our functions receives

def hello(first, second, third, fourth):
    print("Hello "+first+" "+second+" "+third+" "+fourth)

hello(second="morax", fourth="buer", third="beelzebul", first="barbatos")