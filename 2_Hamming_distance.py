def hamming_distance(s, t):
    '''
    Считает расстояние Хэмминга между двумя строками равной длины.

    Raises:
        TypeError: если s или t не строки
        ValueError: если длины строк не совпадают
    '''
    if not isinstance(s, str) or not isinstance(t, str):
        raise TypeError("Аргументы должны быть строками")
    if len(s) != len(t):
        raise ValueError("Строки должны быть одинаковой длины")

    distance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            distance +=1

    return distance

with open('rosalind_hamm.txt') as file:
    lines = file.readlines()
    s = lines[0].strip()
    t = lines[1].strip()
    print(hamming_distance(s, t))