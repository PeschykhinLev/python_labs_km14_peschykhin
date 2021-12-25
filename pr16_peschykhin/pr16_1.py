
#не вийшло зробити з декоратором та функцією, але завдання реалізував так.

while True:

    while True:
        n = int(input("Введіть кулькість сторінок у вашій книзі (кратне 16) : "))
        try:
            b = int()
        except Exception:
            print("Будь-ласка цілі числа")  
            continue

        if n % 16 == 0:
            break
        else:
            print("Невірне значення")
            continue


    list11 = [*range(1,n+1)]
    w =[list11[i:i + 16] for i in range(0, len(list11), 16)]
    total = []
    for i in w:
        y=15
        x=0
        page = []
        while True:
            if y == 7:
                page[2::4], page[3::4] = page[3::4], page[2::4] 
                total.append(page)
                break
            else:
                page.append(i[y]) 
                page.append(i[x])
                x+=1
                y-=1 
    print(f"Без розділень: ")
    print(total)
    print(f"\nЗ розділеннями: ")
    def split(total, n=0):
        if n == len(total):
            return 0
        total[n]=[total[n][i:i + 4] for i in range(0, len(total[n]), 4)]
        split(total,n+1)
        return total

    print(split(total))

    g=input("\nЧи бажаєте продовжити? '+' - так '-' ні " )
    if g=="-":
        break    
