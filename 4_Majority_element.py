def maj_el(lst, n):
    '''
    Возвращает элемент, который встречается в списке больше половины длины списка. Если такого элемента нет, то возвращает -1.

    Raises:
        TypeError: если lst не список или n не int
        ValueError: если n <= 0 или n != len(lst)
    '''

    if not isinstance(lst, list):
        raise TypeError("lst должен быть списком")
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n должно быть целым числом")
    if n <= 0:
        raise ValueError("n должен быть положительным")
    if n != len(lst):
        raise ValueError("n не совпадает с длиной списка")

    ans = -1
    counter = 0
    for a in lst:
        for b in lst:
            if b == a:
                counter += 1
        if counter > n/2:
            ans = a
        else:
            counter = 0

    return ans

namef = input('Введите имя файла (и путь к нему, если он находится в другой директории):') #rosalind_maj.txt
with open(namef) as file:
    k, n = map(int, file.readline().split())
    ans = []

    for _ in range(k):
        arr = list(map(int, file.readline().split()))
        ans.append(maj_el(arr, n))

print(*ans)
