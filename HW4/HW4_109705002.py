import csv
import json


def AVG(L):
    return sum([int(L[i]['成交金額'].replace(',', '')) for i in range(len(L))])/(len(L)), sum([int(L[i]['收盤價'].replace(',', '')) for i in range(len(L))])/(len(L))


path = 'STOCK_DAY_2330_202109.csv'
L = []
L2 = []
with open(path, encoding='UTF-8') as csv_file:
    rd = csv.reader(csv_file)
    rd = list(rd)
    for i in range(1, len(rd)):
        L.append({rd[0][0]: rd[i][0], rd[0][1]: rd[i][1], rd[0][2]: rd[i][2], rd[0][3]: rd[i][3], rd[0]
                 [4]: rd[i][4], rd[0][5]: rd[i][5], rd[0][6]: rd[i][6], rd[0][7]: rd[i][7], rd[0][8]: rd[i][8]})
totalTurnover, totalClosingprice = AVG(L)
print(f'平均成交金額 {totalTurnover}')
print(f'平均收盤價 {totalClosingprice}')
L2 = sorted(L, key=lambda x: x[rd[0][2]])
with open('L2.json', 'w', encoding='UTF-8') as jFile:
    json.dump(L2, jFile,  ensure_ascii=False)
