Fix_my_ipod er scripta sem er ætluð til að raða MP3 skrám, sérstaklega með það í huga að endurnefna
skrár sem ekki heita lýsandi nöfnum(t.d eins og skrár sem að iPodar hafa endurskírt).

ATHUGIÐ:
Scriptan endurnefnir ALLAR MP3 SKRÁR sem innihalda laganafn	
Finni scriptan ekki nafn 'artist' reynir hún að flokka eftir 'album'
Þar sem að scriptan leitar eftir 'artist' fyrst, gæti það gerst að sama 'album' lendi 
í mörgum möppum, þá skipt eftir flytjendum.

Scriptunni er ætlað keyra í þeirri möppu sem geymir MP3 skrárnar 
hún leitar aðeins í undirmöppum og leitar einungis að skrám með .mp3 endingu

Scriptan afritar einungis skrárnar en eyðir engum skrám (vonum við)

Efst í fix_my_ipod.py skránni er að finna tvær breytur, 
þær ákveða möppu-heiti þangað sem að skrárnar eru afritaðar:
copy_folder: þangað fara allar skrár þar sem að fannst 'artist'
other_folder: Þangað fara allar skrára þar sem að ekki fannst 'artist' þeim gæti þó verið raðað eftir 'album'

Séu einhverjar skrár sem ekki var hægt að lesa er hægt að sjá error messages í resault.log sem að verður til
við fyrstu keyrslu.

Skriptan var prufuð með þeim mp3 skrám er fylgdu verkefninu
og var prufuð á bæði Windows og Mac OS x

PyPi package requirements:
fix_my_ipod notar stagger (pip install stagger / easy_install stagger):
https://pypi.python.org/pypi/stagger