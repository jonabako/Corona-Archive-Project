from flask import Flask, render_template, redirect, url_for , request

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/impressum')
def impressum():
    return render_template('imprint.html')

if __name__ == "__main__":
    app.run(debug = True)