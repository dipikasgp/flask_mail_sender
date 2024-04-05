from flask import Flask
from flask_mail import Mail
app = Flask(__name__)

app.config['MAIL_SERVER']="smtp.office365.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = "ABC2@outlook.com"
app.config['MAIL_PASSWORD'] = "password"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = ('ABC', 'ABC@outlook.com')

mail = Mail(app)