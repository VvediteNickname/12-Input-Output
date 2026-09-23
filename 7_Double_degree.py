def neigbours(n, deg, all1, all2):
    '''
    Считает сумму степеней соседей вершины n
    '''
    counter = 0
    for i in range(len(all1)):
        if all1[i] == n:
            counter += deg[all2[i]]
        elif all2[i] == n:
            counter += deg[all1[i]]
    return counter

namef = input('Введите имя файла (и путь к нему, если он находится в другой директории): (7task.txt, 7task2.txt) ')
with open(namef) as file:
    first = file.readline().split()
    v, r = map(int, first) 
    all1 = [] #кто
    all2 = [] #с кем связан
    for line in file:
        a, b = map(int, line.split())
        all1.append(a)
        all2.append(b)

    deg = [0] * (v + 1) #считает количество рёбер к каждой вершине
    for i in range(1, v+1):
        deg[i] = all1.count(i) + all2.count(i)

    

    for x in range(1, v+1):
        print(neigbours(x, deg, all1, all2), end=' ')

        
