# SE-Sprint01-Team26

## Prerequisites
* [Mysql](https://dev.mysql.com/downloads/mysql/)
* Flask 
```
pip3 install Flask
```
* Virtual Env
```
sudo pip3 install virtualenv 
```

## Installation Guide
```bash
# Clone the repo and enter directory.
git clone https://github.com/Magrawal17/SE-Sprint01-Team26
cd SE-Sprint01-Team26

# Create virtual environment
$ virtualenv env

# Start virtual environment
$ source env/bin/activate

# Open  MySQL
$ mysql -u {ENTER YOUR USERNAME OR ROOT} -p

# Run this command in MYSQL command line to create required database.
mysql> source sql/tables.sql
mysql> exit

# Create db.yaml file 
$ touch db.yaml

# Open db.yaml and enter database credentials in the file format described below
$ nano db.yaml

# Run python server
$ python3 app.py

```


# Suggested changes to requirements document

* change entry_date and entry_time entries in VisitorToPlace table for single entry_timestamp entry.
* change exit_date and exit_time entries in VisitorToPlace table for single exit_timestamp entry.