import socket
import os
from _thread import *
import socket
import threading, wave, pyaudio, time


ServerSocket = socket.socket()
host = '192.168.1.4'
port = 9633
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection,client_addr):
    connection.send(str.encode('Welcome to the Servern'))
    print('Connection test:', connection)
    BUFF_SIZE = 65536
    print('son')
    data = connection.recv(2048)
    track_name = data.decode('utf-8')

    CHUNK = 10*1024
    wf = wave.open(track_name)
    #wf = wave.open("T_Love_KING.wav")
    p = pyaudio.PyAudio()
    #print('server listening at',(host, (port)),wf.getframerate())
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    input=True,
                    frames_per_buffer=CHUNK)
    sample_rate = wf.getframerate()
    while True:


        data = wf.readframes(CHUNK)
        connection.sendto(data,client_addr)
        time.sleep(0.8*CHUNK/sample_rate)
        # data = connection.recv(2048)
        # reply = 'Server Says: ' + data.decode('utf-8')
        # if not data:
        #     break
        # connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client,address ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
