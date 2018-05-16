#!/usr/bin/env python
import sys
import imaplib
import getpass
import email
import email.header
import datetime
import talkey

EMAIL_ACCOUNT = "ykspcm@gmail.com"
EMAIL_FOLDER = "Top Secret/PRISM Documents"
tts = talkey.Talkey()

def process_mailbox(M,time_stamp):
    """
    Do something with emails messages in the folder.
    For the sake of this example, print some headers.
    """

    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        print "No messages found!"
        return

    for num in range(time_stamp-10,time_stamp):
        rv, data = M.fetch(str(num), '(RFC822)')
        if rv != 'OK':
            print "ERROR getting message", num
            return

        msg = email.message_from_string(data[0][1])
        decode = email.header.decode_header(msg['Subject'])[0]
        decode1 = email.header.decode_header(msg['from'])[0]
        try:
            subject = unicode(decode[0])
            email_from = unicode(decode1[0])
            print 'Message %s: %s' % (num, subject)
            if(num == (time_stamp-10)):
                tts.say(subject)
            print 'Raw Date:', msg['Date']
            print "FROM %s",(email_from)
            # Now convert to local date-time
            date_tuple = email.utils.parsedate_tz(msg['Date'])
            if date_tuple:
                local_date = datetime.datetime.fromtimestamp(
                    email.utils.mktime_tz(date_tuple))
                print "Local Date:", \
                    local_date.strftime("%a, %d %b %Y %H:%M:%S")
                print '\n\n\n'
        except:
            continue


M = imaplib.IMAP4_SSL('imap.gmail.com')

try:
    tts.say("Please enter password")
    rv, data = M.login(EMAIL_ACCOUNT, getpass.getpass())
except imaplib.IMAP4.error:
    tts.say("Login Failed bro")
    print "LOGIN FAILED!!! "
    sys.exit(1)

print rv, data

rv, mailboxes = M.list()
# if rv == 'OK':
#     print "Mailboxes:"
#     print mailboxes

rv, data = M.select("INBOX")
if rv == 'OK':
    print "Processing mailbox...\n"
    process_mailbox(M,int(data[0]))
    M.close()
else:
    print "ERROR: Unable to open mailbox ", rv

M.logout()
