import random as rnd
from chapter_04.exam01 import bubble_sort

if __name__ == "__main__":

    random_list = []
    rnd.seed(4)
    for num in range(1, 10):
        random_list.append(rnd.randint(1, 46))

        sorted_list = bubble_sort(random_list)

    print('{}'.format(sorted_list))

    search_key = 4
    len = len(sorted_list)
    i = 0
    left = i
    right = len
    while True:
        mid = (left + right) // 2
        if sorted_list[i] == search_key:
            print('res_index = {} search_key = {}'.format(i, search_key))
            break
        else:
            left = mid + 1
            right = right - 1
        i += 1

        if i == len:
            print('존재하지않음', 'search_key = {}'.format(search_key))
            break

