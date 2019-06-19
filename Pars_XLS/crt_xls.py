import csv
from os import listdir
import xlwt

all=listdir("D:\\Data_Python\\fromload")
dat='20190326'
count=0

book=xlwt.Workbook('utf8')
sheet=book.add_sheet('sheetname')
font_base=xlwt.easyxf('font: height 240, name Arial, colour_index black, bold off,\
italic off; align: wrap on, vert top, horiz left; pattern: pattern solid,\
fore_colour white')
font_t=xlwt.easyxf('font: height 240, name Arial, colour_index black, bold on,\
italic off; align: wrap on, vert top, horiz left; pattern: pattern solid,\
fore_colour white')
stroka_xls=0
kolonka_xls=0

def file_to_mass(date):
    reader=csv.reader(open('D:\\Data_Python\\fromload\\'+date+'pat.csv'), delimiter=';')
    return list(reader)

def aver_sell():
    count=0
    n=0
    N_mon="none"
    N_year="none"
    for i in all:
        summ=0
        d=i[:len(i)-7]
        mon=i[4:len(i)-9]
        year=i[:len(i)-11]
        if N_year+N_mon!=year+mon:
            count=count+1
            print("Write change month in cell "+str(count))
            sheet.write(count,kolonka_xls+1,year+"."+mon,font_base)
        count=count+1
        for line in file_to_mass(d):
            if line[0]==None:
                break
            if line[0]=="activationDate":
                continue
            else:
                n=n+1
                summ=summ+int(line[3])

        print(str(n)+' '+str(i))
        if n!=0:
            sheet.write(count,kolonka_xls,d,font_base)
            sheet.write(count,kolonka_xls+1,n,font_base)
            sheet.write(count,kolonka_xls+2,int(summ),font_base)
            n=0
            book.save('D:\\Data_Python\\testXLS.xls')
        else:
            count=count-1
            continue
        N_mon=mon
        N_year=year

    return count

print(aver_sell())

book.save('D:\\Data_Python\\fromload\\PAT.xls')
