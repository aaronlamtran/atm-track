import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

DB_USER = os.getenv('DB_USER')


conn = psycopg2.connect(f"dbname=atm_track user={DB_USER}")
cur = conn.cursor()


def get_all():
    cur.execute('SELECT * FROM "TERMINAL_DATA"')
    records = cur.fetchall()
    # print(records)
    return records


def post_one(t_id, cash, days, last):
    cur.execute("""
  INSERT INTO "TERMINAL_DATA"
  ( "terminalID", "cashBalance", "daysUntilLoad", "lastTransaction")
  VALUES (%s, %s, %s, %s);
  """,
                (t_id, cash, days, last))
    conn.commit()
