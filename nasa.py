import gspread
from pprint import pprint

GC = gspread.service_account(filename='creds1.json')
SH = GC.open('astronauts')
WSH = SH.sheet1


def szamolo(month):
    honap = []
    init = []
    for x in month:
        if x not in init:
            init.append(x)
            many = month.count(x)
            honap.append(many)
    print(honap)


def main():
    month = []
    date = WSH.col_values(5)
    del date[0]
    for x in date:
        if not x[1] == '/':
            month.append(x[:2])
        else:
            month.append(x[0])

    szamolo(month)

main()