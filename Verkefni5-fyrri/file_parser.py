import stagger
import os
from stagger.id3 import *
from pprint import pprint as pp

def file_parser(file_path):

##	smíða dictionary með stagger:
    tag_dict = {}
    try:
        tag = stagger.read_tag(file_path)
        tag_dict['artist'] = tag.artist
        tag_dict['title'] = tag.title
        tag_dict['album'] = tag.album
        tag_dict['track'] = tag.track ## Skilar núll ef að ekki er til track ?
    except:
        tag_dict = {'artist': '', 'album': '', 'title': '', 'track': ''} ## If stagger can't read the ID3, we put placeholders in the values we need

            ## Kanski tjékka hvort að það sé hægt að finna artist i title ##

    if tag_dict['artist'] != '':
##		move_to_artist(file_path, tag_dict)
        print('Move to artist ' + '\n' + file_path + '\n')
        pp(tag_dict)
    else:
        print('Move to other: ' + '\n' + file_path + '\n')
        pp(tag_dict)
##		move_to_other(file_path, tag_dict)




file_path = r"C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\ipod\F29\UAVT.mp3"

file_parser(file_path)
