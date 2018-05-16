import socket
import android
import sl4a
droid = sl4a.Android()
host = 'x.x.x.x'
port = 4422
while True:
    s = socket.socket()
    s.connect((host,port))
    droid = android.Android()
    (ids, result, error) = droid.recognizeSpeech()
    print(result)
    inp = "".encode()
    try:
        inp = result.encode()
    except:
        droid.ttsSpeak("Try again")

    s.sendall(inp)
    s.close()
    
