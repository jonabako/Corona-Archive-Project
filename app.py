from flask import Flask, render_template, redirect, session, url_for, request
from flaskext.mysql import MySQL
import yaml
from flask_selfdoc import Autodoc
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
auto = Autodoc(app)

# function to que mysql cursor
def get_cursor():
    cursor = mysql.get_db().cursor()
    return cursor


#homepage render 
@app.route('/')
@auto.doc()
def index():
    return render_template('index.html')

# visitor registration page
@app.route('/visitor-registration', methods=['POST','GET'])
@auto.doc()
def visitorRegister():
    """Landing page, registration page for visitors.
    Form Data: 
        name: name of visitor
        password: password of visitor
        address: address of visitor
        city: city of visitor
    All fields are required.
    """
    cur = get_cursor()
    if request.method == 'POST' and 'fname' in request.form and 'lname' in request.form and 'address' in request.form \
    and 'city' in request.form and 'email' in request.form and 'phone' in request.form:
        name = request.form['fname'] + " " + request.form['lname']
        address = request.form['address'] + ", " + request.form['city']
        email = request.form['email']
        phone = request.form['phone']
        cur.execute('INSERT INTO Visitor (visitor_name,address,email,phone_number) \
                VALUES (%s,%s,%s,%s)' , (name, address, email, phone))
        mysql.get_db().commit()
        cur.close()
        return redirect(url_for('visitorHomepage'))
    else:
        return render_template('visitor_registration.html')

# place registration page
@app.route('/place-registration', methods=['POST','GET'])
@auto.doc()
def placeRegister():
    """Landing page, registration page for visitors.
    Form Data: 
        name: name of visitor
        password: password of visitor
        address: address of visitor
        city: city of visitor
    All fields are required.
    """
    cur = get_cursor()
    if request.method == 'POST' and 'name' in request.form and 'address' in request.form \
    and 'city' in request.form and 'email' in request.form and 'phone' in request.form:
        name = request.form['name']
        address = request.form['address'] + ", " + request.form['city']
        email = request.form['email']
        phone = request.form['phone']
        cur.execute('INSERT INTO Places (place_name,address,email,phone_number) \
                VALUES (%s,%s,%s,%s)' , (name, address, email, phone))
        mysql.get_db().commit()
        cur.close()
        return redirect(url_for('placeHomepage'))
    else:
        return render_template('place_registration.html')

# agent sign in page
@app.route('/agent-signin', methods=['POST', 'GET'])
@auto.doc()
def agentSignin():
    """login page for agents.
    Form Data: 
        username: username of agent
        password: password of agent
    All fields are required.
    Must be a correct combination in the database
    """
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

#hospital sign in page
@app.route('/hospital-signin', methods=['POST', 'GET'])
@auto.doc()
def hospitalSignin():
    """login page for hospital.
    Form Data: 
        username: username of hospital
        password: password of hospital
    All fields are required.
    Must be a correct combination in the database
    """
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

# visitor homepage
@app.route('/visitor-homepage')
@auto.doc()
def visitorHomepage():
    return render_template('visitor_homepage.html')

# place homepage
@app.route('/place-homepage')
@auto.doc()
def placeHomepage():
    return render_template('place_homepage.html')

# impressum page
@app.route('/impressum',methods=['POST','GET'])
@auto.doc()
def impressum():
    return render_template('imprint.html')

# agent tools page
@app.route('/agent_tools', methods=['POST','GET'])
@auto.doc()
def agent_tools():
    """agent tools page.
    Implementation pending
    """
    cur = get_cursor()
    cur.execute('SELECT citizen_id, visitor_name FROM Visitor WHERE infected')
    infected_people = cur.fetchall()
    # Struggling to figure out the query for places with infected visitors
    # TO DO
    cur.execute('SELECT place_id, place_name FROM Places')
    infected_places = cur.fetchall()
    return render_template('agent_tools.html',
        infected_people = infected_people, infected_places = infected_places)

#hospital tools page
@app.route('/hospital_tools',methods=['POST','GET'])
@auto.doc()
def hospital_tools():
    """hospital tools page.
    Implementation pending
    """
    cur = get_cursor()
    cur.execute('SELECT citizen_id, visitor_name FROM Visitor WHERE infected')
    infected_people = cur.fetchall()
    # Struggling to figure out the query for places with infected visitors
    cur.execute('SELECT place_id, place_name FROM Places')
    infected_places = cur.fetchall()
    return render_template('hospital_tools.html', infected_people = infected_people, infected_places = infected_places)

# Add /docs at the end of the standard link for the documentation
@app.route('/docs')
def docs():
    return auto.html(title='Corona Center API Docs')


if __name__ == "__main__":
    app.run(debug = True)
