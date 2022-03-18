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
$ mysql -u {YOUR USERNAME OR ROOT} -p

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
### `db.yaml` file Format. Enter your respective credentials

We used a local environemnt to run flask project, as we couldn't figure out how to make flask work on clamv.

```yaml
mysql_host: "127.0.0.1"
mysql_user: "{YOUR USERNAME}"
mysql_password: "{YOUR PASSWORD}"
mysql_db: "seteam26"
```


# Suggested changes to requirements document

* change entry_date and entry_time entries in VisitorToPlace table for single entry_timestamp entry.
* change exit_date and exit_time entries in VisitorToPlace table for single exit_timestamp entry.
* add password field to the Visitor table.