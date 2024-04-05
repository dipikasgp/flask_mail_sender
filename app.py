from config import app, mail
from flask_mail import Message


@app.route("/send_mail")
def index():
    mail_content = Message(
        'Testing Testing 1 2 3....',
        recipients=['XYZ@gmail.com','ABC@gmail.com'])
    mail_content.body = "This is a test"
    mail.send(mail_content)
    return "Mail has sent"


if __name__ == '__main__':
    app.run()