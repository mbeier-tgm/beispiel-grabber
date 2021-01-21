import requests
import os

# Store the exercises
beispiele = []

# URLS
teilA = "https://aufgabenpool.at/srdp/teila/"
teilB = "https://aufgabenpool.at/srdp/teilb1/"

# Trim the HTML data to only include the listing of the exercises
htmlA = requests.get(teilA).content
htmlA = htmlA.decode().split("<table>")[1]
htmlA = htmlA.split("</table>")[0]
htmlA = htmlA.split("<tr>")

htmlB = requests.get(teilB).content
htmlB = htmlB.decode().split("<table>")[1]
htmlB = htmlB.split("</table>")[0]
htmlB = htmlB.split("<tr>")

for i in range(4):
	del htmlA[0]
	del htmlB[0]

for i in range(272, len(htmlA)):
	del htmlA[272]

for i in range(469, len(htmlB)):
	del htmlB[469]

# Parse the links to the PDFs out of the HTML data
for i in range(len(htmlA)):
	tds = htmlA[i].split("<td")
	args = tds[2].split(">")
	link = args[2].split("<")[0]
	beispiele.append(teilA + link)

for i in range(len(htmlB)):
	tds = htmlB[i].split("<td")
	args = tds[2].split(">")
	link = args[2].split("<")[0]
	beispiele.append(teilB + link)

# Download all PDFs
os.mkdir(os.path.join(os.getcwd(), "Beispiele"))
for i in range(len(beispiele)):
	htmlBeispiel = requests.get(beispiele[i]).content
	pdfName = htmlBeispiel.decode().split(".pdf")[1][2:]
	beispiele[i] = beispiele[i] + pdfName + ".pdf"
	pdf = requests.get(beispiele[i])
	with open('Beispiele/' + pdfName + ".pdf", 'wb') as f:
		f.write(pdf.content)
		f.close()



