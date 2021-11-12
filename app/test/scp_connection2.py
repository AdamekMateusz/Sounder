
import paramiko
import sys
from scp import SCPClient, SCPException

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

ssh = createSSHClient('192.168.1.4', 22, 'pi', 'musztarda41')


# Define progress callback that prints the current percentage completed for the file
def progress(filename, size, sent):
    sys.stdout.write("%s's progress: %.2f%%   \r" % (filename, float(sent)/float(size)*100) )

# SCPCLient takes a paramiko transport and progress callback as its arguments.
#scp = SCPClient(ssh.get_transport(), progress=progress)

# you can also use progress4, which adds a 4th parameter to track IP and port
# useful with multiple threads to track source
def progress4(filename, size, sent, peername):
    #sys.stdout.write("(%s:%s) %s's progress: %.2f%%   \r" % (peername[0], peername[1], filename, float(sent)/float(size)*100) )
    print(float(sent)/float(size)*100)
#scp = SCPClient(ssh.get_transport(), progress4=progress4)
scp = SCPClient(ssh.get_transport(), progress4=progress4)
scp.put("/home/mateusz/2021_03_02_11_16_35.mkv")
# Should now be printing the current progress of your put function.

scp.close()