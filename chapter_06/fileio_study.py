try:
    f = open('/home/pjs/PycharmProjects/git_python_study/chapter_06/print_study.py', 'r')
    print(type(f))
    print(f)
    data = f.read()
    print(data)
except FileNotFoundError as e:
    print('해당파일 존재하지않음', e, sep='\n')
finally:
    print('finally-done')
    f.close()


try:
    f = open('/home/pjs/PycharmProjects/git_python_study/chapter_06/test.txt', 'x')
    f.write(data)
except FileExistsError as e:
    f = open('/home/pjs/PycharmProjects/git_python_study/chapter_06/test.txt', 'w')
    f.write(data)
    print('파일이 존재함', e , sep = '\n')
finally:
    print('finally-done')
    f.close()


print('done')