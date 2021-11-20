x = int(input("Взять число "))
m = int(input("По модулю "))
if len(str(x))>2*len(str(m)):
    print("Не выполняются условия")
    input()
    exit()
k = len(str(m))#O(1)
z = int((10 ** (k * 2)) / m) 
q1 = int(int(x / (10 ** (k - 1))) * z / (10 ** (k + 1)))
r1 = x%(10**(k+1))
r2 = (q1 * m) % (10**(k+1))
if r1>=r2:#O(1)+O(1)
    r = r1-r2
else:
    r = (10**(k+1))+r1-r2
while(r>=m):#O(N)
    r=r-m
print("результат работы программы: ", r)
print("результат работы обычного mod: ", x % m)
#Cложность алгоритма O(1)+O(N) = O(N)