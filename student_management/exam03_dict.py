file = 'test.txt'

dict1 = {'학번':'01', '이름':'현아', '국어':'90', '영어':'88', '수학':'40', '총점':'218 ', '평균':'72'}

print(dict1)
print(type(dict1))

print(dict1.keys())
print(dict1.values())

with open(file, 'w')as f:

    f.writelines(list(dict1))