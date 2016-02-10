import smtplib
import getpass

print "------You need to allow less secured apps in your gmail security settings---------"
gmail_user = raw_input("Enter your email :")
gmail_pwd = getpass.getpass()
FROM = gmail_user
TO = raw_input("Enter receiver's email :")
SUBJECT = raw_input("Enter Subject :")
TEXT = raw_input("Enter message :")

# creating message 
message = "\r\n".join([
  "From:"+gmail_user,
  "To:"+TO,
  "Subject:"+SUBJECT,
  "",
  TEXT
  ])
try:
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	server.login(gmail_user, gmail_pwd)
	server.sendmail(FROM, TO, message)
	server.close()
	print 'successfully sent the mail'
except:
	print "failed to send mail"
	print "Please allow less secured apps from google security."
	print "If less secured apps are already allowed, then please check the password and try again."
