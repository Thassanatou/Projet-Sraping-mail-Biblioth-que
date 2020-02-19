import smtplib
import csv
from email.message import EmailMessage


tomails = []
#Lire un fichier CSV
with open('nom de fichier csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)


#ligne les lignes
	for line in csv_reader:
		col1 = line['col1']
		col2 = line['col2']
		col3 = line['col3']
		tomails.append(f"{col1}")


		#envoyé un mail
		conn = smtplib.SMTP('imap.gmail.com',587)
		conn.ehlo()
		conn.starttls()
		conn.login('ton mail', 'mot de passe')
	

		for tomail in tomails:
			msg = EmailMessage()
			msg['Subject'] = 'Essai PYTHON'
			msg['From'] =  'ton mail'
			msg['To'] = tomail
			#msg.set_content(f'<p>J\'ai envoyé {len(tomails)} messages via python</p>')
			msg.set_content('Bonjour {},\n\n essai python {} \n  {}'.format(col1,col2, col3))


		conn.send_message(msg)
		print(tomail)

	nombre_mail = f'<p>vous avez envoyé {len(tomails)} mails</p>'
	print(nombre_mail)

	conn.quit()