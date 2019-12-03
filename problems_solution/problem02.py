from chapter_04.exam01 import bubble_sort

list = [-4, -1, 0, 3, 10]

for i in range(len(list)):
    list[i] *= list[i]

print(list)

list = sorted(list)

print(list)
