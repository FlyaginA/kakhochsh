x = int(input("Взять число: " ))
m = int(input("По модулю: "))
bt = 10 ** (len(str(m)))
c = bt - m
q = x // bt
r = x % bt  
while q > 0:#O(N)
    r1 = (q * c) % bt
    r = r+r1
    q = (q * c) // bt
while r >= m:#O(N)
    r = r - m
print(f'Результат работы алгоритма:{r}')
input()
#Сложность алгоритма в общем случае равна  О(N)+O(N)=O(N)