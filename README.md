## Achievements / Improvements

- [x] Created separate files inside sql folder, for database & table creation, and data population.

- [x] Fixed frontend inconsistencies (mentioned fixes i.e. positions of page elements, tables etc...).

- [x] Changed the footer of the Landing page (Contact us etc…) - too repetitive and space-consuming.

- [x] Replaced the navigation bar tabs with Corona Archive - redirecting to landing page, to avoid the repetition of User login/register redirects.

- [x] Simplified login proccess by avoiding redirecting page (after logging in, user had to click a link to get to their respective page.)

- [x] Solved bug upon successful Visitor Login - the scanning webcam opened separately as a python script which would never close.
 
- [x] Added timer feature after Visitor scans QR code until they press Leave Place.
 
- [x] Removed redudant feature in Hospital page - Search infected people in the main page not working (useless)

- [x] Implemented log out button for all users after successful log in.

- [x] Created my_validation.py that contains functions used for responsive input validation, (to avoid too much code in app.py)

- [x] Improved Automatic Generation and Download format of QR code.

- [x] Implemented function to remember the specific user and always redirect to their dashboard instead of the landing page.

- [x] Implemented a prototype for real-time input validation using Javascript.

- [x] Added frontend and backend testcases for sprint 4.

## Built with
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>Python</li>
  <li>Flask</li>
  <li>MySQL</li>
</ul>

## Prerequisites

### `Pip3`

- Linux
<p>If Python 3 has already been installed on the system, execute the command below to install pip3:</p>

```bash
$ sudo apt install python3-pip
```

- Windows
<p>Download <a href="https://bootstrap.pypa.io/get-pip.py">get-pip.py</a> to a folder on your computer.<br>
Navigate to the folder containing the get-pip.py installer and run the following command:</p>

```powershell
> python get-pip.py
```

### `Virtual Env`

- Linux
```bash
$ sudo pip3 install virtualenv
```
- Windows
```powershell
> python -m pip install virtualenv
```

### `MySQL`

- Linux
```bash
# install the mysql-server package
$ sudo apt install mysql-server
```

- Windows
```powershell
# install mysql with chocolatey
> choco install mysql
```

- Set MySQL root password
```mysql
# enter mysql command line
mysql -u root

# set password for root
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';
```

## `db.yaml` File Format

```yaml
mysql_host: "127.0.0.1"
mysql_user: "{YOUR USERNAME}"
mysql_password: "{YOUR PASSWORD}"
mysql_db: "corona_archive"
bcrypt_secret: "BAD_SECRET_KEY"
```

## Installation Guide
```
# Clone the repo and enter the directory
git clone https://github.com/jonabako/se-04-team-26
cd se-04-team-26
```

- Linux
```bash
# Create virtual environment
$ virtualenv env

# Start virtual environment
$ source env/bin/activate

# Install requirements.txt
$ pip3 install -r "requirements.txt"

# Create db.yaml file
$ touch db.yaml

# Open db.yaml and enter database credentials
$ nano db.yaml

# Login to MySQL
$ mysql -u {ROOT/YOUR PERSONAL USERNAME} -p

# Import Database, User and Table from createtables.sql
mysql> source sql/createtables.sql

# Populate database with data from insertdata.sql
mysql> source sql/insertdata.sql

# Leave mysql command prompt
mysql> exit

# Run python server
$ python3 app.py
```

- Windows
```powershell
# Create virtual environment
> virtualenv env

# Start virtual environment
> .\env\Scripts\activate

# Install requirements.txt
> pip install -r "requirements.txt"

# Create db.yaml file
> new-item db.yaml

# Open db.yaml and enter database credentials
> notepad.exe db.yaml

# Login to MySQL
> mysql -u {ROOT/YOUR PERSONAL USERNAME} -p

# Import Database, User and Table from createtables.sql
mysql> source sql/createtables.sql

# Populate database with data from insertdata.sql
mysql> source sql/insertdata.sql

# Leave mysql command prompt
mysql> exit

# Run python server
> flask run
```

### To run tests

- Linux
```
$ python3 test_group4.py
```

- Windows
```powershell
> python test_group4.py
```

### To see documentation

- Go to url
```
http://127.0.0.1:5000/docs
```
