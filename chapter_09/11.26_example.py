file = 'coffeeShopSales.txt'

with open(file, 'r')as f:
    dict1, dict2, dict3, dict4 = {}, {}, {}, {}
    all_dict, espresso, americano, cafelatte, cappucino, keys, dict_res, coffee_menu = [], [], [], [], [], [], [], []
    cnt, coffee = 0, 0
    coffee_menu_list = [espresso, americano, cafelatte, cappucino]

    header = f.readlines()
    [dict_res.append(header[i].split()) for i in range(len(header))]

    for i in range(len(header)):
        dict1.update({dict_res[0][i]: dict_res[1][i]})
        dict2.update({dict_res[0][i]:dict_res[2][i]})
        dict3.update({dict_res[0][i]: dict_res[3][i]})
        dict4.update({dict_res[0][i]: dict_res[4][i]})

    all_dict = [dict1, dict2, dict3, dict4]

    [print(all_dict[i]) for i in range(len(all_dict))]

    coffee_menu = list(all_dict[0].keys())

    while 1:
        if coffee == len(coffee_menu_list):
            break
        coffee_menu_list[coffee].append(int(all_dict[cnt][coffee_menu[coffee+1]]))
        cnt += 1
        if cnt >= len(all_dict):
            coffee += 1
            cnt = 0

    [keys.append(key) for key, value in all_dict[0].items()]

    total_sum = [sum(espresso), sum(americano), sum(cafelatte), sum(cappucino)]
    total_mean = [sum(espresso) / len(espresso), sum(americano) / len(americano),
                  sum(cafelatte) / len(cafelatte), sum(cappucino) / len(cappucino)]

    for k in range(len(total_sum)):
         print('[{}] 판매량'.format(keys[k+1]))
         print('- 나흘 전체: {}, 하루 평균: {}'.format(total_sum[k], total_mean[k]))
