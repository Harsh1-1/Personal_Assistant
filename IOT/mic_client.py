# import socket
import android
# host = '192.168.32.150'
# port = 12345
# s = socket.socket()
# s.connect((host,port))
droid = android.Android()
(ids, result, error) = droid.recognizeSpeech()
print(result)
# inp = result.encode()
# #inp = raw_input()
# s.sendall(inp)
# s.close()
