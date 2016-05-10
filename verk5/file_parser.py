import stagger
import os
from stagger.id3 import *  

def file_parser(file_path):

##	smíða dictionary með stagger:
    tag_dict = {}
    try:
        tag = stagger.read_tag(file_path)
        tag_dict['artist'] = tag.artist
        tag_dict['title'] = tag.title
        tag_dict['album'] = tag.album
        tag_dict['track'] = tag.track
    except:
        tag_dict = {'artist': '', 'album': '', 'title': '', 'track': ''}


        
##	SETJA TÓMAN STRENG EF AÐ EITTHVAÐ TAG ER EKKI TIL !



    if tag_dict['artist'] != '':
##		move_to_artist(file_path, tag_dict)
        print(' move to artist ' + '\n' + file_path + '\n')
        print(tag_dict)
    else:
        print(' move to other ' + file_path + '\n')
        print(tag_dict)
##		move_to_other(file_path, tag_dict)




file_path = r"C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\ipod\F48\CUCH.mp3"

file_parser(file_path)
