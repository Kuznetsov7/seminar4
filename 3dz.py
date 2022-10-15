
list = [1.82,1.43,5,10.66,1.3]

res = []
for i in list:
    i = str(i) #переводим элементы в строку
    if i.find('.')!= -1: 
        j = i.find('.')
        res.append(i[j:]) #записываем то что идет после точки
res_2 = []

for j in res:
    res_2.append(float(j))
print(res_2)
res_2.sort() #сортируем от меньшего к большему
print(res_2)
print(round((res_2[-1]*res_2[0]),2))