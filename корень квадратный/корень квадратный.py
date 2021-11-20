a = int(input("введите число:"))
x = a 
x0 = x
x = int((int(a / x) + x ) / 2)
while not (x >= x0):#O(N)
    x0 = x
    x = int((int(a / x) + x ) / 2)  
print("результат работы программы:", x0)
#В общем случае сложность алгоритма равна: O(N)+O(1)=O(N)
