"""
#ineuron class assignments:
from urllib.request import urlopen
import re as r
import os

def shut_down():
    shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")

    if shutdown == 'no':
        exit()
    else:
        os.system("shutdown /s /t 1")


def getIP():
    d = str(urlopen('http://checkip.dyndns.com/')
            .read())
 
    return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
 
def length(s):
    c=0
    for i in s:
        c+=1
    return c


def index_find(l):
    z=length(l)
    for i in range(z):
        print(i,l[i])
def numeric_check(l):
    for i in l:
        if type(i)==int:
            print(i,end=" ")

s="ankennc"
print(length(s))
l=[1,2,5,11,7,9,"anuvab","chakraborty"]
index_find(l)
print(getIP())
#shut_down()
numeric_check(l)
"""
import smtplib , ssl
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "sskumar9876@gmail.com"  # Enter your address
receiver_email = "sudhanshu@ineuron.ai"  # Enter receiver address
#password = 'rlplfdcsoiqruagn'
password = 'fdafasfas'
message = """this is my message from python code """

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    
    
    
    
    =====================================================================
import smtplib
import time
import imaplib
import email
ORG_EMAIL = "@gmail.com" 
FROM_EMAIL = 'sskumar9876@gmail.com'
FROM_PWD = 'rlplfdcsoiqruagn'
SMTP_SERVER = "imap.gmail.com" 
SMTP_PORT = 993
imaplib._MAXLINE = 400000000

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')

    except Exception as e:
        traceback.print_exc() 
        print(str(e))

read_email_from_gmail()
