import FUNC as f
from sys import argv

f.log("reading file")

deck=f.readYaml("CAH.yaml")

f.log("read file")

mainDeck=deck[0]
mainDeckWhite=mainDeck["white"]
mainDeckBlack=mainDeck["black"]

whiteCards=[]

for card in mainDeckWhite:
	whiteCards+=[card["text"]]

blackCards=[]

for card in mainDeckBlack:
	blackCards+=[[card["text"],card["pick"]]]

f.log("made decks")

f.log("length of white deck is "+str(len(mainDeckWhite)))
f.log("length of black deck is "+str(len(mainDeckBlack)))

default=f.read("WHITECARD.svg")

f.log("read svg")

for i in range(len(whiteCards)):
	svg=default
	text=f.splitStringWithDash(
		whiteCards[i],20
	)

	f.log("card: "+whiteCards[int(i)])

	f.log("text: "+str(text))

	locations=["Ѹ","Ψ","Ѻ","Ө","ӿ","ʨ","~","Ϟ","ʬ"]

	for n in range(len(text)):
		svg=svg.replace(locations[n],text[n])

	for location in locations:
		svg=svg.replace(location,"")

	f.write("WHITE"+str(i)+".svg",svg)
	f.log("wrote svg "+str(i))

f.log("processing black cards")
blackText=[]
for i in range(len(blackCards)):
	if blackCards[i][1]==2:
		blackText+=["Draw 2."]
	else:
		blackText+=[""]
	blackCards[i]=blackCards[i][0]
f.log("processed")

f.log("reading svg")
default=f.read("BLACKCARD.svg")
f.log("read svg")

for i in range(len(blackCards)):
	svg=default
	text=f.splitStringWithDash(
		blackCards[i],20
	)

	if len(text)==8:
		text=text+[blackText[i]]
	else:
		text=text+[" ",blackText[i]]

	f.log("card: "+blackCards[int(i)])

	f.log("text: "+str(text))

	locations=["Ѹ","Ψ","Ѻ","Ө","ӿ","ʨ","~","Ϟ","ʬ"]

	for n in range(len(text)):
		if not text[n]=="":
			svg=svg.replace(locations[n],text[n])

	for location in locations:
		svg=svg.replace(location,"")

	f.write("BLACK"+str(i)+".svg",svg)

	f.log("wrote svg "+str(i))


f.log("converting files into pdf")
import cairosvg
import os

f.log("converting white cards into png")

def toPng(inFile,outFile):
	cairosvg.svg2pdf(
		file_obj=open(inFile, "rb"), write_to=outFile)
	os.remove(inFile)

for i in range(len(whiteCards)):
	f.log("converting "+str(i))
	toPng("WHITE"+str(i)+".svg","WHITE"+str(i)+".pdf")

f.log("conversion done")

f.log("merging all white cards")
from PyPDF2 import PdfFileMerger, PdfFileReader
 
mergedObject = PdfFileMerger()

for i in range(len(whiteCards)):
	f.log("merging "+str(i))
	mergedObject.append(PdfFileReader("WHITE"+str(i)+'.pdf', 'rb'))
	os.remove("WHITE"+str(i)+'.pdf')

mergedObject.write("WHITE.pdf")
f.log("merged all white")

for i in range(len(blackCards)):
	f.log("converting "+str(i))
	toPng("BLACK"+str(i)+".svg","BLACK"+str(i)+".pdf")

f.log("conversion done")

f.log("merging black cards")
 
mergedObject = PdfFileMerger()

for i in range(len(blackCards)):
	f.log("merging "+str(i))
	mergedObject.append(PdfFileReader("BLACK"+str(i)+'.pdf', 'rb'))
	os.remove("BLACK"+str(i)+'.pdf')

mergedObject.write("BLACK.pdf")

f.log("merged black")
f.log("merging white and black")

mergedObject = PdfFileMerger()

mergedObject.append(PdfFileReader("BLACK.pdf", 'rb'))
mergedObject.append(PdfFileReader("WHITE.pdf", 'rb'))

mergedObject.write("CARDS.pdf")

f.log("done")
