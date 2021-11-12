from os import system
import paramiko
from paramiko import SSHClient, AutoAddPolicy, RSAKey

from scp import SCPClient, SCPException

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

ssh = createSSHClient('192.168.1.4', 22, 'pi', 'musztarda41')
scp = SCPClient(ssh.get_transport())

scp.put("/home/mateusz/dwhelper/ROCK/T_Love_KING.mp3")