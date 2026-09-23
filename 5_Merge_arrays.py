namef = input('Введите имя файла (и путь к нему, если он находится в другой директории): (rosalind_merge.txt) ')
with open(namef) as file: #rosalind_merge.txt
    lines = file.readlines()
    n = int(lines[0])
    lst1 = list(map(int, lines[1].split()))
    m = int(lines[2])
    lst2 = list(map(int, lines[3].split()))

ans = []
a, b = 0, 0

while a < n and b < m:
    if lst1[a] <= lst2[b]:
        ans.append(lst1[a])
        a += 1
    else:
        ans.append(lst2[b])
        b += 1

while a < n:
    ans.append(lst1[a])
    a += 1
while b < m:
    ans.append(lst2[b])
    b += 1

print(*ans)