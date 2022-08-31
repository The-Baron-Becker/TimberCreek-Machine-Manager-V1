from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from datetime import date
import psycopg2
#from waitress import serve


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://uajyocnbfrotvo:3178edc598ff2676d3e5be7681f44bccc3da83ae7f2c2f4762b5ca43e1c5c4da@ec2-44-210-36-247.compute-1.amazonaws.com:5432/deolrt4s7iaiq1"
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class machines(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, default = datetime.now().date())
    employee = db.Column(db.String(200), nullable = False)
    machine = db.Column(db.String(200), nullable = False)
    task = db.Column(db.String(200), nullable = False)
    note = db.Column(db.String(200), nullable = False)

    def __repr__(self):
        return '<Name %r>' % self.name

def __init__(self, date, employee, machine,task,note):
   self.date = date
   self.employee = employee
   self.machine = machine
   self.task = task
   self.note = note

@app.route('/')
def show_all():
   return render_template('show_all.html', machines = machines.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
        new_task = machines(employee = request.form.get('employee'), machine = request.form.get('machine'),
        task = request.form.get('task'), note = request.form.get('note'))
        
        db.session.add(new_task)
        db.session.commit()
        flash('Task was successfully added')
        return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all()   
   
   #serve(app, host="0.0.0.0", port=8080)
   #app.run(debug = True)

app.run()