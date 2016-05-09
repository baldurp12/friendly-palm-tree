from pprint import pprint as pp
import taglib
import os
import string
import eyed3


def test_pytaglib():


    a = os.getcwd()
    b = os.listdir(a)
    print(a)
    print(b)
    artist_list = []
    for i in b:
        if i.endswith('.mp3'):
            f = taglib.File(os.path.join(a, i))
            try:
                artist_list.append(f.tags['ARTIST'])
            except:
                print('No artist in: ' + f.tags)
    return 5


test_pytaglib()
