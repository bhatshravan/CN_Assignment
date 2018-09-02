import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(user, pwd, recipient, subject, body):

	#try:
		#server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
		#server = smtplib.SMTP("smtp.gmail.com", 587)
		server = smtplib.SMTP("localhost",3333)
		server.ehlo()
		#server.starttls()
		#server.login(user, pwd)

		msg = MIMEMultipart()

		# setup the parameters of the message
		msg['From']="bhabha@shr.com"
		msg['To']=(recipient)
		msg['Subject']=subject
		msg['Body']=body
		msg.attach(MIMEText(body, 'plain'))

		# send the message via the server set up earlier.
		#server.send_message(msg)
		
		
		server.sendmail("rprustagi@local.com", recipient, msg.as_string())
		server.close()
		
		print("successfully sent the mail")
	#except Exception as e:
		#print("failed to send mail {0}".format(e))

def send_email2(user, pwd, recipient, subject, body):

	#try:
		#server = smtplib.SMTP("smtp.gmail.com", 587)
		server_ssl = smtplib.SMTP_SSL("localhost", 25)
		server_ssl.ehlo()
		#server_ssl.starttls()
		server_ssl.login(user, pwd)

		msg = MIMEMultipart()

		# setup the parameters of the message
		msg['From']="bhatshravan@yahoo.com"
		msg['To']=(recipient)
		msg['Subject']=subject
		msg['Body']=body
		msg.attach(MIMEText(body, 'plain'))

		# send the message via the server set up earlier.
		server_ssl.send_message(msg)
		
		
		server_ssl.sendmail("helloworld@gm", recipient, msg.as_string())
		server_ssl.close()
		
		print("successfully sent the mail")

if __name__ == '__main__':
	send_email("bhatshravan@yahoo.com","no-man","shrvnbhat99@gmail.com","Derp","Cool boy")
	#send_email("computernetworkksit@gmail.com","ksitksitksit","shrvnbhat@gmail.com","No name","Nin amma is goo5")

	#server_ssl.login("bhatshravan@yahoo.com","wi-jazzhtml##55")