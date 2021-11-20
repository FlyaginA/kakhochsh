i1 = int(input("Взять числа от 1 до  "))
j1 = int(input("По модулю от 1 до  "))
for i in range (1, i1):
    for j in range(1, j1):
        x=i
        m=j
        if len(str(x))>2*len(str(m)):
            print(f'Не выполняются условия для {i}  {j}')
            break
        k = len(str(m))
        z = int((10 ** (k * 2)) / m)
        q1 = int(int(x / (10 ** (k - 1))) * z / (10 ** (k + 1)))
        r1 = x%(10**(k+1))
        r2 = (q1 * m) % (10**(k+1))
        if r1>=r2:
            r = r1-r2
        else:
            r = (10**(k+1))+r1-r2
        while(r>=m):
            r=r-m
        rr = x%m
        if rr!=r:
            print(f'Ошибка. {x}mod{m} . Результат {r}, проверка{r1}')
            input ()
            exit()
        print("%-10d%3d%30d%30d" % (x,m,r,rr))
print ("Кол-во ошибок: 0")
input ()