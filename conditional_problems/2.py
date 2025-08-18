day = 'wednesday'
age = 2

price = 12 if age >= 18 else 8
updated_price = (price - 2) if day == 'wednesday' else price

print(updated_price)