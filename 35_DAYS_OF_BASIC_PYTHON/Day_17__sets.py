# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
dishes.update(utensils)
utensils.update(dishes)
dinner_Table = utensils.union(dishes)

#print(utensils.difference(dishes))
#print(dishes.difference(utensils))
#print(utensils.intersection(dishes))

for x in dinner_Table:
    print(x)