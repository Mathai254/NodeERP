from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, InputRequired, AnyOf
from ERP.models import User

class RegisterForm(FlaskForm):


    def validate_email_address(self, email_to_check):
        email_address = User.query.filter_by(email_address=email_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different Email Address')
    
    fname = StringField(label='First Name', validators=[Length(min=3, max=30), InputRequired()])
    lname = StringField(label='Last Name', validators=[Length(min=3, max=30), InputRequired()])
    email_address = StringField(label='Email Address', validators=[Email(), InputRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6, message='Password must be at least 6 characters long.'), InputRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[InputRequired(), EqualTo('password1', message='Passwords do not match')])
    submit = SubmitField(label='Register')



class LoginForm(FlaskForm):
    email_address = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    team = SelectField(u'Team', choices=[(None, 'Choose...'),('sales', 'Sales'), ('finance', 'Finance'), ('support', 'Support')],
        validators=[DataRequired(), AnyOf(values=('sales', 'finance', 'support'), message=u'Incorrect login credentials', values_formatter=None)])
    submit = SubmitField(label='Submit')

class AdminLoginForm(FlaskForm):
    email_address = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Submit')

