from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'bhn-prod-db-do-user-15790658-0.c.db.ondigitalocean.com'
app.config['MYSQL_USER'] = 'doadmin'
app.config['MYSQL_PASSWORD'] = 'AVNS_uS_AX6dwa30d0e1vpGW'
app.config['MYSQL_DB'] = 'braveheart_nation'
app.config['MYSQL_PORT'] = 25060

mysql = MySQL(app)

@app.route("/")
def hello():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM auth_user LIMIT 5;")
    columns = [col[0] for col in cursor.description]
    result = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    print("==============",result)
    html = """Hello {name}!
    Hostname: This is an automated message post production deployment!!"""
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, use_reloader=True)