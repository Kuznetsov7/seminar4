N = int(input('Введите число: '))
a = 0
b = 1
fibo1 =[0]
for i in range(N):
    a,b = b, a+b
    fibo1.append(a)
a = 0
b = 1
fibo2 =[]
for i in range(N):
    a,b = b, a-b
    fibo2.append(a)
fibo2.reverse()
print(fibo2 + fibo1)
