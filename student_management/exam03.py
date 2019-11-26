
#list, tuple, dictionary, set 중 하나를 선택하여 프로그램 작성
#student_management 패키지 추가
#1)1. 학생목록, 2.학생추가 3.학생수정, 4.학생삭제, 5.종료메뉴
#2)프로그램 수행 시 먼저 student_list.txt 파일을 읽어 수행
#3)각각 메뉴별 수행되도록 작성
#4)종료시 학생목록이 student_list.txt에 저장
#5)프린트하여 제출
#6)이왕이면 2개(dictionary + 재량)
# 학생 정보 : 학번, 학생명, 국어, 영어, 수학, 총점, 평균, 등수

file = 'student_list.txt'
share_list = []


def print_stu_list():
    global file
    global share_list
    with open(file, 'r+')as f:
        line = f.readlines()
        if share_list < line:
            share_list = line

        for i in share_list:
             print(i, '\n')

        print(type(share_list))


def add_stu_list():
     global file
     global share_list
     #global share_list
     with open(file, 'r')as f:
        line = f.readlines()
        if share_list < line:
            share_list = line
        print('학생정보를 입력하시오. 학번->이름->국어->영어->수학순으로')
        num, name, kor, eng, math = input().split()
        format_string = '{} '.format(int(kor) + int(eng) + int(math))
        format_string2 = '{}'.format((int(kor) + int(eng) + int(math)) // 3)
        share_list.append([num, name, kor, eng, math, format_string, format_string2])
        print(share_list, '\n')
        print('추가완료')


def fix_stu_list():
     global file
     global share_list
     with open(file, 'r+')as f:
        line = f.readlines()
        if share_list < line:
            share_list = line
        list_len = len(share_list)
        stu_list = range(list_len)
        print('수정할 학생정보를 고르시오')
        for i in stu_list:
            print(i,'번 ', end=' ')
        num = input()
        while num >= '0':
            print(num+'번 학생 정보 수정 1.학번 2.이름 3.국어성적 4.영어성적 5.수학성적')
            num2 = input()
            if num2 == '1':
                print('학번 수정:')
                share_list[int(num)][0] = input()
            elif num2 == '2':
                print('이름 수정:')
                share_list[int(num)][1] = input()
            elif num2 == '3':
                print('국어성적 수정:')
                share_list[int(num)][2] = input()
            elif num2 == '4':
                print('영어성적 수정:')
                share_list[int(num)][3] = input()
            elif num2 == '5':
                print('수학성적 수정:')
                share_list[int(num)][4] = input()
            share_list[int(num)][5] = '{} '.format(int(share_list[int(num)][2]) + int(share_list[int(num)][3]) + int(share_list[int(num)][4]))
            share_list[int(num)][6] = '{}'.format((int(share_list[int(num)][2]) + int(share_list[int(num)][3]) + int(share_list[int(num)][4])) // 3)
            break

        print('수정완료')

def del_stu_list():
    global file
    global share_list
    with open(file, 'r+')as f:
        line = f.readlines()
        if share_list < line:
            share_list = line
        list_len = len(share_list)
        stu_list = range(list_len)
        print('삭제 할 학생정보를 고르시오')
        for i in stu_list:
            print(i, '번 ', end=' ')
        num = input()
        while num >= '0':
            share_list.remove(share_list[int(num)])
            print(num+'번이 삭제되었습니다.')
            break


def exit_and_save(sep):
    global file
    with open(file, 'w')as f:
        vstr = ''
        for save in share_list:
            vstr = vstr+str(save)+sep
        vstr = vstr.rstrip(sep)
        f.writelines(vstr)



if __name__ == '__main__':
     while True:
         print('1)학생목록 2)학생추가 3)학생수정 4)학생삭제 5)종료')
         num = input()
         if num == '1':
             print_stu_list()
         elif num == '2':
             add_stu_list()
         elif num == '3':
             fix_stu_list()
         elif num == '4':
            del_stu_list()
         elif num == '5':
            exit_and_save('\n')
            print('저장 후 종료되었습니다.')
            break


