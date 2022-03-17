from ast import Return
from crypt import methods
from pdb import post_mortem
from flask import Flask, render_template, redirect, url_for, request
from flaskext.mysql import MySQL

import yaml
import os

app = Flask(__name__)

app.secret_key = os.urandom(16)


db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_DATABASE_HOST'] = db['mysql_host']
app.config['MYSQL_DATABASE_USER'] = db['mysql_user']
app.config['MYSQL_DATABASE_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DATABASE_DB'] = db['mysql_db']

mysql = MySQL()
mysql.init_app(app)

def get_cursor():
    cursor = mysql.get_db().cursor()
    return cursor

@app.route('/', methods=['POST','GET'])
def visitorRegister():
    print('here1')
    error = None
    cur = get_cursor()
    if request.method == 'POST' and 'name' in request.form  and 'address' in request.form and  'city' in request.form and 'password' in request.form:
        print('here2')
        citizenId = 1 #make dynamic
        name = request.form['name']
        address = request.form['address'] + request.form['city']
        phoneNumber = '12345678' #make dynamic
        email = 'user@gmail.com' #make dynamic
        device_id = '12345' #make dynamic
        password = request.form['password']
        infected = False
        cur.execute('INSERT INTO Visitor (citizen_id,visitor_name,address,phone_number,email,device_id,infected,password) \
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)' , 
                    (citizenId,name, address,phoneNumber,email, device_id,infected,password))
        mysql.get_db().commit()  
        cur.close()
        return redirect(url_for('scanQR'))
    else:
        print('here3')
        return render_template('index.html', error=error)

@app.route('/scanQR')
def scanQR():
    return render_template('scanQR.html')

@app.route('/impressum',methods=['POST','GET'])
def impressum():
    return render_template('imprint.html')

@app.route('/agent_tools',methods=['POST','GET'])
def agent_tools():
    cur = get_cursor()
    cur.execute('SELECT citizen_id, visitor_name FROM Visitor WHERE infected')
    infected_people = cur.fetchall()
    # Struggling to figure out the query for places with infected visitors
    cur.execute('SELECT place_id, place_name FROM Places')
    infected_places = cur.fetchall()
    return render_template('agent_tools.html', infected_people = infected_people, infected_places = infected_places)


if __name__ == "__main__":
    app.run(debug = True)