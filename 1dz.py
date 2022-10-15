list = [3,11,7,9,6]
N = len(list)
summa_chet = []
summa_nechet = []
for i in range(N):
    if i % 2 == 0:
        summa_chet.append(i)
    else:
        summa_nechet.append(list[i])
print( sum(summa_nechet))