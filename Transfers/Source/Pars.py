import xlwt

stroka_xls=-1
kolonka_xls=-1
end='**КОНЕЦ**'
num='Карта №'
no_find='данные о записанном ПБ отсутствуют'
file='m'
kol=0
kol_test=0
m=0
setting=open('D:\\Data_Python\\Transferes\\settings.ini')
setting_lines=setting.readlines()
class settings():
    def main_file():
        for s in setting_lines:
            if s=='PATH_MAIN\n':
                path=setting_lines[setting_lines.index(s)+ 1]
                return path[:len(path)-1]
    def xls():
        for s in setting_lines:
            if s=='PATH_XLS\n':
                path=setting_lines[setting_lines.index(s)+ 1]
                return path[:len(path)-1]


def valid_num(num):
    n=['0','1','2','3','4','5','6','7','8','9']
    for r in list(num):
        print (list(num))
        print(r)
        if r not in n:
            print(r)
            return "not valid"
    return 5
    print("valid")

def Del_Duplicate(mass):
    card_find=0
    card_del=0
    for line in mass:
        if num in line:
            i=mass.count(line)
            card_find=card_find+1
            if i!=1:
                card_del=card_del+1
                mass.remove(line)
                continue
    return mass

def Parsing(card, mass, xls):
    book=xlwt.Workbook('utf8')
    sheet=book.add_sheet('sheetname')
    font_base=xlwt.easyxf('font: height 240, name Arial, colour_index black, bold off,\
    italic off; align: wrap on, vert top, horiz left; pattern: pattern solid,\
    fore_colour white')
    font_t=xlwt.easyxf('font: height 240, name Arial, colour_index black, bold on,\
    italic off; align: wrap on, vert top, horiz left; pattern: pattern solid,\
    fore_colour white')
    m=0
    stroka_xls=-1
    kolonka_xls=-1
    while file=='m':
        card_num=num+card
        for line in mass:
            if card_num in line:
                ind=mass.index(line)
                for el in mass[ind::]:
                    if num in el:
                        m=m+1
                        stroka_xls=stroka_xls+1
                        t=mass.index(el)
                        for p in mass[t::]:
                            if no_find in p:
                                continue
                            elif not end in p:
                                kolonka_xls=kolonka_xls+1
                                sheet.write(stroka_xls,kolonka_xls,p,font_base)
                            else:
                                break
                        kolonka_xls=-1
                    if end in el:
                        continue
        book.save(settings.xls()+xls+'.xls')
        return str(m)
        m=0
        break
