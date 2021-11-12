import email, smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendMail():
    @staticmethod
    def send(receiver_email,hashcode):
        subject = "[BitFeel]Restore Password"
        body = f"""
You starting reseting your password,
Login using hashcode: {hashcode}, and go to the setting and change your password,
        
Never give anybody this hashcode, 
        
This is an email is autogeneration do not reply to this email """
        sender_email = "bitfeel.contact@gmail.com"
        #receiver_email = "sounder.support@interia.pl"
        #password = input("Type your password and press enter:")
        password = "Inzynierka178@"

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(body, "plain"))
        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)

import hashlib
class Md5():
    @staticmethod
    def md5sum_file(filepath):
        return hashlib.md5(open(filepath, 'rb').read()).hexdigest()
    @staticmethod
    def md5sum_string(str2hash):
        return hashlib.md5(str2hash.encode()).hexdigest()


