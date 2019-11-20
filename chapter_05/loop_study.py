for i in [0, 1, 2, 3, 4, 5]:
    print(i, end=' ')

print()
for i in range(1, 10):
    print(i, end=' ')

print()
for i in range(0, 10, 2):
    print(i, end=' ')

print()
print('{} {}'.format(range(1, 10), list(range(10))))

print(list(range(0, 20, 5)))
print(list(range(-10, 0, 2)))
print(list(range(3, -10, -3)))
print(list(range(0, -5, 1)))


#gugudan


def gugu(num):
    i = num

    for j in range(1, 10):
        print(i * j, end= ' ')



gugu(2)#2단


def gugudan():
    for i in range(1, 10):
        for j in range(1, 10):
            print()
            print('{} * {} = {}'.format(i , j, i*j))
            print()

gugudan()# 전체


def gugudan_land():
    for i in range(1, 10):
        for j in range(2, 10):
            print('{} * {} = {}'.format(j, i, i*j), end='\t')
            print()




gugudan_land()#2*1 = 2 3*1=3....9*1 =9