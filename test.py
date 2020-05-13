def je_prastevilo(n):
    '''Funkcija , ki pove, ali je podeano stevilo prastevilo'''
    if n < 2:
        return False
    if n== 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i ** 2 <= n:
        if n % i == 0:
            return False
        else:
            i += 2
    return True

for i in range(1000):
    if je_prastevilo(i):
        print(i)