from flask import Flask
from flask_mail import Mail
app = Flask(__name__)

app.config['MAIL_SERVER']="smtp.office365.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = "ABC@outlook.com"
app.config['MAIL_PASSWORD'] = "password"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = ('ABC', 'ABC@outlook.com')
app.config['MAIL_MAX_EMAILS'] = 20 #it can send 20 emails at once. then close the connection and run again
mail = Mail(app)