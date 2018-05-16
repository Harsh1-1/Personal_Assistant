#!/usr/bin/python3           # This is server.py file
import socket
import talkey
import os
commands = ["turn on lights", "time", "dummy","get deadlines","send email","news","read emails","weather","hello","play","hi"]

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)

port = 4422

# bind to the port
serversocket.bind(('192.168.43.29', port))

# queue up to 5 requests
serversocket.listen(5)
print("server is listening...")
while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()
   flag = False

   print("Got a connection from %s" % str(addr))
   print("Listening commands...")
   # msg = 'Thank you for connecting'+ "\r\n"
   msg = clientsocket.recv(1024)
   print(msg.decode())
   clientsocket.close()
   if(len(msg) <= 0):
	   tts = talkey.Talkey()
	   tts.say('Sorry could not understand your message')
   else:
	   for command in commands:
		   if(command in msg.decode()):
			   flag = True
			   break
	   if(flag):
		   tts = talkey.Talkey()
		#    tts.say('Executing command captain')
		   if( commands.index(command) == 9 ):
			   os.system("python ./scripts/" + str(commands.index(command)) +  ".py " + msg.decode())
		   elif( commands.index(command) == 7 ):
			   os.system("python3 ./scripts/" + str(commands.index(command)) +  ".py " + msg.decode())
		   else:
			   os.system("python ./scripts/" + str(commands.index(command)) +  ".py")

	   else:
		   tts = talkey.Talkey()
		   tts.say('Invalid command')
