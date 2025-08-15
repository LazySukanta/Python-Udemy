'''
union ->  |
intersection  -> &
'''

set1 = {"a","b","c"}
set2 = {"b","d","e"}

print(set1|set2)
print(set1&set2)
print(f"{"a" in set2}")
print(f"{"a" in set1}")
print(set1 - set2)