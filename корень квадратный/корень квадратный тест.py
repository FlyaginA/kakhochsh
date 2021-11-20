import math
i1 = int(input("числа от 1 до "))
for i in range (1,i1+1):
    a = i
    x = a 
    x0 = x
    x = int((int(a / x) + x ) / 2)
    while not (x >= x0):
        x0 = x
        x = int((int(a / x) + x ) / 2)  
    print(f'{i:10} {x0:10}  {(int(math.sqrt(i))):10}')
    if x0 != int(math.sqrt(i)) :
        print("Ошибка!")
        input()
        exit
print("Успешно!")
input()



