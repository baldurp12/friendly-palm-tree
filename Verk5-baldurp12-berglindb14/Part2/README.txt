QizUp er auglj�s tilraun til a� taka yfir heimsveldi� QuizUp
QizUp er einfalt spurninga kerfi hugsa� fyrir b�rn og Hjalta

Me� QizUp fylgja 3 m�ppur sem nau�synlegar eru til keyrslu:
answers: �ar liggja texta skr�r me� sv�rum fyrir hvert topic fyrir sig
questions: �ar liggja texta skr�r me� spurningum fyrir hvert topic fyrir sig
pictures: �ar er a� finna einstaklega gl�silegar og s�rhanna�ar myndir

Vi� fyrstu keyrslu �tb�r QizUp JSON skr�nna QandA.JSON me� spurningum og sv�rum

JSON skr�in er � forminu:
{
	'topic':
	{'question01': 'Question',
	 'answer01': 'Answer'
	 }
}

H�gt er a� loka QizUp me� �v� a� fara � file->exit
� glugganum er a� finna turtles icon (picture/turtles.ico)

Til a� einfalda pr�fun eru h�r fyrstu sv�rin vi� 'Animal' spurningum:
"question01": "What food makes up nearly all (around 99%) of a Giant Panda's diet?",      
"answer01": "Bamboo"
 
"question02": "True or false? Mice live for up to 10 years.",
"answer02": "False"

"question03": "What is the name of the phobia that involves an abnormal fear of spiders?",
"answer03": "Arachnophobia"

"question04": "What is the largest type of 'big cat' in the world?",
"answer04": "The tiger"

"question05": "True or false? Crocodiles have no sweat glands so they use their mouths to release heat.",
"answer05": "True"

Annars eru �ll sv�r � answers m�ppunni og h�gt a� sj� � QandA.JSON skr�nni s� h�n til (ver�ur til eftir fyrstu keyrslu)
Athuga�u a� sv�rin eru ekki case-sensitive

PyPi package requirements:
QizUp notar Pillow (pip install pillow) 
https://pypi.python.org/pypi/Pillow/3.2.0







