from exp_root.exponentation import exp2, exp3
from exp_root.root import root2, root3
from factorial.factorial import fact
from logarithm.logarithm import log, ln, lg


def main():
 while True:

    try:
        x = int(input("\nМеню на сьогодні:\n\nДруга степінь 'n'- 1\nТретій степінь 'n' - 2\nКорінь квадратичний від 'n' - 3\nКорінь кубічний від 'n' - 4 \nФакторіал від 'n' - 5\nЛогарифм від '(n, base)' - 6\nНатуральний логарифм від 'n' - 7\nДесятичний логарифм від 'n' - 8\n\nВаш вибір: " ))
    except Exception:
        print("Невірне значення! Давайте сробуємо ще раз!")
        continue

    if x not in range(0, 9):
        print("\nМаємо всього 8 позицій меню! Повторімо!")
        print("\n---------------------------------------")
        continue

    if x == 6:
        n = int(input("Уведіть 'n': "))
        base = int(input("Уведіть 'base':"))
        if base > 0 and n > 0:
            print(round(log(n, base), 4))
        else:
            print("Обмеження логарифма! Спробуемо ще раз!")
            continue

    if x == 3:
        n = int(input("Уведіть 'n': "))
        if n >= 0:
            print(round(root2(n), 4))
        else:
            print("Число під коренем лише > 0! Спробуемо ще раз!")
            continue

    if x == 5:
        n = int(input("Уведіть 'n': "))
        if n >= 0:
            print(fact(n))
        else:
            print("Факторіал лише додатнього числа чи 0! Спробуемо ще раз!")
            continue
    if x == 7:
        n = int(input("Уведіть 'n': "))
        if n >= 0:
            print(ln(n))
        else:
            print("Натуральний логарифм лише додатнього числа! Спробуемо ще раз!")
            continue
    if x == 8:
        n = int(input("Уведіть 'n': "))
        if n >= 0:
            print(lg(n))
        else:
            print("Десятичний логарифм лише додатнього числа! Спробуемо ще раз!")
            continue

    if x == 1:
        n = int(input("Уведіть 'n': "))
        print(exp2(n))

    if x == 2:
        n = int(input("Уведіть 'n': "))
        print(exp3(n))

    if x == 4:
        n = int(input("Уведіть 'n': "))
        print(round(root3(n), 4))

    if x == 8:
        n = int(input("Уведіть 'n': "))
        print(lg(n))

    g = input("\nЧи бажаєте продовжити? '+' - так '-' ні ")
    if g == "-":
        break



if __name__ == '__main__':
    main()


