def func3(list):
    i = 0
    while i < len(list):
        list[i] *= list[i]
        i += 1
    print(list)


def func4(list):
    i = 0
    while i < len(list):
        list[i] *= list[i]
        i += 1



if __name__ == "__main__":
    res = (lambda x: x ** 2)(3)
    print(res)

    mySquare = lambda x: x ** 2

    print(mySquare(9))

    scores = [90, 80, 95, 85]

    score_sum = 0
    subject_num = 0

    for score in scores:
        score_sum = score_sum + score
        subject_num = subject_num + 1

    average = score_sum / subject_num

    print('총점:{0}, 평균:{1}'.format(score_sum, average))

    print('총점2:{0}, 평균2:{1}'.format(sum(scores), sum(scores) / len(scores)))

    print('최하점수:{}, 최고점수:{}'.format(min(scores), max(scores)))

    list1 = [1, 2, 3, 4, 5]

    func3(list1)
