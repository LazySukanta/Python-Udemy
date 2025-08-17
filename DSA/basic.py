def countDigit(n):
  a = 0
  while n>0:
    n = n//10
    a = a + 1
  print(a)

countDigit(700)