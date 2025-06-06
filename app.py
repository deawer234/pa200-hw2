from flask import Flask, request, render_template
from azure.identity import DefaultAzureCredential
import psycopg2

app = Flask(__name__)

def get_db_connection():
    credential = DefaultAzureCredential()
    accessToken = credential.get_token('https://ossrdbms-aad.database.windows.net/.default')
    
    conn = psycopg2.connect(
        host="pa200-postgresdb.postgres.database.azure.com",
        password=accessToken.token,
        user="aad_postgresflexible_xlqf6", 
        port="5432",
        database="postgres"
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL
        )
    ''')

    if request.method == 'POST':
        msg = request.form.get('message', '').strip()
        if msg:
            cur.execute("INSERT INTO messages (content) VALUES (%s)", (msg,))
            conn.commit()

    cur.execute("SELECT content FROM messages ORDER BY id DESC")
    messages = cur.fetchall()
    cur.close()
    conn.close()

    # Define external JavaScript URL for Azure Blob Storage
    # You'll need to update this URL when you upload your script to Azure
    azure_script_url = "https://pa200hw2xnemec11.blob.core.windows.net/scripts/message-board.js"
    
    return render_template('index.html', messages=messages, script_url=azure_script_url)
