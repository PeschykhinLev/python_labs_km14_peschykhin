# Заздалегідь вибачаюсь за дуже нечитабельний код.

def rrange(begin,end,step=1,lst1=[],lst2=[],lst3=[]):
    if begin==end or begin==-end:
        return
    else:
        if begin<end and step>0:
            lst1.append(begin+step)
            rrange(begin+step,end,step)
            return list(map(lambda x: x - step, lst1))

        if begin>end and step<0:
            lst2.append(begin+step)
            rrange(begin+step,end,step)
            return list(map(lambda x: x - step, lst2))   
     
        if begin>end and step>0:
            return lst3



x = rrange(1, 10)
y = rrange(10, 1, -1)
z = rrange(10, 1, 1)
print(x, y, z)

assert x == list(range(1, 10)), 'Failed test for simple range'
assert y == list(range(10, 1, -1)), 'Failed test for reverse range'
assert z == list(range(10, 1, 1)), 'Failed test for empty range'
print('All tests good!')