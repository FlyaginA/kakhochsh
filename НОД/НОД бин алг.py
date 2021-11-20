a = int(input())
b = int(input())
a1 = a
i=0
j=0
while (a % 2 == 0):#O(log2n)
    a = a // 2
    i+=1
while (b % 2 == 0):#O(log2n)
    b = b // 2
    j += 1
k = min(i,j)
while a != b:#O(log2n)
    if a < b:#O(1)+O(1)=O(1)
        c = a
        a = b
        b = c
    c = a - b 
    while c % 2 == 0:#O(log2n)
        c = c / 2
    a = c
c=(2**(k))*a
print ("результат работы программы:", int(c) )
input()
#Сложность алгоритма в общем случае:сложность алгоритма равна:O(log2n)+O(log2n)*O(log2n)
