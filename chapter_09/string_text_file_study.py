file = 'coffeeShopSales.txt'

with open(file, 'r')as f:
    line = f.readlines()
    for lines in line:
        print(lines, end=' ')

with open(file, 'r')as f:
    header = f.readline()
    print(header, header.split())
    headerList = header.split()
    #[print(lines.split())for lines in f]

    espresso = []
    americano = []
    cafelatte = []
    cappucino = []

    for line in f:
        dataList = line.split()

        espresso.append(int(dataList[1]))
        americano.append(int(dataList[2]))
        cafelatte.append(int(dataList[3]))
        cappucino.append(int(dataList[4]))

print('{}:{}'.format(headerList[1], espresso))
print('{}:{}'.format(headerList[2], americano))
print('{}:{}'.format(headerList[3], cafelatte))
print('{}:{}'.format(headerList[4], cappucino))

total_sum = [sum(espresso), sum(americano), sum(cafelatte), sum(cappucino)]
total_mean = [sum(espresso)/len(espresso), sum(americano)/len(americano),
              sum(cafelatte)/len(cafelatte), sum(cappucino)/len(cappucino)]

for k in range(len(total_sum)):
    print('[{}] 판매량'.format(headerList[k+1]))
    print('- 나흘 전체: {}, 하루 평균: {}'.format(total_sum[k], total_mean[k]))


#[{'날짜':'10.15' , '에스프레소' : '10', '아메리카노' : '50', '카페라테':'45', '카푸치노' : '20'}]
#이런식으로 해서 딕셔너리로 작성.