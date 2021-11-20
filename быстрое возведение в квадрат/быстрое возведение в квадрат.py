#N - КОЛ-ВО ЗНАКОВ В ДВОИЧНОМ ПРЕДСТАВЛЕНИИ
x = list(input("Введите число \n"))
#step 1 O(2N)
y = [0 for i in range(2*len(x))] #O(2*N)
x = [int(i) for i in x]#O(len(X))
x.reverse()#(O(len(x)))
#step 2.1
for i in range(len(x)):#O(N^2)
    uv = y[2*i]+x[i]*x[i] 
    c = 0
    u = uv //10
    v = uv % 10 
    y[2*i] = v
    
    for j in range(i+1, len(x)):#O(N)
        #step 2.2
        cuv =   y[i+j] + 2*x[i]*x[j] + c*10 + u
        c = cuv //100
        u = cuv//10%10
        v = cuv%10
        y[i+j] = v 
    #step 2.3 O(1)+O(1)
    if (i+len(x)+1 < len(y)):
        y[i+len(x)+1] += c #c
    y[i+len(x)] += u
#step 3 #O(N)
y.reverse() 
while (y[0] == 0):
    y.pop(0)
for i in y:
    print(i,end = '')
print('')
input("введите любой символ для закрытия программы")
#сложность алгоритма O(2N)+O(N^2)+O(N) = O(N^2)
