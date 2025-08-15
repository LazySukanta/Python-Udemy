ingredients = ["water","milk","tea"]
ingredients.append("sugar")
print(ingredients)
ingredients.insert(2,"wheat")
print(ingredients)

item = ingredients.pop()
print(item)

print(ingredients)

sugar_level = [1,2,4,5,7,123,3,6,6]
print(f"maximum sugar level: {max(sugar_level)}")