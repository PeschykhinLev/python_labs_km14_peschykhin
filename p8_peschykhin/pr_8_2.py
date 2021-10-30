import math


try:
    a=float(input("Enter 'a' value: "))
    b=float(input("Enter 'b' value: "))
    c=float(input("Enter 'c' value: "))

    D=b**2-4*a*c 

    if D<0: raise Exception ("Discriminant is less than 0, so there are no roots")
    x1= (-b + math.sqrt(D))/2*a
    x2= (-b - math.sqrt(D))/2*a

    print("Discriminant = "+str(D))
    if (x1 == x2): 
        print("x = "+str(x1))
    else:
        print("x1 = "+str(x1)+"\n"+"x2 = "+str(x2))
except TypeError as er:
    print("'Float/Int' types only"+str(er))  
except ZeroDivisionError as errrr:
    print("'A' must be > 0. No divission by zero!"+"Defenition of your error: "+str(errrr))
except ValueError as errr:
    print("There must be 3 digit numbers!"+" Defenition of your error: "+str(errr))    
except Exception as err:
    print(err)