from math import sin
import math

a = 0
b = math.pi/2
n = 100

h = (b-a)/n

for i in (1 , n):
    s = sin(a + (i-1)*h) + sin(a + i*h)

s = s * h /2

print(s)
