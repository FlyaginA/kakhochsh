CountOfErrors = 0
CountOfCircles = int(input("введите порог проверки от 1 до ..."))
for circle in range(1,CountOfCircles):
    x = list(str(circle))
    #step 1
    y = [0 for i in range(2*len(x))]
    x = [int(i) for i in x]
    x.reverse()
    #step 2.1
    for i in range(len(x)):
        uv = y[2*i]+x[i]*x[i] 
        c = 0
        u = uv //10
        v = uv % 10 
        y[2*i] = v
        
        for j in range(i+1, len(x)):
            #step 2.2
            cuv =   y[i+j] + 2*x[i]*x[j] + c*10 + u
            c = cuv //100
            u = cuv//10%10
            v = cuv%10
            y[i+j] = v 
        #step 2.3
        if (i+len(x)+1 < len(y)):
            y[i+len(x)+1] += c #c
        y[i+len(x)] += u
    #step 3
    y.reverse() 
    while (y[0] == 0):
        y.pop(0)
    for i in y:
        print(i,end = '')
    if (str(y) != str(circle*circle)):
        test = 0
        CountOfErrors += test
    print(' ',circle*circle,' ',test)
print("CountOfErrors:",CountOfErrors)
input()

