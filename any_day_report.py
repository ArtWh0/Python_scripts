import datetime
import smtplib
from collections.abc import Iterable
import pymssql
from os.path import basename
from collections.abc import Iterable
from os import listdir
from os.path import isfile, join, basename

server = 'your server'
user = 'user'
password = 'password'
conn = pymssql.connect(server, user, password, 'bd_table')
cursor = conn.cursor()
dateFrom=datetime.datetime(2019,3,1)
dateTo=datetime.datetime(2019,5,31)

def get_file_name():
    path = 'D:\\Data_Python\\fromload\\'
    date_for_filename = dateFrom.strftime("%Y%m%d")
    company_name = 'pat'
    ext = '.csv'
    return path + date_for_filename + company_name + ext

while dateFrom!=dateTo:
    cursor.execute(f"EXEC dbo.patReport \'{dateFrom.strftime('%Y.%m.%d %H:%M:%S')}\'")
    row = cursor.fetchone()
    print("load for date "+dateFrom.strftime("%Y%m%d"))
    with open(get_file_name(), 'w') as output_file:
        print("open file "+get_file_name())
        output_file.write("activationDate;UID;SAM;paymentInRubles\n")
        print("start write file "+get_file_name())
        while row:
            print("write file "+get_file_name())
            output_file.write("%s;%s;%s;%s\n" % (row[0], row[1], row[2], row[3]))
            row = cursor.fetchone()
        print("file "+get_file_name()+" is writed")
    dateFrom = dateFrom + datetime.timedelta(days=1)
    print("date is change")
    output_file.close()
conn.close()
