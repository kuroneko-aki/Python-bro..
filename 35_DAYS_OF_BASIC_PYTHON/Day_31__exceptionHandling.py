# exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("you can't divide by zero! dumbfukc!")
except ValueError as e:
    print(e)
    print("enter only numbers plz!")
except Exception as e:
    print(e)
    print("something went wrong :<")
else:
    print(result)
finally:
    print("this will always execute")