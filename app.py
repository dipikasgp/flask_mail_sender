from config import app, mail
from flask_mail import Message


@app.route("/send_mail")
def index():
    mail_content = Message(
        'Attachment',
        recipients=['XYZ@gmail.com','ABC@gmail.com'])
    mail_content.body = "This is a test"
    mail_content.html = '<b>Please see attached</b>'
    with app.open_resource('some_attachment.pdf') as pdf:
        mail_content.attach('some_attachment.pdf','application/pdf',pdf.read())
    mail.send(mail_content)
    return "Mail has sent"


@app.route('/bulk_mail')
def bulk_mail():
    users = [{'name':'ABC', 'mail': 'ABC@email.com'}]
    with mail.connect() as conn:
        for user in users:
            msg = Message('Bulk', recipients=[user['mail']])
            msg.body= f"Hey {user['name']}!"
            conn.send(msg)

if __name__ == '__main__':
    with app.app_context():
        index()
    app.run()