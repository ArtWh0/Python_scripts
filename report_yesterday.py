import datetime
import smtplib
from collections.abc import Iterable
import pymssql
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.header import Header

server = 'your server'
user = 'user'
password = 'password'
conn = pymssql.connect(server, user, password, 'bd_table')
cursor = conn.cursor()


def get_yesterday_date():
    now = datetime.datetime.now()
    yesterday = now - datetime.timedelta(days=1)
    return yesterday


def get_file_name():
    path = 'D:\\'
    date_for_filename = get_yesterday_date().strftime("%Y%m%d")
    company_name = 'pat'
    ext = '.csv'
    return path + date_for_filename + company_name + ext


cursor.execute(f"EXEC in your bd \'{get_yesterday_date().strftime('%Y.%m.%d %H:%M:%S')}\'")
row = cursor.fetchone()
with open(get_file_name(), 'w') as output_file:
    output_file.write("activationDate;UID;SAM;paymentInRubles\n")
    while row:
        output_file.write("%s;%s;%s;%s\n" % (row[0], row[1], row[2], row[3]))
        row = cursor.fetchone()
output_file.close()
conn.close()

email_user = 'example@mail.ru'
send_to = ['mail list to']
server = smtplib.SMTP('smtp_serv', 'port')

server.login('mail_user', 'mail_pass')

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = COMMASPACE.join(send_to)
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = Header('report ORGP ' + get_yesterday_date().strftime("%Y-%m-%d"), 'utf-8')

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
