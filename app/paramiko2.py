import paramiko
from threading import Thread
import time

class Connection():
    def __init__(self,host = "192.168.1.56"):
        self.host = host
        self.username = 'pi'
        self.password = "musztarda41"


    def ssh_run_remote_command(self, cmd):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname=self.host,
                           username=self.username,
                           password=self.password)
        #ssh_client.exec_command('cd ~/app')
        stdin, stdout, stderr = self.ssh_client.exec_command(cmd)
        #ssh_client.exec_command(cmd)
        #x = Thread(target=ssh_client.exec_command(cmd))
        #x.start()
        #out = stdout.read().decode().strip()
        #error = stderr.read().decode().strip()
        # if self.log_level:
        #     logger.info(out)
        # if error:
        #     raise Exception('There was an error pulling the runtime: {}'.format(error))
        #ssh_client.close()

        #return out
    def exit_stream(self):
        self.ssh_client.exec_command('pkill -9 python3')
        self.ssh_client.close()

# conn = Connection(host='192.168.1.4')
# print(conn.ssh_run_remote_command('python3 ~/app/server2.py '))
