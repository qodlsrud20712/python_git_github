import json

python_dict = {
    '이름': '홍길동',
    '나이': 25,
    '거주지': '서울',
    '신체정보':{
        '키': 175,
        '몸무게': 71
    },
    '취미': [
        '등산',
        '자전거타기',
        '독서'
    ]
}

print(type(python_dict))

json_data = json.dumps(python_dict)

print(type(json_data))

json_data = json.dumps(python_dict, indent=3, sort_keys=True, ensure_ascii=False)
print(json_data)

json_dict = json.loads(json_data)
print(type(json_dict))

print(json_dict['신체정보']['몸무게'])


student = [
        {
            'no' : 1,
            "name" : "김승영",
            "score" : {'국어': 90, '영어' : 80, '수학': 70}
        },
        {
            'no' : 2,
            "name" : "지재삼",
            "score" : {'국어': 90, '영어': 80, '수학': 90}
        }
]

json_student = json.dumps((student))
print(type(json_student))

with open('json_text.txt', 'w', encoding='utf-8')as f:
    json.dump(json_student, f)

with open('json_text.txt', 'r', encoding='utf-8')as f:
    x=json.load(f)
    print(type(x), x)
students = json.loads(x)
print(type(students))

for std in students:
    print('{} {} #{} {} {}'.format(type(std['no']), type(std['name']), type(std['score']['국어']), type(std['score']['영어']),
                                   type(std['score']['수학'])))
    print(std['no'], std['name'], end=' ')
    total = sum([x for x in std['score'].values()])

    [print(score, end = ' ') for score in std['score'].values()]
    print(total, total//float(3))