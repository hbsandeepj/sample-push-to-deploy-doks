import os
from flask import Flask, jsonify
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
app.config['MYSQL_PORT'] = int(os.environ.get('MYSQL_PORT'))

mysql = MySQL(app)

@app.route("/")
def hello():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM auth_user LIMIT 5;")
    columns = [col[0] for col in cursor.description]
    result = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, use_reloader=True)