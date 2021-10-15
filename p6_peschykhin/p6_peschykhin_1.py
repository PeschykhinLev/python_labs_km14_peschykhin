x=input("Enter the first phrase: ")
phrase_1=set()
for i in x:
    if i.isalpha():
        phrase_1.add(i.lower())

y=input("Enter the second phrase: ")
phrase_2=set()
for i in y:
    if i.isalpha():
        phrase_2.add(i.lower())    

print("Letters of the first phrase: "+str(phrase_1))
print("Letters of the second phrase: "+str(phrase_2))

if len(phrase_2 - phrase_1) == 0:
    print("You can make second phrase")
else:
    print("You can`t make second phrase")
