from pprint import pprint as pp
import taglib
import os
import string
import eyed3
import stagger


def test_pytaglib():


##    a = r"C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\ipod\F00"
##    b = os.listdir(a)
##    print(a)
##    print(b)
##    artist_list = []
##    for i in b:
##        if i.endswith('.mp3'):
##            f = taglib.File(os.path.join(a, i))
##            try:
##                artist_list.append(f.tags['ARTIST'])
##            except:
##                print('No artist in: \n' + i)
##    pp(artist_list)
##    return 5

    a = r"C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\ipod\baldur\jolasveinn.mp3"
    f = taglib.File(a)
    print(f.tags)


test_pytaglib()
