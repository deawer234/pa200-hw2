from flask import Flask, request, render_template
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(os.environ['DB_USER'], os.environ['DB_PASSWORD'], os.environ['DATABASE_URL'],os.environ['DB_PORT'], os.environ['DB_NAME'])
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS visits (count INT);')
    cur.execute('SELECT count FROM visits;')
    row = cur.fetchone()
    if row:
        count = row[0] + 1
        cur.execute('UPDATE visits SET count = %s;', (count,))
    else:
        count = 1
        cur.execute('INSERT INTO visits (count) VALUES (1);')
    conn.commit()
    cur.close()
    conn.close()
    return f'<h1>Visits: {count}</h1>'
