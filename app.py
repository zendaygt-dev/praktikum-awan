import os
import pymysql
from flask import Flask

app = Flask(__name__)

def get_conn():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "rootpass"),
        database=os.getenv("DB_NAME", "appdb"),
    )

@app.route('/')
def hello():
    return "Halo dari Flask + Docker + Jenkins!"

@app.route('/db')
def db_check():
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT NOW()")
        now = cur.fetchone()[0]
    conn.close()
    return f"Koneksi database OK. Waktu server DB: {now}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
