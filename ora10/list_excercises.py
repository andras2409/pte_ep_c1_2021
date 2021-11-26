"""
1. feladat
"""
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
month = ['január','február','március','április','május','június',
         'július','augusztus','szeptember','október','november','december']
month_and_days = []
for i in range(12):
    month_and_days.append(month[i])
    month_and_days.append(days_in_month[i])
print(month_and_days)
"""
2. feladat
"""
szamok = [34,97,12,-15,35,10]

max = szamok[0]
indexmax = 0
for i in range(len(szamok)):
    if (max < szamok[i]):
        max = szamok[i]
        pozmax = i
print(max)
print(pozmax)

min = szamok[0]
indexmin = 0
for i in range(len(szamok)):
    if (min > szamok[i]):
        min = szamok[i]
        pozmin = i
print(min)
print(pozmin)