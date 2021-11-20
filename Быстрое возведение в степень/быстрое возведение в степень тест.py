j0 = int(input("числа от 1 до "))
k0 = int(input("возводим в степень от 1 до "))
s = 0
for j in range(1,j0+1):
    for k in range (1, k0+1 ):
        x= j
        y= list(bin(k))
        q=x
        del y[0:2]
        y.reverse()
        if (y[0] == '1'):
            z = x
        if (y[0] == '0'):
            z= 1
        for i in range(1,len(y)):
            q = q*q
            if (y[i] == '1'):
                z=z*q
        z1 = x**k
        if z==z1:
            t=0
        if z!=z1:
            t=1
        
        s = s + t
        print ("%-10d%3d%30d%30d%3d" % (int(j),int(k), int(z), int(z1) ,int(t)))
print ("кол-во ошибок:", s)
input()