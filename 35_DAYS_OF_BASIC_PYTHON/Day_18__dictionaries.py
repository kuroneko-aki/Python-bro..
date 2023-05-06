# dictionary = A changeable, unordered collection of unique key:value
# pairs fast because they use hashing, allow us to access a value quickly/

capitals = {"Gremany":"Berlin",
            "Japan":"Tokyo", 
            "Philippines":"Manila",
            "Russia":"Moscow" }

capitals.update({"France":"Paris"})
capitals.update({"Germany":"Frankfurt"})
capitals.pop("Philippines")
#capitals.clear()

print(capitals["Russia"])
print(capitals.get("USA"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key,value)