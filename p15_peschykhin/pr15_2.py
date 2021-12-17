
def card_generator():
    suites =("diamonds", "clubs", "hearts", "spades")
    elements=("A",*range(1,10),"J","Q","K")
    n=0
    y=0
    while n<13:
        if n<13:
            yield (f"{elements[n]} {suites[y]}")
            n+=1
        else: 
            n=0
            y+=1
            yield (f"{elements[n]} {suites[y]}")
            n+=1    

              
x = card_generator() 

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

