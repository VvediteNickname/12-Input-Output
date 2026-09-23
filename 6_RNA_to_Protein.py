text = '''
UUU F CUU L AUU I GUU V
UUC F CUC L AUC I GUC V
UUA L CUA L AUA I GUA V
UUG L CUG L AUG M GUG V
UCU S CCU P ACU T GCU A
UCC S CCC P ACC T GCC A
UCA S CCA P ACA T GCA A
UCG S CCG P ACG T GCG A
UAU Y CAU H AAU N GAU D
UAC Y CAC H AAC N GAC D
UAA Stop CAA Q AAA K GAA E
UAG Stop CAG Q AAG K GAG E
UGU C CGU R AGU S GGU G
UGC C CGC R AGC S GGC G
UGA Stop CGA R AGA R GGA G
UGG W CGG R AGG R GGG G
'''

text = text.split()
codon_table = dict(zip(text[::2], text[1::2]))

namef = input('Введите имя файла (и путь к нему, если он находится в другой директории): (rosalind_prot.txt, 6task.txt) ')
with open(namef) as file:
    s = file.read().strip()

ans = ''
for i in range(len(s)//3):
    if codon_table[s[:3]] == 'Stop':
        break
    else:
        ans = ans + codon_table[s[:3]]
        s = s[3:]

print(ans)
