# logical operators (and, or, not) = used to check if two or more conditional statements are true

temp = int(input("Enter temperature: "))

#if temp >= 0 and temp <= 30:
#    print("The temperature is good today!")
#    print("GO OUT AND TOUCH SOME GRASS YOU WEIRD FUCK!")
#elif temp < 0 or temp > 30:
#    print("the temperature is bad today!")
#    print("STAY FUCKING PUT INSIDE!")

if not(temp >= 0 and temp <= 30):
    print("the temperature is bad today!")
    print("STAY FUCKING PUT INSIDE!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today!")
    print("GO OUT AND TOUCH SOME GRASS YOU WEIRD FUCK!")



