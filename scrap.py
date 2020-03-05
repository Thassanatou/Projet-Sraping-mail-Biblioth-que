import urllib.request
import re
import csv
from bs4 import BeautifulSoup as b
# importer le premier url(region) de la page
url_region = "https://www.annuaire-mairie.fr/bibliotheque.html"
html = urllib.request.urlopen(url_region).read()
soup = b(html, "html.parser")
# exporter le fichier comme csv
file = open('bibliotheque_ile_de_france.csv', 'w+')
writer = csv.writer(file)
# la premiere ligne
writer.writerow(['DEPARTEMENT', 'VILLE', 'ADRESSE', 'CP' ,'E-MAIL'])
#selectionne les données qui correspondent à la region îles de France par "id" puis par "li"
for region in soup.find("div", {"id" : "bibliotheque_11_content"}):
	for dep in region.findAll("li", {"class" : "lazy"}):
		nom_departement = dep.div.a
		dep_link = nom_departement['href']
		departements = nom_departement.text
		#print(" ")
		#print(departements)
		#print(" ")
		# importer le deuxieme  url de tous les pages du departement	
		url1 = "https://www.annuaire-mairie.fr" + dep_link
		html1 = urllib.request.urlopen(url1).read()
		soup1 = b(html1, "html.parser")
		#selectionner le "a" de toutes les villes des departement de "dep_link"
		for departement in soup1.findAll("table",{"class": "tblmaire"}):
			for ville in departement.findAll("a"):
				ville_link = ville['href']
				villes = ville.text
				# importer le  url de tous les pages des villes
				url2 = "https://www.annuaire-mairie.fr" + ville_link
				html2 = urllib.request.urlopen(url2).read()
				soup2 = b(html2,"html.parser")
				#filtrer le "div" qui  correspond aux adresses du bibliotheque de la ville par  "ville_link"
				bibliotheque = soup2.find("div",{"class": "ville_info"})
				#on suprime le mot "Adresse" qui est devant les liens
				adresse = bibliotheque.p.text.replace(" Adresse", "").rpartition("\n")
				rue = adresse[0].replace("\n", ", ")
				CP = adresse[2].replace("(Le)", "").replace("(La)", "")
				#filtrer tous les bibliotheques qui ont un adresse mail
				for email in bibliotheque.findAll(text=re.compile("@")):
					#print(departement)
					print(villes)
					print(rue)
					print(CP)
					print(email)
					print(" ")
					writer.writerow([departements, villes, rue, CP,  email])
file.close()
							
