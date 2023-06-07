from math import sin
from math import pi
from math import exp 

def f(x):
    fun = pi**(1/2) * exp(-x**2)
    return fun

def dai(a=0,b=1,n=100):
    h = (b-a)/n
    s = 0

    for i in range(1 , n+1):
        s += f(a + (i-1)*h) + f(a + i*h)

    s = s * h /2
    return s

result = dai(-100,100,1000)

print(result)
