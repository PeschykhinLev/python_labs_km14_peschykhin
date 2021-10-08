prices = [str(i) for i in input('Enter the number of objects through a space: ').split()]
lenght=len(prices)
for i in prices:
    if lenght == 1:
        print(i) 
        break 
    elif i == prices[-1]:
        print("and",prices[-1])
    elif i == prices[-2]:
        print(i,end=" ")
    else:
        print(i+",",end=" ")

