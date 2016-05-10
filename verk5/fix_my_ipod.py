import os
from os import path as pa
from os.path import join as jo
from stagger import *
from pprint import pprint as pp

def list_dir_test():
    multi_pass_check = []
    
    a = [x[0] for x in os.walk(os.getcwd())]
    test_list = []
    for i in a[1:]:
        for j in os.listdir(i):
            curr_path = pa.join(i,j)
            if pa.isfile(curr_path) and j.endswith('.mp3'):
##                if j in multi_pass_check:
##                    print('\n' + j + ' is already parsed' + '\n and is in: ' + curr_path)
##                else:
##                    multi_pass_check.append(j)
                file_parser(curr_path)



##                try:
##                    tag = stagger.read_tag(curr_path)
##                    test_list.append(tag.artist)
##                except:
##                    print(curr_path)
##
##    print(set(test_list))
##    
        
        


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




list_dir_test()

