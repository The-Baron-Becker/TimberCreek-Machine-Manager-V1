from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from datetime import date
import psycopg2
import os
from sqlalchemy import desc
import pandas as pd
from sqlalchemy import create_engine
#from waitress import serve


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://fmmyadnsacuxoi:a6c1b059a5e7aa869aba2ab8e8f8a61593afe930a852856a35a73f3ed64f81c0@ec2-44-207-133-100.compute-1.amazonaws.com:5432/d9gs2n7uf4cgu"
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class machines(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String, default = str(datetime.now().date()))
    employee = db.Column(db.String(200), nullable = False)
    machine = db.Column(db.String(200), nullable = False)
    task = db.Column(db.String(200), nullable = False)
    hours = db.Column(db.String)
    note = db.Column(db.String(200), nullable = False)

    def __repr__(self):
        return '<Name %r>' % self.name

def __init__(self, date, employee, machine, task, other, hours, note):
   self.date = date
   self.employee = employee
   self.machine = machine
   self.task = task
   self.other = other
   self.hours = hours
   self.note = note

@app.route('/')
def show_all():
   return render_template('show_all.html', machines = machines.query.all())

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if request.form['employee'] == "employee":
            flash('Please select employee id', 'error')

      else:

        new_task = machines(employee = request.form.get('employee'), machine = request.form.get('machine'),
        task = request.form.get('task')+request.form.get('other'), hours = request.form.get('hours'), note = request.form.get('note'))
        
        db.session.add(new_task)
        db.session.commit()
        flash('Task was successfully added')
        return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
