import psycopg2
import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
load_dotenv()

DB_USER = os.getenv('DB_USER')
SEND_TO_EMAIL_ADDRESS = os.getenv('SEND_TO_EMAIL_ADDRESS')
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PW = os.getenv('EMAIL_PW')

conn = psycopg2.connect(f"dbname=atm_track user={DB_USER}")
cur = conn.cursor()

msg = EmailMessage()
msg['From'] = EMAIL_ADDRESS
msg['To'] = SEND_TO_EMAIL_ADDRESS


def get_all():
    cur.execute('SELECT * FROM "TERMINAL_DATA"')
    records = cur.fetchall()
    # print(records)
    return records

def email(t_id, cash, days, last):
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
    cur.execute("""
  INSERT INTO "TERMINAL_DATA"
  ( "terminalID", "cashBalance", "daysUntilLoad", "lastTransaction")
  VALUES (%s, %s, %s, %s);
  """,
                (t_id, cash, days, last))
    conn.commit()



# if __name__ == '__main__':
#   email()