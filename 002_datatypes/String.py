# Encoding Decoding
'''
when delaing with japanese spanish or chinese etc character we encode it then we can decode later
'''

label = "Chai or Chài"
encoded_lebel = label.encode("utf-8")
print(f"non encoded lebel = {label}")
print(f"encoded lebel = {encoded_lebel}")
decoded_lebel = encoded_lebel.decode("utf-8")
print(f"decoded lebel = {decoded_lebel}")
