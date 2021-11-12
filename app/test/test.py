from ssh import *

ssh = SSH()
session =ssh.connect()
stdin, stdout, stderr = session.exec_command('ls app')
print(stdout.readlines())

session.exec_command('mkdir -p slon')
stdin, stdout, stderr = session.exec_command('ls --width=1')
print(stdout.readlines())

#session.close()
stdin, stdout, stderr = session.exec_command("echo 'balwan")
print(stderr.readlines())