```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_verification_email(user_email, verification_code):
    # set up the SMTP server
    s = smtplib.SMTP(host='your_host_address', port=your_port)
    s.starttls()
    s.login('your_email_address', 'your_password')

    # create a message
    msg = MIMEMultipart()

    # setup the parameters of the message
    msg['From']='your_email_address'
    msg['To']=user_email
    msg['Subject']="Email Verification"

    # add in the message body
    message = f"Hello, \n\nPlease verify your email by entering the following code in the app: {verification_code}"
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server
    s.send_message(msg)

    del msg

    # Terminate the SMTP session and close the connection
    s.quit()

def verify_email(user_email, entered_code, actual_code):
    if entered_code == actual_code:
        # Update the user's status in the database
        database_connection.execute(f"UPDATE users SET verified = 1 WHERE email = '{user_email}'")
        return True
    else:
        return False
```