from flask import Flask, render_template, redirect, session, url_for, request
from flaskext.mysql import MySQL
import yaml
import os

app = Flask(__name__)

app.secret_key = os.urandom(16)


#mysql configuration
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_DATABASE_HOST'] = db['mysql_host']
app.config['MYSQL_DATABASE_USER'] = db['mysql_user']
app.config['MYSQL_DATABASE_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DATABASE_DB'] = db['mysql_db']

# init app
mysql = MySQL()
mysql.init_app(app)

# function to que mysql cursor
def get_cursor():
    cursor = mysql.get_db().cursor()
    return cursor

@app.route('/', methods=['POST','GET'])
def visitorRegister():
    cur = get_cursor()
    if request.method == 'POST' and 'name' in request.form  and 'address' in request.form \
    and  'city' in request.form and 'password' in request.form:
        name = request.form['name']
        address = request.form['address'] + request.form['city']
        password = request.form['password']
        cur.execute('INSERT INTO Visitor (visitor_name,address,password) \
                VALUES (%s,%s,%s)' , (name, address,password))
        mysql.get_db().commit()
        cur.close()
        return redirect(url_for('scanQR'))
    else:
        return render_template('index.html')

@app.route('/agent-signin', methods=['POST', 'GET'])
def agentSignin():
    error = None
    cur = get_cursor()
    if request.method == 'POST' and 'username' in request.form  and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cur.execute("SELECT * FROM Agent A WHERE A.username = %s AND A.password = %s", (username, password))
        account = cur.fetchone()
        if account:
            session['loggedin'] = True
            session['username'] = username
            session['agent_id'] = account[0]
            cur.close()
            return redirect(url_for('agent_tools'))
        else:
            error = 'Error occured'
            return render_template('agent_signin.html', error=error)

    else:
        return render_template('agent_signin.html')

@app.route('/hospital-signin', methods=['POST', 'GET'])
def hospitalSignin():
    error = None
    cur = get_cursor()
    if request.method == 'POST' and 'username' in request.form  and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cur.execute("SELECT * FROM Hospital A WHERE A.username = %s AND A.password = %s", (username, password))
        account = cur.fetchone()
        if account:
            session['loggedin'] = True
            session['username'] = username
            session['hospital_id'] = account[0]
            cur.close()
            return redirect(url_for('hospital_tools'))
        else:
            error = 'Error occured'
            return render_template('hospital_signin.html', error=error)

    else:
        return render_template('hospital_signin.html')

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

@app.route('/hospital_tools',methods=['POST','GET'])
def hospital_tools():
    cur = get_cursor()
    cur.execute('SELECT citizen_id, visitor_name FROM Visitor WHERE infected')
    infected_people = cur.fetchall()
    # Struggling to figure out the query for places with infected visitors
    cur.execute('SELECT place_id, place_name FROM Places')
    infected_places = cur.fetchall()
    return render_template('hospital_tools.html', infected_people = infected_people, infected_places = infected_places)


if __name__ == "__main__":
    app.run(debug = True)
