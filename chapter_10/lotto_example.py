import random
from chapter_04.exam01 import bubble_sort


def lotto_generator():
    lotto_number = random.sample(range(1, 46), 6)
    return lotto_number


def lotto_buyer():
    lotto_buyer1, lotto_buyer2, lotto_buyer3, lotto_buyer4 = [], [], [], []
    all_lotto_num = [lotto_buyer1, lotto_buyer2, lotto_buyer3, lotto_buyer4]

    for i in range(len(all_lotto_num)):
        all_lotto_num[i] = random.sample(range(1, 46), 6)

    return all_lotto_num


def lotto_data(list, list2):
    a, b, c, cnt = 0, 0, 0, 0
    grade = []

    while b < len(list2):
        if b == len(list2) or a >= len(list):
            break
        if list[a] == list2[b][c]:
            cnt += 1
            if c < len(list) - 1:
                c += 1
            elif c == len(list)-1:
                print('{}번 구매자가 맞춘 로또번호는 {}입니다'.format(b, cnt))
                grade.append(cnt)
                a = 0
                b += 1
                cnt = 0
                c = 0

        elif a == len(list) - 1 and c == len(list) - 1:
            print('{}번 구매자가 맞춘 로또번호는 {}입니다'.format(b, cnt))
            grade.append(cnt)
            a = 0
            b += 1
            cnt = 0
        elif c == len(list) - 1:
            a += 1
            c = 0
        else:
            c += 1

    return grade


def buyer_grade(list):
    i = 0
    while 1:
        if i == len(list):
            break
        if list[i] == 6:
            print('{}번 구매자는 1등입니다.'.format(i))
            i+=1
        elif list[i] == 5:
            print('{}번 구매자는 2등입니다.'.format(i))
            i += 1
        elif list[i] == 4:
            print('{}번 구매자는 3등입니다.'.format(i))
            i += 1
        elif list[i] == 3:
            print('{}번 구매자는 4등입니다.'.format(i))
            i += 1
        else:
            print('{}번 구매자는 당첨되지않았습니다.'.format(i))
            i += 1


if __name__ == "__main__":
    lotto_num = lotto_generator()
    all_buyers = lotto_buyer()

    print('로또번호: {}'.format(bubble_sort(lotto_num)))
    print()
    print('========buyer========')
    [print(bubble_sort(all_buyers[i])) for i in range(len(all_buyers))]
    print('=====================')
    print()
    print('======lotto 맞춘 갯수======')
    grade_lotto_data = lotto_data(lotto_num, all_buyers)
    print('=========================')
    print()
    print('======lotto 당첨 여부======')
    lotto_buyer_grade = buyer_grade(grade_lotto_data)
    print('=========================')

