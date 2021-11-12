import smtplib, ssl

def read_creds():
    # user = passw = ""
    # with open("credentials.txt", "r") as f:
    #     file = f.readlines()
    #     user = file[0].strip()
    #     passw = file[1].strip()

    return 'bitfeel.contact@gmail.com', 'Inzynierka178@'


port = 465

sender, password = 'bitfeel.contact@gmail.com','Inzynierka178@'

recieve = "mateusz20.08.1999@gmail.com"

message = """\
Subject: Python Email Tutorial

This is from python!

Tech With Tim
"""

context = ssl.create_default_context()

print("Starting to send")
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, recieve, message)

print("sent email!")