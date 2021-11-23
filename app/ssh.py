import paramiko
from scp import SCPClient, SCPException
import sys
from paramiko import SSHClient, AutoAddPolicy, RSAKey
from tkinter import *



class SSH():
    def __init__(self,host="192.168.1.4",port=22,username='pi',password='musztarda41',):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.progress:float

#command1 ='cd ~/app |ls'
#command2 ='ls'
    # def connect(self):
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     ssh.connect(self.host, self.port, self.username, self.password)
    #     return ssh

# stdin, stdout, stderr = ssh.exec_command(command1)
# print(stdout.readlines())
#     def get_progress(self):
#         print(self.progress_value)
    def connect(self):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.host, self.port, self.username, self.password)
        return client

    def scp_client(self,ssh_session):
        return SCPClient(ssh_session.get_transport(), progress4=self.progress4)

    def progress(filename, size, sent):
        sys.stdout.write("%s's progress: %.2f%%   \r" % (filename, float(sent) / float(size) * 100))
        return float(sent) / float(size) * 100

    def progress4(self,filename, size, sent, peername):
        sys.stdout.write("(%s:%s) %s's progress: %.2f%%   \r" % (peername[0], peername[1], filename, float(sent)/float(size)*100) )
        #self.progress_value = float(sent) / float(size) * 100











