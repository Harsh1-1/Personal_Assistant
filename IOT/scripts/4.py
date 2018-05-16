import smtplib
import getpass
import talkey
import time
tts = talkey.Talkey()
def send_email(from_email,passw,to_email,msg):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(from_email,passw)
    server.sendmail(from_email,to_email,msg)
    server.quit()

tts.say("Please Enter your email")
time.sleep(1)
from_email = raw_input("Enter your email id:")
tts.say("Please Enter your password")
passw = getpass.getpass()
tts.say("Enter receiver's email id")
to_email = raw_input("Enter receiver email id:")
tts.say("Finally enter your message")
msg = raw_input("Enter your message:")
try:
    send_email(from_email,passw,to_email,msg)
    tts.say("Email sent successfully")
except:
    tts.say("Failed to send message, please give permissions")
