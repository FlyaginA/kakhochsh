x= int(input("введите X "))
y= list(bin(int(input("введите Y "))))
q=x
del y[0:2]#O(2)
y.reverse()
if (y[0] == '1'):
    z = x
if (y[0] == '0'):
    z= 1
for i in range(1,len(y)):#O(N)
    q = q*q
    if (y[i] == '1'):
        z=z*q
print ("Результат работы программы:",z)
input()
#Сложность алгоритма: O(2)+O(N) = O(N) в общем случае