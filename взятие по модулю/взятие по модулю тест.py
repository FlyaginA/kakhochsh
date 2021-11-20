i1 = int(input("взять числа от 1 до "))
m = int(input("по модулю:"))
for i in range(1, i1+1):
    x=i
    bt = 10 ** (len(str(m)))
    c = bt - m
    q = x // bt
    r = x % bt
    while q > 0:
        r1 = (q * c) % bt
        r = r+r1
        q = (q * c) // bt
    while r >= m:
        r = r - m
    print(f'{x:10} {m:10} {r:10} {(i % m):10} ')
    if r != i%m:
        print("ОШИБКА")
        exit
print("успешно")
input()

