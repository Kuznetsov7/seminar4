def convertr(value):
    list = []
    result= '' 
    while value != 0:
        list.append(value%2)
        value = value//2
    list = list[::-1] #переворачиваем список
    for i in list:
        result = result + str(i) #переводим в цикле в строку
    return list
    
a = int(input('Введите число: '))
print(convertr(a))