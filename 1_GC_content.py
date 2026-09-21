def gc_content(a):
    counter = 0
    for x in a:
        if x in 'GC':
            counter += 1
    return counter/len(a)

def parse_file(filename):
    '''
    Создаёт словарь типа {ID: последовательность}
    '''
    result = {}
    current_key = None

    with open(filename) as file:
        for line in file:
            line = line.rstrip("\n")

            if line.startswith(">"):
                current_key = line[1:]
                result[current_key] = ""
            else:
                if current_key is not None:
                    result[current_key] += line

    return result

namef = input('Введите имя файла (и путь к нему, если он находится в другой директории):') #rosalind_gc.txt
d = parse_file(namef)
gc = -1
i = None #айди
for k, v in d.items():
    content = gc_content(v)
    if content > gc:
        gc = content
        i = k

print(i)
print(gc)