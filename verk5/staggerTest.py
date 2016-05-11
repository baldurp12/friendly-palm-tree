import stagger
from stagger import *
from pprint import pprint as pp

file_path = r'C:\Users\Baldur\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\ipod\F00\BNXG.mp3'

def stagger_test():
    tag_dict = {}
    try:
        tag = stagger.read_tag(file_path)
        tag_dict['artist'] = ''.join(x for x in tag.artist if x not in ',<>:"/\|?*')
        tag_dict['title'] = ''.join(y for y in tag.title if y not in ',<>:"/\|?*')
        tag_dict['album'] = ''.join(z for z in tag.album if z not in ',<>:"/\|?*')
        tag_dict['track'] = tag.track ## Skilar núll ef að ekki er til track ?
    except:
        print('failed')
        tag_dict = {'artist': '', 'album': '', 'title': '', 'track': ''} ## If stagger can't read the ID3, we put placeholders in the values we need

    
    pp(tag_dict)



stagger_test()
