from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import UserForm
from app.models import User

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, phonenumber=form.phonenumber.data,
        email=form.email.data, propertyaddress=form.propertyaddress.data, notes=form.notes.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for submitting your info!'.format(
            form.username.data
        ))
        return redirect(url_for('index'))
    return render_template('index.html',form=form)

@app.route('/about')
def about():
    return render_template('about.html')