import socket
import threading, wave, pyaudio, time, queue,os
import sys

ClientSocket = socket.socket()
host = '192.168.1.4'
port = 9633

q = queue.Queue(maxsize=2000)


def audio_stream_UDP():
    BUFF_SIZE = 65536


    print('Waiting for connection')
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    #ClientSocket.send(str.encode(track_name),(host, port))

    p = pyaudio.PyAudio()
    CHUNK = 10 * 1024
    stream = p.open(format=p.get_format_from_width(2),
                    channels=2,
                    rate=44100,
                    output=True,
                    frames_per_buffer=CHUNK)

    # create socket
    # message = b'Hello'
    # ClientSocket.sendto(message, (host, port))
    #message = b'Golden_Life_Oprocz.wav'
    message = sys.argv[1]
    message = str.encode(message)
    ClientSocket.sendto(message, (host, port))

    socket_address = (host, port)

    def getAudioData():
        while True:
            frame, _ = ClientSocket.recvfrom(BUFF_SIZE)
            q.put(frame)
            print('Queue size...', q.qsize())


    t1 = threading.Thread(target=getAudioData, args=())
    t1.start()
    time.sleep(0.5)
    # print('Now Playing...')
    while True:
        frame = q.get()
        #print(q.get())
        stream.write(frame)
        # print(type(frame))
        # print('pingwin')
        # print(len(frame))
        # print('borsuk')
        # print(len(frame))
        if len(frame) == 0:
            break
        # if q.qsize() == 0:
        #     q.join()
        #     break
        # if q.qsize() == 0 and len(frame) < 1:
        #     #time.sleep(1)
        #     print('wielblad')
        #     print(len(frame))
        #     print('borsuk')
        #     print('krolik')
        #     print(q.qsize())
        #     print("zaba")
        #     break

            # break
            # print(frame)
            # print(len(frame))
            # if frame.decode('utf-8') == '':
            #     break
        #     print('slon')
        #     # t1.join()
        #     # print('True')
        #     # return True
        #     break

    ClientSocket.close()
    print('Audio closed')
    os._exit(1)


t1 = threading.Thread(target=audio_stream_UDP, args=())
t1.start()
