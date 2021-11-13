import numpy as np

# Перше завдання 
years = np.arange(1900, 2020+3, 1)

a=list(filter(lambda x: x%400 != 0, years))
b=list(filter(lambda x: x%4 == 0, a))
c=list(filter(lambda x: x%400 == 0,years))

years_1 = sorted(b+c)
print("Високосні"+str(years_1))

# Друге завдання