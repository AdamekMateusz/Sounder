import paramiko
from scp import SCPClient, SCPException
import sys
from paramiko import SSHClient, AutoAddPolicy, RSAKey
from  threading import Thread
import time

class SSH():
    def __init__(self,host="192.168.1.4",port=22,username='pi',password='musztarda41'):
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
        #sys.stdout.write("(%s:%s) %s's progress: %.2f%%   \r" % (peername[0], peername[1], filename, float(sent)/float(size)*100) )
        self.progress = float(sent) / float(size) * 100
        return float(sent) / float(size) * 100


# def uploading(scp):
#     A = Thread(target=scp.put("/home/mateusz/2021_03_02_11_16_35.mkv", remote_path='/home/pi')).start()
#     time.sleep(1)
# def show_func():
#     while(1):
#         print('slon')
#         time.sleep(1)


if __name__ == "__main__":
    ssh = SSH()
    ssh_session = ssh.connect()
    scp = ssh.scp_client(ssh_session)
    scp.put("/home/mateusz/2021_03_02_11_16_35.mkv", remote_path='/home/pi')


    # upload = Thread(target=uploading(scp)).start()
    # pritner = Thread(target=show_func()).start()
    #
    # upload.join()
    # pritner.join()
    # Should now be printing the current progress of your put function.
    #print('slon')
    #print(scp.progress)
    scp.close()
