coffe = '  에스프레소 ,아메리카노, 카페라테, 카푸치노  '
p_num = '+82-01-2335-6789'
split_num = p_num.split('-', 1)

str_lr ='000Python is easy  to learn.000'

coffe_list = coffe.split(',')

cf_list = []
for coffe2 in coffe_list:
    temp = coffe2.strip()
    cf_list.append((temp))

name1 = 'ㅊㅅ'
name2 = 'ㅇㅁ'

hello = '님, 주소와 전화번호 입력바람'

address_list = ['서울시', '서초구', '반포', '201(반포동)']


if __name__ == '__main__':
    print(coffe.split(','))
    print(type(coffe.split(',')))

    print(coffe.split(maxsplit=2))
    print(split_num)
    print('국내전화번호:{}'.format(split_num[1]))
    print('aaaaPythonaaab'.strip('ab'))
    print(str_lr.strip('0'))
    print(str_lr.rstrip('0'))
    print(str_lr.lstrip('0'))
    print(coffe_list)

    print(cf_list)

    print(name1 + hello)
    print(name2 + hello)

    print(address_list)

    a =' '
    print(a.join(address_list))
    print(' '.join(address_list))

    str_f ='Python code.'

    print('찾는문자열의 위치:', str_f.find('Python'))
    print('찾는문자열의 위치:', str_f.find('code'))
    print('찾는문자열의 위치:', str_f.find('n'))
    print('찾는문자열의 위치:', str_f.find('easy'))

    str_f_se = 'Python is powerful. Python is easy to learn.'

    print(str_f_se.find('Python', 10, 30))
    print(str_f_se.find('Python', 35))

    str_c = 'Python is powerful. Python is easy to learn. Python is open'

    print('Python의 개수는?', str_c.count('Python'))

    print(str_f_se.replace('Python', 'IPython', 2))