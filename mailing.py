
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib 


host ="smtp.gmail.com"
port = 587
username = "hass.djire@gmail.com"
password = "jadoelakqmtamixo"
from_email =  username
emaillist = open('/home/djire-pro/dossier_hass/essai.csv', 'r').readlines()


to_liste = ["hass.djire@gmail.com"]
#subject = 'Essaie Gmail'
#body = 'j utilise python pour envoyer le message'
#msg = f'Sujet: {subject}\n\n{body} .'
try:
	email_conn = smtplib.SMTP(host, port)
	email_conn.ehlo()
	email_conn.starttls()
	email_conn.login(username, password)
	#email_conn.sendmail(from_email, to_liste, msg)
	#email_conn.quit()

	the_msg = MIMEMultipart("alternative")
	the_msg['Subject'] = "Saluut"
	the_msg["From"] = from_email
	#the_msg["To"] = email

	plain_tex ="Essaie message"
	html_txt = """\
	<html>
	<head></head>
	<body>
	<h3>Hey!</h3><br><p>
	Essaie message
	</p>
	</body>
	</html>
	"""

	part_1 = MIMEText(plain_tex, 'plain')
	part_2 = MIMEText(html_txt, 'HTML')

	the_msg.attach(part_1)
	the_msg.attach(part_2)

	#print(the_msg.as_string())

	email_conn.sendmail(from_email,to_liste,the_msg.as_string())
	email_conn.quit()
	print ("ok")
except smtplib.SMTPException:
	print("Error sendind message")


	