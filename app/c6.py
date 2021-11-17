import socket
import threading, wave, pyaudio, time, queue

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

    p = pyaudio.PyAudio()
    CHUNK = 10 * 1024
    stream = p.open(format=p.get_format_from_width(2),
                    channels=2,
                    rate=44100,
                    output=True,
                    frames_per_buffer=CHUNK)

    # create socket
    message = b'Hello'
    ClientSocket.sendto(message, (host, port))
    socket_address = (host, port)

    def getAudioData():
        while True:
            frame, _ = ClientSocket.recvfrom(BUFF_SIZE)
            q.put(frame)
            print('Queue size...', q.qsize())

    t1 = threading.Thread(target=getAudioData, args=())
    t1.start()
    time.sleep(5)
    print('Now Playing...')
    while True:
        frame = q.get()
        stream.write(frame)

    ClientSocket.close()
    print('Audio closed')
    os._exit(1)


t1 = threading.Thread(target=audio_stream_UDP, args=())
t1.start()
