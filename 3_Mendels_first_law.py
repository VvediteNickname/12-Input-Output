def p_aa(lst):
    '''
    Функция ищет вероятность того, что у потомков проявится рецессивный признак.

    Raises:
        TypeError: если аргументы не являются целыми числами
        ValueError: если числа отрицательные или всего организмов < 2
    '''
    k = int(lst[0]) #AA
    m = int(lst[1]) #Aa
    n = int(lst[2]) #aa

    if k < 0 or m < 0 or n < 0:
        raise ValueError("Числа не могут быть отрицательными")

    N = k + m + n
    if N < 2:
        raise ValueError("Нужно минимум два организма")
    
    '''
    Aa + Aa: m/N * (m-1)/(N-1)
    Aa + aa: m/N * n/(N-1) * 2
    aa + aa: n/N * (n-1)/(N-1)

    p(aa):
    Aa + Aa: 1/4
    Aa + aa: 1/2
    aa + aa: 1
    '''
    p = (m/N * (m-1)/(N-1))*(1/4) + (m/N * n/(N-1) * 2)*(1/2) + (n/N * (n-1)/(N-1))*1
    return p

namef = input('Введите имя файла (и путь к нему, если он находится в другой директории): (rosalind_iprb.txt) ') #rosalind_iprb.txt
with open(namef) as file:
    line = file.readline().split()
    q = p_aa(line)
    p = 1 - q

'''
#Для проверки:

line = input().split()
q = p_aa(line)
p = 1 - q
'''

print(f"{p:.5f}") 