import talkey
import time
tts = talkey.Talkey()
tts.say(time.strftime("%I %M %p on %A, %B %e, %Y"))
