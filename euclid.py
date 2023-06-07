import random

#a = int(input("a の値を入力: "))
#b = int(input("b の値を入力: "))

def gojy(big,sma):
  if  big < sma:
    big,sma = sma,big

  while big % sma != 0:
    sma,big=big%sma,sma

  #so(sma)
  #return print(sma)
  return sma

def so(n):
  if n == 1:
    return print(str(a) + "と" +str(b) + "は互いに素である")
  else:
    return print(str(a) + "と" +str(b) + "は互いに素ではない")

#gojy(a,b)

#extra
count = 0 
count2 = 0

for i in range(0,100000):
  a = int(random.uniform(1,10000))
  b = int(random.uniform(1,10000))

  div = gojy(a,b)

  if div == 1:
    count += 1
  else:
    count2 += 1

print(count2/count)
