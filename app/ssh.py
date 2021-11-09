import paramiko

class SSH():
    def __init__(self,host="192.168.1.4",port=22,username='pi',password='musztarda41'):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

#command1 ='cd ~/app |ls'
#command2 ='ls'
    def connect(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host, self.port, self.username, self.password)
        return ssh

# stdin, stdout, stderr = ssh.exec_command(command1)
# print(stdout.readlines())