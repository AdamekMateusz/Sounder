import smtplib
from email.mime.text import MIMEText

title = 'My title'
msg_content = '<h2>{title} > <font color="green">OK</font></h2>\n'.format(title=title)
message = MIMEText(msg_content, 'html')

message['From'] = 'Sender Name <sounder.support@interia.pl>'
message['To'] = 'Receiver Name <mateusz20.08.1999@gmail.com>'
message['Cc'] = 'Receiver2 Name <jerzyadamek71@gmail.com>'
message['Subject'] = 'Any subject'

msg_full = message.as_string()

server = smtplib.SMTP('poczta.interia.pl:465')
server.starttls()
server.login('sender@server.com', 'Inzynierka178@')
server.sendmail('sender@server.com',
                ['receiver@server.com', 'receiver@server.com'],
                msg_full)
server.quit()
