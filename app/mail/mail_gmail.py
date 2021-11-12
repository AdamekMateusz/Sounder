from mailer import Mailer

mail = Mailer(email='sounder.support', password='Inzynierka178@')
mail.send(receiver='mateusz20.08.1999@gmail.com', subject='TEST', message='From Python!')
