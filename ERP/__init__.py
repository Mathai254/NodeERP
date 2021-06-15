from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///node.db'
app.config['SECRET_KEY'] = '5b8b56fa47332aac0de517db'
app.config['MAIL_SERVER']='corporate.vip5.noc401.com'
app.config['MAIL_USERNAME']='swambugu@akiki.co.ke'
app.config['MAIL_PASSWORD']=')_#Op_L{n1Dh'
app.config['MAIL_PORT']=465
app.config['MAIL_USE_SSL']=True
app.config['MAIL_USE_TLS']=False
app.config['USER_ENABLE_EMAIL'] = True
app.config['USER_EMAIL_SENDER_EMAIL'] = "noreply@example.com" 

s = URLSafeTimedSerializer('5b8b56fa47332aac0de517db')
mail = Mail(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"


from ERP import routes