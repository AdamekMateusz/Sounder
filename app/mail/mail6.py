import imaplib
from email.message import Message
from time import time

connection = imaplib.IMAP4_SSL('poczta.interia.pl')
connection.login('sounder.support@interia.pl', 'Inzynierka178@')

new_message = Message()
new_message["From"] = "mateusz20.08.1999@gmail.com"
new_message["Subject"] = "My new mail."
new_message.set_payload("This is my message.")

connection.append('INBOX', '', imaplib.Time2Internaldate(time()), str(new_message).encode('utf-8'))