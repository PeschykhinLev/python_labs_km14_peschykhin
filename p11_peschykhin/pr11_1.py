# МІЙ КОД ТУТ
def cons(head,tail=[]):
    tail.insert(0,head)
    return tail

# ПЕРЕВІРКА

l = cons(3, cons(2, cons(1, [])))
print(f'Result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')



# МІЙ КОД ТУТ 1.2
def sum(x):
    if x==[]:
        return 0
    else:
        return x[0]+sum(x[1:]) 
        
# ПЕРЕВІРКА

#print(sum(l))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')