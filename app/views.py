from app import app, db
from app.form import Loginform, RegisterForm
from flask import request, render_template
from flask_bootstrap import Bootstrap

from models import Register

Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/contact', methods= ['GET', 'POST'])
def contact():
    form = Loginform()
    if request.method =='POST' and form.validate():
        user = Register.query.filter_by(username=form.username.data).first()
        if user:
            if user.password==form.password.data:
                return render_template('index.html')



    return render_template('contact.html', form=form)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post')
def post():
    return render_template('post.html')



@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = RegisterForm()
    if request.method=='POST':
        user = Register(username = form.username.data, password=form.password.data,
                        email = form.email.data,
                        surname = form.surname.data,
                        name=form.name.data,        MiddleName=form.MiddleName.data,
                        birthPlace=form.birthPlace.data,
                        passport=form.passport.data
                        )
        db.session.add(user)
        db.session.commit()
        return render_template('contact.html', form=form)
    return render_template('signup.html', form=form)