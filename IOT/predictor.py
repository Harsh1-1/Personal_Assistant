import cv2
import subprocess as sp
import numpy
import talkey
import os

tts = talkey.Talkey()

FFMPEG_BIN = "ffmpeg"
command = [ FFMPEG_BIN,
        '-i', 'fifo264',             # fifo is the named pipe
        '-pix_fmt', 'bgr24',      # opencv requires bgr24 pixel format.
        '-vcodec', 'rawvideo',
        '-an','-sn',              # we want to disable audio processing (there is no audio)
        '-f', 'image2pipe', '-']
pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)


Id=1
j = 0


recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('./trainner/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

flag = False
# cam = cv2.VideoCapture(0)
#font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
while True:
    # ret, im =cam.read()

    # Capture frame-by-frame
    raw_image = pipe.stdout.read(640*480*3)
    # transform the byte read into a numpy array
    image =  numpy.fromstring(raw_image, dtype='uint8')
    image = image.reshape((480,640,3))          # Notice how height is specified first and then width

    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    if(flag):
        break
    for(x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        print("Inside faces")
        j+=1
        if(j==50):
            Id="yash"
            print(Id)
            tts.say("Hello "+ Id + " How are you ?")
            flag = True
            break
        if(conf<50):
            if(Id==1):
                Id="yash"
                print(Id)
                tts.say("Hello "+ Id + " How are you ?")
                flag = True
                break
                # import win32com.client as wincl
                # speak = wincl.Dispatch("SAPI.SpVoice")
                # print(Id)
                # speak.Speak("Good morning "+Id+" "+" how Are you my freind")


            elif(Id==2):
                Id="Sam"
        else:
            Id="Unknown"
        # cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
    #cv2.imshow('im',im)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
# cam.release()
cv2.destroyAllWindows()

if(flag):
    tts.say("what's up ?")
    os.system("python3 mic_server.py")
else:
    tts.say("could not detect you")
