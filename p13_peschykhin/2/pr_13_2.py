from functools import partialmethod
import string
string.digits
import re
from collections import Counter

x=1880
boys=[]
girls=[]

while x<=2019:

    file = open(f"archive/yob{x}.txt", "r")

    lines = file.read()
    text = [i for i in lines]

    text_look_for = r"\w+,F,\d+"
    allresults = re.findall(text_look_for,lines)
    girls.append(allresults[0])

    text_look_for2 = r"\w+,M,\d+"
    allresults2 = re.findall(text_look_for2,lines)
    boys.append(allresults2[0])

    x+=1


boys1 = [x.rstrip(string.digits) for x in boys]
boys2 = [x.strip("M, ") for x in boys1]
boys_top = dict(Counter(boys2))
boys_top1 = sorted(boys_top.items(), key=lambda x: -x[1]) 

print("\nTop Male names:\n")
for i in boys_top1:
    print(i)


print("\n------------\n")
print("Top Female names:\n")

girls1 = [x.rstrip(string.digits) for x in girls]
girls2 = [x.strip("F, ") for x in girls1]
girls_top = dict(Counter(girls2))
girls_top1 = sorted(girls_top.items(), key=lambda x: -x[1]) 

for i in girls_top1:
    print(str(i))






