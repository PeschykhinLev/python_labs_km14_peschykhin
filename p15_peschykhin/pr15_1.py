def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n-1)

def binom(power):
    value = 0
    while value <= power:
        yield fact(power)/(fact(power-value)*fact(value))
        value +=1

def result(n,g=0):
    if n<g:
        return 0
    else:    
        for i in binom(g):
            print(int(i), end =" ")
    print()        
    result(n,g+1)

while True:
    try:
        n = int(input("Введіть степінь: "))
        if n<0:
            raise TypeError
    except ValueError:
        print("Невірний формат! Лише числа! Спробуйте ще раз!")
        continue 
    except TypeError:
        print("Лише натуральні числа, будь-ласка!")
        continue

    result(n)

    m=input("\nЧи бажаєте продовжити? '+' - так '-' ні " )
    if m=="-":
        break

