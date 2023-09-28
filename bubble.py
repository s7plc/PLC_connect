from random import randint

#N = 14

a = [2, 6, 7, 9, 2, 4, 2, 7, 6, 5, 6, 4, 2, 5, 6]
N = len(a)
#for i in range(N):
#    a.append(randint(1, 99))
print(a)

i = 0
while i < N - 1:
    j = 0
    while j < N - 1 - i:
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
        j += 1
    i += 1

print(a)