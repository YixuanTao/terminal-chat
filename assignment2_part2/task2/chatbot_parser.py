import os
from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host)
cursor = conn.cursor()

@app.route('/register', methods=['POST'])
def register():
    content = request.json
    command = content['command']
    server_url = content['server_url']
    cursor.execute("INSERT INTO commands (command, server_url) VALUES (%s, %s)", (command, server_url))
    conn.commit()
    return jsonify({'message': f'{command} is now registered to {server_url}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
