        # SE-Sprint01-Team26

#### We ask the following be considered when grading:

- Only 9 days implementation time was given for first sprint
- Volen was lost in the organization of the project (didn't receive repository access until monday of the week of the deadline), since he wasn't properly registered in time. Some time was required to catch him up to the current status of the project.
- We developed on Ubuntu and MacOS, any package installed should also be available for windows as well. Check official documentation.

# Sprint Progress Team 1, Diego Zablah and Volen Yordanov

- Created project, included installation steps and prerequisite installation
- Setup database: created tables.sql document that contains required tables for project, as well as sample agent and hospital credentials
- Setup connection in app.py to the database
- Created landing page with registration for visitors, with working table data insertion
- Created hospital sign in page, with working static information from database
- Created agent sign in page, with working static information from database
- Styled the pages with custom css
- Implemented documentation in addition to comment the code
- Implemented tests for routes

# Suggested changes to requirements document

- change entry_date and entry_time entries in VisitorToPlace table for single entry_timestamp entry.
- change exit_date and exit_time entries in VisitorToPlace table for single exit_timestamp entry.
- add password field to the Visitor table.

## Prerequisites

- [Mysql](https://dev.mysql.com/downloads/mysql/)
- Flask

```
pip3 install Flask
```

- Virtual Env

```
sudo pip3 install virtualenv
```

- [Flask-MySql](https://flask-mysql.readthedocs.io/en/stable/)

## Installation Guide

```bash
# Clone the repo and cd into directory.
git clone https://github.com/Magrawal17/SE-Sprint01-Team26
cd SE-Sprint01-Team26

# Create virtual environment
$ virtualenv env

# Start virtual environment
$ source env/bin/activate

# Install requirements.txt
$ pip3 install -r "requirements.txt"

# Open  MySQL
$ mysql -u {YOUR USERNAME OR ROOT} -p

# Run this command in MYSQL command line to create required database.
mysql> source sql/tables.sql
mysql> exit

# Create db.yaml file
$ touch db.yaml

# Open db.yaml (with preffered text editor) and enter database credentials in the file format described below
$ nano db.yaml

# Run python server
$ python3 app.py

```

### `db.yaml` file Format. Enter your respective credentials

We used a local environment to run flask project, as we couldn't figure out how to make flask work on clamv.

```yaml
mysql_host: "127.0.0.1"
mysql_user: "{YOUR USERNAME}"
mysql_password: "{YOUR PASSWORD}"
mysql_db: "seteam26"
```

### To run tests

```
python3 tests/test.py
```

### To see documentation

```go to url
http://127.0.0.1:5000/docs
```

##### If issue with any package

Should and issue occur with any package, such that it is missing or the version is incorrect, try the following:

```
$ pip3 uninstall {name of package}
$ pip3 install {nameofpackage==version}
```

or alternatively

```
$ pip3 install -Iv {nameofpackage==version}
```

---

# Sprint Progress Team 2, Qais Qamhia and Vahid Nesro

## Achievements / Changes Implemented

- Created Landing Page, which was non-existent
- Implemented a hover option UI to give the website and extra punch. (Hover on the Homepage Bar to Ses)
- Improved Mis-matched forms (some had unnecesary input fields, others lacked fields such as password)
- Implemented Permanent Sessions to store each registered users data for 30 days -- this was neccesary as the project design does not save password
- Implemented custom animation on hero title
- Implemented QR Generation
- Restructured database according to project design -- fixing inconsistencies between SQL tables and project design (added fields to Visitors/Places and removed password from Visitors)
- Created Separte Registration pages for Visitor, Place, Hospital and Agency
- Implemented Logout buttons to clear registered user session
- Improved Commenting and Adding Much More of our own
- Improved Navbar UI to make it look more attractve and professional
- Redid Requirements.txt because it was not correct
- Improved Installation Steps -- previous one was not complete
- Automated MySQl user creation to simplify installation -- this was assumed in previous sprint which made installation a pain


## Prerequisites

- [Mysql](https://dev.mysql.com/downloads/mysql/)
- Flask

## Installation Guide for Linux

```bash
# Clone the repo and cd into directory.
git clone https://github.com/Magrawal17/SE-Sprint01-Team26
cd SE-Sprint01-Team26

# Create virtual environment
$ virtualenv env

# Start virtual environment
$ source env/bin/activate

# Install requirements.txt
$ pip3 install -r "requirements.txt"

# Login to MySQL
$ mysql -u {ROOT/YOUR PERSONAL USERNAME} -p

# Import Database, User and Table from tables.sql by running this command in MYSQL command line to create required database.
mysql> source sql/tables.sql
mysql> exit

# Run python server
$ python3 app.py
```
# Sprint Progress Team 3, Ilyas Benyamna and Ujjwal Khadka
- [x] Option to download the generated QR code
- [x] Ability to scan a QR code (pops up in another window) to check into a place and also check out. (see below for detailed instructions)
- [x] CSS improvements
- [x] Ability for Agent to view infected people dropdown and see their info along with which places they visited and at what time
- [x] Ability for Hospitals to mark visitors as infected
- [x] Ability for Hospital to see list of visitors (and search)
- [x] Ability for Agent to register hospitals
- [x] Ability for Agent to see the list of hospitals (and search)
- [x] Ability for Agent to see all visitors (and search)
- [x] Ability for Agent to see registered places (and search)
- [x] Testing (see test_group3.py)
- [x] added deployement procedure for windows, see below

- [] navigate to error page on getting error. for eg wrong email pass instead of displaying error in bottom

## Prerequisites

- [Mysql](https://dev.mysql.com/downloads/mysql/)
- Flask

## Installation Guide for Windows 
```powershell
# Clone the repo and cd into directory.
> git clone https://github.com/Magrawal17/SE-Sprint01-Team26
> cd SE-Sprint01-Team26

# Create virtual environment
> virtualenv env

# Start virtual environment
> .\env\Scripts\activate

# Install requirements.txt
> pip3 install -r "requirements.txt"

# Login to MySQL
> mysql -u {ROOT/YOUR PERSONAL USERNAME} -p

# Import Database, User and Table from tables.sql by running this command in MYSQL command line to create required database.
mysql> source sql\tables.sql
mysql> exit

# Run python server
> flask run
```

## QR code scanning intructions
### Step 1, generate a QR code on your phone
- On your phone, go to https://www.qr-code-generator.com or any other QR code generator
- as text, enter the following `test-qr-code` (case sensitive), there already exists an entry in the Place table which has the previous qr code.
- Click on GENERATE QR CODE
### Step 2, run the web app and register as a Visitor
- After registering, click on SCAN QR CODE
- a pop up window will appear, bring your phone with the previously generated QR code infront of the webcam and it should scan it.
- You should see `connected to: test place`
### Step 3, checking out
- Simply click on LOGOUT

---

# SE Sprint-04 Team-26

## Contributors
* Jona Bako
* Zineb Laouzi

## Sprint 4 - Achievements

- [x] ...

- [x] ...

- [x] ...

- [x] ...

- [x] ...

- [x] ...

- [x] ...

- [x] Added testcases for frontend and backend.

## Built with
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>Python</li>
  <li>MySQL</li>
</ul>

## Installation Guide for Linux / Ubuntu Subsystem for Windows
```
# Clone the repo.
git clone https://github.com/Magrawal17/se-04-team-26

```
