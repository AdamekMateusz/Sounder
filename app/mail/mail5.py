import smtplib

def sendmail():
    subject = 'message subject'
    to = 'mateusz20.08.1999@gmail.com'
    sender = 'sounder.support@interia.pl'
    smtpserver = smtplib.SMTP("poczta.interia.pl",465)
    user = 'sounder.support@interia.pl'
    password = 'Inzynierka178@'
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(user, password)
    header = 'To:' + to + '\n' + 'From: ' + sender + '\n' + 'Subject:' + subject + '\n'
    message = header + '\n This is my message'
    smtpserver.sendmail(sender, to, message)
    smtpserver.close()

sendmail()