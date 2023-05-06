# if statement = a block of code that will execute if it's condition is true

age = int(input("Enter your age: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print(" you're an adult bruh")
elif age <0:
    print("you haven't been born yet")
else:
    print("you are a child!")