import math

def hipotenusa(a,b):
  # calculates the hypotenuse of the values a, b and returns c
  c = math.sqrt(a**2 + b**2)
  return c

num = round(hipotenusa(10,10))
print(num)
