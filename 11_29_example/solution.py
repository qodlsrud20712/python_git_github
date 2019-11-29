from chapter_04.exam01 import bubble_sort
import re
import operator

# 1번 문제

file = 'Gettysburg_Address.txt'

example_list, all_dict_list = [], []
list_variable,split_list, Len_list = [], [], []
dict1, dict2, dict3, dict4, dict5, empty_dict, all_dict = {}, {}, {}, {}, {}, {}, {}


with open(file, 'r')as f:
    cnt = 0
    k = 0
    line = f.readline()
    while line:
        example_list.append(line)
        line = f.readline()

    example_list.remove(example_list[0])

    for i in range(len(example_list)):
        example_list[i] = example_list[i].replace('-','')
        example_list[i] = example_list[i].replace(',','')
        example_list[i] = example_list[i].replace('.','')
        list_variable.append(example_list[i])

    for i in range(len(example_list)):
        split_list.append(list_variable[i].split())

    for i in range(len(example_list)):
        Len_list.append(len(split_list[i]))

    all_dict_list = [dict1, dict2, dict3, dict4, dict5]

    while True:
        if k > len(example_list)-1:
            break
        for i in range(Len_list[k]):
            if cnt > 2:
                empty_dict = {x: cnt}
                all_dict_list[k].update(empty_dict)
                cnt = 0
            else:
                cnt = 0
            for j in range(Len_list[k]):
                if split_list[k][i] == split_list[k][j]:
                    x = split_list[k][i]
                    cnt += 1
            if i == len(split_list[k])-1:
                k += 1

    for i in range(len(all_dict_list)):
        all_dict.update(all_dict_list[i])

    sdict = sorted(all_dict.items(), key=operator.itemgetter(1))

    print('=============1번문제=============')
    print('단어 별 빈도수 내림차순 정렬: ', sdict)
    print()

#2번문제
print('=============2번문제=============')
print('원하는 연산을 정한 후 값을 입력하시오.')
print('1번:더하기, 2번:빼기, 3번:곱하기, 4번:나누기')
z = input()

if z == '1':
   a, b = map(int, input().split())
   res = lambda a, b: a+b
   print('값:',res(a, b))
elif z == '2':
    a, b = map(int, input().split())
    res = lambda a, b: a - b
    print('값:',res(a, b))
elif z == '3':
    a, b = map(int, input().split())
    res = lambda a, b: a * b
    print('값:',res(a, b))
elif z == '4':
    a, b = map(int, input().split())
    res = lambda a, b: a // b
    print('값:',res(a, b))


#3번 문제
print()
print('=============3번문제=============')

n= 1

while 1:
    if n == 11:
        print('나무가 넘어갑니다.')
        break
    print('나무꾼이 나무를 {}번 찍습니다'.format(n))
    n +=1




#4번문제

def solution(array, commands):
    answer = []
    for a in range(len(commands)):
        i, j, k = commands_array[a][0], commands_array[a][1], \
              commands_array[a][2]
        b = bubble_sort(array[i:j])
        answer.append(b[k])

    return answer


array = [1,5,2,6,3,7,4]
commands_array = [[1,5,2], [3,4,0],[0,7,2]]
print()
print('=============4번문제=============')
print('solution 결과값:{}'.format(solution(array, commands_array)))

