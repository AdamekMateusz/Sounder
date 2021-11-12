from tkinter import *
from tkinter.ttk import *
from ssh import *

import paramiko
from scp import SCPClient, SCPException
import sys
from paramiko import SSHClient, AutoAddPolicy, RSAKey

class SSH():
    def __init__(self,host="192.168.1.4",port=22,username='pi',password='musztarda41'):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

#command1 ='cd ~/app |ls'
#command2 ='ls'
    # def connect(self):
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     ssh.connect(self.host, self.port, self.username, self.password)
    #     return ssh

# stdin, stdout, stderr = ssh.exec_command(command1)
# print(stdout.readlines())

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
        return float(sent) / float(size) * 100



root = Tk()

progress = Progressbar(root, orient=HORIZONTAL,
                       length=100, mode='indeterminate')

ssh = SSH()
ssh_session = ssh.connect()
scp = ssh.scp_client(ssh_session)
scp.put("/home/mateusz/2021_03_02_11_16_35.mkv")
# Should now be printing the current progress of your put function.

scp.close()

# Function responsible for the updation
# of the progress bar value
def bar():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 50
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 100
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 50
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 20
    root.update_idletasks()
    time.sleep(0.5)
    progress['value'] = 0


progress.pack(pady=10)

# This button will initialize
# the progress bar
Button(root, text='Start', command=bar).pack(pady=10)

# infinite loop
mainloop()