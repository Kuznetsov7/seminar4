from random import randint
imput_proverka = True
while imput_proverka:
    len_list = input('Введите длину списка: ')
    try:
        len_list = int(len_list)
        if len_list <= 0:
            print('нужно число больше 0: ')
            imput_proverka = True
        else:
            imput_proverka = False
    except ValueError:
        print('не правильный ввод')

list = []
for i in range(len_list):
    list.append(randint(0,10)) # заполняем список случайными числами

print(f'список из {len_list} элементов')
print(list)

list_para =[]
if len(list) == 2:
    list_para.append(list[0] * list[1])
else:
    if len(list)%2 == 0:
        for i in range(len(list)// 2):
            list_para.append(list[i]*list[len(list)- i-1])
    else:
        for i in range(len(list)// 2+1):
            list_para.append(list[i]*list[len(list)- i-1])
print(list_para)