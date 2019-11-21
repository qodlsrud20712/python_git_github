
def my_student_info_list(list):
    for key in range(len(list)):
        print('학생이름:{}'.format(list[key][0]))
        print('학급번호:{}'.format(list[key][1]))
        print('전화번호:{}'.format(list[key][2]))
        print()

    print('-------------------------------list done')


def my_student_info_tuple(tuple):
    for key in range(len(tuple)):
        print('학생이름:{}'.format(tuple[key][0]))
        print('학급번호:{}'.format(tuple[key][1]))
        print('전화번호:{}'.format(tuple[key][2]))
        print()

    print('-------------------------------tuple done')


def my_student_info_dict(dict):
    for key in dict.keys():
        print(key)
        print('학생이름:{}'.format(dict[key].get('학생이름')))
        print('학급번호:{}'.format(dict[key].get('학급번호')))
        print('전화번호:{}'.format(dict[key].get('전화번호')))
        print()
    print('-------------------------------dict done')


if __name__ == '__main__':
    std_list = [['현아', '01', '01-235-6789'], ['진수', '02', '01-987-6543']]
    my_student_info_list(std_list)

    std_tuple = (('현아', '01', '01-235-6789'), ('진수', '02', '01-987-6543'))
    my_student_info_tuple(std_tuple)

    std_dict = {'번호01' : {'학생이름' : '현아', '학급번호' :'01', '전화번호' :'01-235-6789'},
                '번호02' : {'학생이름' :'진수', '학급번호': '02', '전화번호' :'01-987-6543'}}
    my_student_info_dict(std_dict)

