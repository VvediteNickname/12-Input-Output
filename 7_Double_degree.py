def neigbours(n, deg, all1, all2):
    '''
    Считает сумму степеней соседей вершины n+1 (n - индекс в списке, т.е. у ребра 1 n = 0)
    '''
    counter = 0
    for i in range(len(all1)):
        if all1[i] == n+1:
            counter += deg[all2[i-1]]
        elif all2[i] == n+1:
            counter += deg[all1[i-1]]
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

    deg = [0] * (v) #в этом списке будет количество рёбер к каждой вершине
    for i in range(v):
        deg[i] = all1.count(i+1) + all2.count(i+1)

    

    for x in range(v):
        print(neigbours(x, deg, all1, all2), end=' ')

        
