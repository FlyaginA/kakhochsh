import math
a1 = int(input("первое число от 1 до "))
b1 = int(input("второе число от 1 до "))

for p in range ( 1, a1+1):
    for l in range (1, b1+1):
        a = p
        b = l
        i = 0
        j = 0
        while (a % 2 == 0):
            a = a / 2
            i+=1
        while (b % 2 == 0):
            b = b // 2
            j += 1
        k = min(i,j)
        while a != b: 
            if a < b:
                c = a
                a = b
                b = c
            c = a - b 
            while c % 2 == 0:
                c = c / 2
            a = c
        c=(2**(k))*a
        print (f'{int(p):10} {int(l):10} {int(c):10} {int(math.gcd(p,l)):10} ')
        if c!= math.gcd(p,l):
            print (f'Ошибка!')
            input()
            exit
print('Успешно')
input()
        
