from ERP import app
from flask import render_template, redirect, url_for, flash, request
from ERP.models import User
from ERP.forms import RegisterForm, LoginForm, AdminLoginForm
from ERP import db, mail, s
from flask_login import login_user, logout_user, login_required, current_user
from itsdangerous import SignatureExpired
from flask_mail import Mail, Message
from flask_user import roles_required, UserManager


@app.route('/')
@app.route('/home')
def home_page():
    return  render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()

    if request.method == "GET":
        return render_template('login.html', form=form)

    if form.validate_on_submit():
    	attempted_user = User.query.filter_by(email_address=form.email_address.data).first()
    	if attempted_user and attempted_user.team == form.team.data and attempted_user.check_password_correction(attempted_password=form.password.data):
    		
            #Sales Team
            if attempted_user.team == 'sales':
                login_user(attempted_user)
                flash(f'Hi {attempted_user.fname}. Welcome to the Sales Dashboard', category='success')
                return redirect(url_for('sales_dashboard'))

            #Support Team
            if attempted_user.team == 'support':
                login_user(attempted_user)
                flash(f'Hi {attempted_user.fname}. Welcome to the Support Dashboard', category='success')
                return redirect(url_for('support_dashboard'))

            #Finance Team
            if attempted_user.team == 'finance':
                login_user(attempted_user)
                flash(f'Hi {attempted_user.fname}. Welcome to the Finance Dashboard', category='success')
                return redirect(url_for('finance_dashboard'))

            
    	else:
    		flash("Incorrect login credentials", category='danger')
    		return render_template('login.html', form=form)

    if form.errors != {}:
    	flash("Incorrect login credentials", category='danger')

    return render_template('login.html', form=form)


@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login_page():
    form = AdminLoginForm()

    if request.method == "GET":
        return render_template('admin_login.html', form=form)

    if form.validate_on_submit():
    	attempted_user = User.query.filter_by(email_address=form.email_address.data).first()
    	if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
    		login_user(attempted_user)
    		flash(f'Hi {attempted_user.fname}. Welcome to the Admin dashboard', category='success')
    		return redirect(url_for('admin_dashboard'))
    	else:
    		flash("Incorrect login credentials", category='danger')

    if form.errors != {}:
    	flash("Incorrect login credentials", category='danger')

    return render_template('admin_login.html', form=form)

    
@app.route('/admin_dashboard', methods=['GET', 'POST'])
@roles_required('Admin')
def admin_dashboard():
	return render_template('admin_dashboard.html')


@app.route('/sales_dashboard', methods=['GET', 'POST'])
@login_required
def sales_dashboard():
	return render_template('sales_dashboard.html')

@app.route('/support_dashboard', methods=['GET', 'POST'])
@login_required
def support_dashboard():
    return render_template('support_dashboard.html')

@app.route('/finance_dashboard', methods=['GET', 'POST'])
@login_required
def finance_dashboard():
    return render_template('finance_dashboard.html')


@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out', category='info')
    return redirect(url_for('home_page'))

@app.route('/admin_logout')
def admin_logout():
    logout_user()
    flash('You have been logged out', category='info')
    return redirect(url_for('admin_login_page'))

@app.route('/services')
def services_page():
    return render_template('services.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')