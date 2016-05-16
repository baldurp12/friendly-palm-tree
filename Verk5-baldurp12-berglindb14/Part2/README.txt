QizUp er augljós tilraun til að taka yfir heimsveldið QuizUp
QizUp er einfalt spurninga kerfi hugsað fyrir börn og Hjalta

Með QizUp fylgja 3 möppur sem nauðsynlegar eru til keyrslu:
answers: þar liggja texta skrár með svörum fyrir hvert topic fyrir sig
questions: þar liggja texta skrár með spurningum fyrir hvert topic fyrir sig
pictures: þar er að finna einstaklega glæsilegar og sérhannaðar myndir

Við fyrstu keyrslu útbýr QizUp JSON skránna QandA.JSON með spurningum og svörum

JSON skráin er á forminu:
{
	'topic':
	{'question01': 'Question',
	 'answer01': 'Answer'
	 }
}

Hægt er að loka QizUp með því að fara í file->exit
Á glugganum er að finna turtles icon (picture/turtles.ico)

Til að einfalda prófun eru hér fyrstu svörin við 'Animal' spurningum:
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

Annars eru öll svör í answers möppunni og hægt að sjá í QandA.JSON skránni sé hún til (verður til eftir fyrstu keyrslu)
Athugaðu að svörin eru ekki case-sensitive

PyPi package requirements:
QizUp notar Pillow (pip install pillow) 
https://pypi.python.org/pypi/Pillow/3.2.0







