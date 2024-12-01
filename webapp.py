from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client.local
students = db.submission_list

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/submit')
def submit():
    return render_template("submit.html")

@app.route('/show')
def show():
    students_list = list(students.find())  
    return render_template("show.html", students=students_list)  

@app.route('/Add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form.get('Name')
        place = request.form.get('place')
        mail_id = request.form.get('Mail id')
        mobile = request.form.get('mobile')

        student_data = {
            "Name": name,
            "Place": place,
            "Mail id": mail_id,
            "Mobile": mobile
        }

        students.insert_one(student_data)

        return redirect(url_for('submit'))  

    return render_template('Add.html')

if __name__ == "__main__":
    app.run(debug=True)
