from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'postgres-service'),
        database=os.environ.get('DB_NAME', 'myapp'),
        user=os.environ.get('DB_USER', 'admin'),
        password=os.environ.get('DB_PASSWORD', 'password')
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS visits (id serial PRIMARY KEY, time timestamp DEFAULT CURRENT_TIMESTAMP);')
    cur.execute('INSERT INTO visits DEFAULT VALUES;')
    cur.execute('SELECT COUNT(*) FROM visits;')
    count = cur.fetchone()[0]
    cur.close()
    conn.commit()
    conn.close()
    return f"<h3>Application Flask + Postgres</h3><p>Nombre de visites : {count}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
