'''
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
'''
'''
foods = ['paneer','rice','Daal','aloo']
# a = foods.pop(2)
# print(a)
# print(foods)
# food_copy = foods[:]
food_copy = foods.copy()
food_copy[2] = 'zzzzz'
print(foods)
print(food_copy)
'''



# List Comprehension

squared_num = [x**2 for x in range(1,4)]
print(squared_num)
CUBE_NUMBER = [x**3 for x in range(10)]
print(CUBE_NUMBER)