from math import sin
from math import pi 

a = 0
b = pi/2
n = 100
f = sin

h = (b-a)/n
s = 0

for i in range(1 , n+1):
    s = s + f(a + (i-1)*h) + f(a + i*h)

s = s * h /2

print(s)
