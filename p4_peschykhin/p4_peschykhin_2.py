speed = float(input("Type the tornado speed: "))
if speed<0:
    print("You've entered the negative number!!!")
elif 0<=speed<137:
    print("The potential damage is minor")
elif 137<=speed<177:
    print ("The potential damage is moderate")    
elif 177<=speed<217:
    print ("The potential damage is considerable")   
elif 217<=speed<266:
    print ("The potential damage is severe")   
elif 266<=speed<322:
    print ("The potential damage is devastating")
elif speed>=322:
    print ("The potential damage is incredible")   
