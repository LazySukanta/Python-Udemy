chai_type = {'masala':'spicy','ginger':'zesty','green':'mild'}
# print(chai_type['ginger'])
# for chai in chai_type:
#   print(chai,chai_type[chai])

# for key, value in chai_type.items():
#   print(key,value)

# if 'masala' in chai_type:
#   print("I have masala")

# a = chai_type.pop('ginger')
# print(a)
# b = chai_type.popitem()

# print(b)
# print(chai_type)

del chai_type['green']
print(chai_type)

squared_num = {x:x**2 for x in range(10)}
print(squared_num)

# Constructing new dictionary
keys = ['masala','ginger','lemon']
default_value = 'Dilicious'
new_dict = dict.fromkeys(keys,default_value)
# new_dict = dict.fromkeys(keys,keys)
print(new_dict)