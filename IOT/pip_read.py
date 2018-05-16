import cv2
import subprocess as sp
import numpy

FFMPEG_BIN = "ffmpeg"
command = [ FFMPEG_BIN,
        '-i', 'fifo264',             # fifo is the named pipe
        '-pix_fmt', 'bgr24',      # opencv requires bgr24 pixel format.
        '-vcodec', 'rawvideo',
        '-an','-sn',              # we want to disable audio processing (there is no audio)
        '-f', 'image2pipe', '-']
pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)

detector=cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

# Id=input('enter your id')
Id = 1
sampleNum=0

while True:
    # Capture frame-by-frame
    raw_image = pipe.stdout.read(640*480*3)
    # transform the byte read into a numpy array
    image =  numpy.fromstring(raw_image, dtype='uint8')
    image = image.reshape((480,640,3))          # Notice how height is specified first and then width

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    # print("outside face")
    for (x,y,w,h) in faces:
        print("inside face")
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        #incrementing sample number
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        if(cv2.imwrite(r"./dataset/User."+str(Id) +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])):
            print('yo')

        cv2.imshow('frame',image)
        print ("here")
    #wait for 100 miliseconds
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif sampleNum>20:
        break
cam.release()
cv2.destroyAllWindows()


#     if image is not None:
#         cv2.imshow('Video', image)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     pipe.stdout.flush()
#
# cv2.destroyAllWindows()
