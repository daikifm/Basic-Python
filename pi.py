text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""
text1 = text.replace(',' or '.', '') 

list1 = text1.split()

word_num = list(map(len,list1))

pi = ""

for i in word_num:
    pi =  pi + str(i)

print(pi)
