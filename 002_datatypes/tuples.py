'''
tuples are immutable
() -> parenthesis
[] -> brackets
{} -> braces
'''

masala_spices = ("cardimom","Cloves","cinnemon")
(spice1,spice2,spice3) = masala_spices #unpacking
print(f"Spices are {spice1}, {spice2}, {spice3}")

print(f"Is ginger in masala spices ? {"Ginger" in masala_spices}")
print(f"Is ginger in masala spices ? {"Cloves" in masala_spices}")



ratio1,ratio2 = 1,2
print(f"ratio1 = {ratio1}, ratio2 = {ratio2}")
ratio1,ratio2 = ratio2,ratio1
print(f"ratio1 = {ratio1}, ratio2 = {ratio2}")