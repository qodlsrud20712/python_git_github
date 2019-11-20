tu1 = (1, 2, 3, 4)

print("tu1{} type: {}".format(tu1, type(tu1)))

tu2 = (5, 6, 7, 8)

print('tu2{} type: {}'.format(tu2, type(tu2)))

tu3 = (9,)
tu4 = 10,

print('tu3{} type: {}'.format(tu3, type(tu3)))
print('tu4{} type: {}'.format(tu4, type(tu4)))

t_li = [tu1, tu2, tu3, tu4]

print('t_li {}'.format(t_li))

print("{} {}".format(tu1[1], tu1.index(2)))

# 로또번호생성기를 작성하고 당첨번호에 따라 순위를 구하는 프로그램
# 5000원치 로또번호 생성.

import random as rnd
from chapter_04.exam01 import bubble_sort

def lotto_generator():
    lotto_num = set()

    while len(lotto_num) < 6:
        lotto_num.add(rnd.randint(1, 46))
    return lotto_num


if __name__ == "__main__":
    rnd.seed(4)


    # for num in range(0, 10):
    #     random_list.append(rnd.randint(1, 46))
    set_lotto = list(lotto_generator())
    print('로또번호 : {}'.format(bubble_sort(set_lotto)))#정렬된결과


