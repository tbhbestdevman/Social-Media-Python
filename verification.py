```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from database import database_connection
from user import UserSchema

def verify_email(user_id):
    user = UserSchema.query.get(user_id)
    if not user:
        return {"error": "User not found"}

    msg = MIMEMultipart()
    msg['From'] = 'no-reply@our-social-media.com'
    msg['To'] = user.email
    msg['Subject'] = 'Email Verification'

    body = f"""
    Hi {user.username},

    Please click the link below to verify your email address:

    http://our-social-media.com/verify/{user.verification_token}

    If you did not request this, please ignore this email.

    Regards,
    Our Social Media Team
    """

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('no-reply@our-social-media.com', 'password')
    text = msg.as_string()
    server.sendmail('no-reply@our-social-media.com', user.email, text)
    server.quit()

    return {"message": "Verification email sent"}

def confirm_verification(token):
    user = UserSchema.query.filter_by(verification_token=token).first()
    if not user:
        return {"error": "Invalid verification token"}

    user.is_verified = True
    database_connection.session.commit()

    return {"message": "Email verified successfully"}
```