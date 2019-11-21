file = 'two_times_table.txt'                #전역변수는 global로 받을 수 있따.


def file_write():
    global file
    f=open(file, 'w')
    for num in range(1, 6):
        format_string = '2x{0} = {1}\n'.format(num, 2*num)
        f.write(format_string)
    f.close()


def file_Readline_one(str):                         # try,except문 이용 예외처리한거
    try:
        with open(str, 'r')as f:
            line = f.readline()
            print(line, end='')
    except FileNotFoundError as e:
        print('해당파일 존재하지않음',e,sep='\n')

    print('Readline_one_done')


def file_Readline_while(str):
    f=open(str)
    line=f.readline()
    while line:
        print(line, end='')
        line = f.readline()
    f.close()

    print('Readline_done')

def file_Readline_all(str):
    f=open(str)
    lines=f.readlines()
    f.close()

    for line in lines:
        print(line, end='')

    print('Readline_all_done')

# 4개 함수 출력


if __name__ == '__main__':
    file = 'two_times_table.txt'
    file_write()
    file_Readline_one(file)
    file_Readline_while(file)
    file_Readline_all(file)