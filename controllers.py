import psycopg2
import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PW = os.getenv('DB_PW')
DB_NAME = os.getenv('DB_NAME')
SEND_TO_EMAIL_ADDRESS = os.getenv('SEND_TO_EMAIL_ADDRESS')
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PW = os.getenv('EMAIL_PW')

print(f"dbname=atm_track user={DB_USER} password={DB_PW}")
conn = psycopg2.connect(f"host=localhost dbname={DB_NAME} user={DB_USER} password={DB_PW}")

def get_all():
    cur = conn.cursor()
    cur.execute('SELECT * FROM "TERMINAL_DATA"')
    records = cur.fetchall()
    # print(records)
    return records


def email_one(t_id, cash, days, last):
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = SEND_TO_EMAIL_ADDRESS
    message = f'{t_id}: last transaction {last}. days until reload: {days}. cash: {cash} '
    msg['Subject'] = f'Transaction {message}'
    msg.set_content(message)
    print(msg)
    server = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
    server.ehlo()
    server.login(EMAIL_ADDRESS, EMAIL_PW)
    server.send_message(msg)
    print('email sent')


def post_one(t_id, cash, days, last):
    # conn = psycopg2.connect(f"dbname=atm_track user={DB_USER}")
    cur = conn.cursor()
    cur.execute("""
  INSERT INTO "TERMINAL_DATA"
  ( "terminalID", "cashBalance", "daysUntilLoad", "lastTransaction")
  VALUES (%s, %s, %s, %s);
  """,
                (t_id, cash, days, last))
    conn.commit()

def email_reminder(ui_msg_txt):
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = SEND_TO_EMAIL_ADDRESS
    message = ui_msg_txt
    msg['Subject'] = f'REMINDER!'
    msg.set_content(message)
    print(msg)
    server = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
    server.ehlo()
    server.login(EMAIL_ADDRESS, EMAIL_PW)
    server.send_message(msg)
    print('email sent')


# if __name__ == '__main__':
#   get_all()
