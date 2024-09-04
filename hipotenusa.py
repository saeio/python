import math

def hipotenusa(a,b):
  c = math.sqrt(a**2 + b**2)
  return c

num = round(hipotenusa(10,10))
print(num)