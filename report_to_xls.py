import pymssql
import datetime
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.header import Header
import xlsxwriter as xlsxwriter


def get_yesterday_date():
    now = datetime.datetime.now()
    yesterday = now - datetime.timedelta(days=1)
    return yesterday


def get_file_name():
    path = 'D:\\'
    date_for_filename = get_yesterday_date().strftime("%Y%m%d")
    ext = '.xlsx'
    return path + date_for_filename + ext


def create_file():
    workbook = xlsxwriter.Workbook(get_file_name())
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', '1')
    worksheet.write('B1', '2')
    worksheet.write('C1', '3')
    worksheet.write('D1', '4')
    worksheet.write('E1', '5')
    row_table = 1
    col_table = 0

    server = 'server_add'
    user = 'user'
    password = 'password'
    conn = pymssql.connect(server, user, password, 'bd_table')
    cursor = conn.cursor()

    cursor.execute("EXEC in your bd")
    row = cursor.fetchone()
    while row:
        worksheet.write(row_table, col_table, row[0])
        worksheet.write(row_table, col_table + 1, str(row[1]))
        worksheet.write(row_table, col_table + 2, row[2])
        worksheet.write(row_table, col_table + 3, row[3])
        worksheet.write(row_table, col_table + 4, row[4])
        row_table += 1
        row = cursor.fetchone()
    conn.close()
    workbook.close()


def send_mail():
    email_user = 'example@mail.ru'
    send_to = ['mail list to']
    server = smtplib.SMTP('smtp_serv', 'port')

    server.login('mail_user', 'mail_pass')

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = Header('activation devices ORGP ' + get_yesterday_date().strftime("%Y-%m-%d"), 'utf-8')

    msg.attach(MIMEText('This message is automatically generated.', 'plain', 'utf-8'))

    file_name = get_file_name()
    with open(file_name, "rb") as fil:
        part = MIMEApplication(
            fil.read(),
            Name=basename(file_name))

    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file_name)
    msg.attach(part)

    server.sendmail(email_user, send_to, msg.as_string())
    server.close()


create_file()
send_mail()
