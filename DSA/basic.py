'''
def countDigit(n):
  a = 0
  while n>0:
    n = n//10
    a = a + 1
  print(a)
countDigit(14)
'''

import math
def countDigit(n):
  if n == 0:
    return 1
  return int(math.log10(n) + 1)
print(countDigit(1110))