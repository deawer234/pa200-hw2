from flask import Flask, request, render_template
import psycopg
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg.connect(
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        host=os.environ['DATABASE_URL'], 
        port=os.environ['DB_PORT'],
        dbname=os.environ['DB_NAME']
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        msg = request.form.get('message', '').strip()
        if msg:
            cur.execute("INSERT INTO messages (content) VALUES (%s)", (msg,))
            conn.commit()

    cur.execute("SELECT content FROM messages ORDER BY id DESC")
    messages = cur.fetchall()
    cur.close()
    conn.close()

    return render_template_string('''
        <h1>Message Board</h1>
        <form method="post">
            <input name="message" required>
            <button type="submit">Send</button>
        </form>
        <ul>
        {% for msg in messages %}
            <li>{{ msg[0] }}</li>
        {% endfor %}
        </ul>
    ''', messages=messages)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)