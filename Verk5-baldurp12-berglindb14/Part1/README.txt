Fix_my_ipod er scripta sem er �tlu� til a� ra�a MP3 skr�m, s�rstaklega me� �a� � huga a� endurnefna
skr�r sem ekki heita l�sandi n�fnum(t.d eins og skr�r sem a� iPodar hafa endursk�rt).

ATHUGI�:
Scriptan endurnefnir ALLAR MP3 SKR�R sem innihalda laganafn	
Finni scriptan ekki nafn 'artist' reynir h�n a� flokka eftir 'album'
�ar sem a� scriptan leitar eftir 'artist' fyrst, g�ti �a� gerst a� sama 'album' lendi 
� m�rgum m�ppum, �� skipt eftir flytjendum.

Scriptunni er �tla� keyra � �eirri m�ppu sem geymir MP3 skr�rnar 
h�n leitar a�eins � undirm�ppum og leitar einungis a� skr�m me� .mp3 endingu

Scriptan afritar einungis skr�rnar en ey�ir engum skr�m (vonum vi�)

Efst � fix_my_ipod.py skr�nni er a� finna tv�r breytur, 
��r �kve�a m�ppu-heiti �anga� sem a� skr�rnar eru afrita�ar:
copy_folder: �anga� fara allar skr�r �ar sem a� fannst 'artist'
other_folder: �anga� fara allar skr�ra �ar sem a� ekki fannst 'artist' �eim g�ti �� veri� ra�a� eftir 'album'

S�u einhverjar skr�r sem ekki var h�gt a� lesa er h�gt a� sj� error messages � resault.log sem a� ver�ur til
vi� fyrstu keyrslu.

Skriptan var prufu� me� �eim mp3 skr�m er fylgdu verkefninu
og var prufu� � b��i Windows og Mac OS x

PyPi package requirements:
fix_my_ipod notar stagger (pip install stagger / easy_install stagger):
https://pypi.python.org/pypi/stagger