from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)
mysql.connect()

def get_cursor():
    cursor = mysql.connection.cursor()
    return cursor

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/impressum')
def impressum():
    return render_template('imprint.html')

@app.route('/agent_tools')
def agent_tools():
    cur = get_cursor()
    cur.execute('SELECT visitor_id, visitor_name FROM Visitor WHERE infected')
    infected_people = cur.fetchall()
    # Struggling to figure out the query for places with infected visitors
    cur.execute('SELECT place_id, place_name FROM Places')
    infected_places = cur.fetchall()
    return render_template('agent_tools.html', infected_people = infected_people, infected_places = infected_places)


if __name__ == "__main__":
    app.run(debug = True)