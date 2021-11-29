import abc
import string
from collections import Counter

file = open('gadsby.txt', 'r')
print('file.name:', file.name)
lines = file.read()

lines_lower=lines.lower()
text = [i for i in lines_lower if i.isalpha()]
print(len(text))


abc = list(string.ascii_lowercase)
c = Counter(text)

def my_counter(text,abc,x=0):
    

    d={}
    for i in text:
        if i == abc[x]:
            d.update({abc[x] : round((c[abc[x]]/len(lines_lower))*100, 3) })
            x+=1
            if x == len(list(string.ascii_lowercase)):
                break
            continue
    a = sorted(d.items(), key=lambda x: (-x[1]/len(lines_lower))) 

    for i in a[:5]+ a[-5:]:
        print(i)

    
my_counter(text,abc)    

