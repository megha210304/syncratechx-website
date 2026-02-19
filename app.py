from flask import Flask, render_template, request, flash, redirect, url_for
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'syncra_tech_x_secret_key_2026')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        if not name or not email or not message or '@' not in email:
            flash("Please provide a valid name, email, and message.", "error")
            return redirect(url_for('contact'))

        send_contact_email(name, email, message)
        flash(f"Thank you, {name}! Your message has been sent successfully.", "success")
        return redirect(url_for('contact'))
        
    return render_template('contact.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


def send_contact_email(name, email, message):
    smtp_server = os.environ.get('SMTP_SERVER')
    smtp_port = os.environ.get('SMTP_PORT')
    smtp_user = os.environ.get('SMTP_USER')
    smtp_password = os.environ.get('SMTP_PASSWORD')
    recipient = os.environ.get('CONTACT_RECIPIENT', 'hr@headsyncratechx.com')

    if not smtp_server or not smtp_port or not smtp_user or not smtp_password:
        return

    msg = EmailMessage()
    msg['Subject'] = f'New contact from {name}'
    msg['From'] = smtp_user
    msg['To'] = recipient
    body = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
    msg.set_content(body)

    with smtplib.SMTP_SSL(smtp_server, int(smtp_port)) as server:
        server.login(smtp_user, smtp_password)
        server.send_message(msg)

if __name__ == '__main__':
    app.run(debug=True)
