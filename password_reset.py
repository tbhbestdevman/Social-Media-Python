```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from database import database_connection
from user import UserSchema

def reset_password(email):
    user = database_connection.query(UserSchema).filter(UserSchema.email == email).first()
    if user:
        new_password = generate_new_password()
        user.password = hash_password(new_password)
        database_connection.commit()
        send_reset_email(email, new_password)
        return True
    else:
        return False

def generate_new_password():
    import string
    import random
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(10))

def hash_password(password):
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()

def send_reset_email(email, new_password):
    msg = MIMEMultipart()
    msg['From'] = 'no-reply@socialmedia.com'
    msg['To'] = email
    msg['Subject'] = 'Password Reset'
    body = 'Your new password is: ' + new_password
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['From'], 'password')
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
```