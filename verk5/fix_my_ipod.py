import os
from os import path as pa
from os.path import join as jo
from stagger import *           ## Stagger: pip install stagger
from pprint import pprint as pp ## Used for 'debugging'

copy_folder = '00_copy_folder'
other_folder = '00_Other'
log_file = open('resaults.log', 'a')

def list_dir_test():
    multi_pass_check = [] ## Hluti af testi, ma henda i tiltekt
    

    ##---- Making copy_folder and other_folder ----##
    
    try:
        os.mkdir(os.path.join(os.getcwd(), copy_folder))
    except:
        if os.path.isdir(os.path.join(os.getcwd(), copy_folder)):
            pass
        else:
            log_file.write('ERROR While making folder: ' + copy_folder)
            print('Could not create folder: ' + copy_folder)
            return 0 ##Abort if cant make copy_folder and copy_folder doesnt exist


    try:
        os.mkdir(os.path.join(os.getcwd(), other_folder))
    except:
        if os.path.isdir(os.path.join(os.getcwd(), other_folder)):
            pass
        else:
            log_file.write('ERROR While making folder: ' + other_folder)
            print('Could not create folder: ' + other_folder)
            print('enter "y" to continue')
            return 0    ##Abort if cant make other_folder and other_folder doesnt exist



    ##---- Start walking through folders ----#
    a = [x[0] for x in os.walk(os.getcwd())]
    test_list = []
    for i in a[1:]:
        for j in os.listdir(i):
            curr_path = pa.join(i,j)
            if pa.isfile(curr_path) and j.endswith('.mp3'):
                file_parser(curr_path)
 
        
        


def file_parser(file_path):

    ##---- Create dictionary with stagger ----##
    
    tag_dict = {}
    try:
        tag = stagger.read_tag(file_path)
        tag_dict['artist'] = ''.join(x for x in tag.artist if x not in ',<>:"/\|?*')
        tag_dict['title'] = ''.join(y for y in tag.title if y not in ',<>:"/\|?*')
        tag_dict['album'] = ''.join(z for z in tag.album if z not in ',<>:"/\|?*')
        tag_dict['track'] = tag.track ## Skilar núll ef að ekki er til track ?
    except:
        tag_dict = {'artist': '', 'album': '', 'title': '', 'track': ''} ## If stagger can't read the ID3, we put placeholders in the values we need

##Kanski tjékka hvort að það sé hægt að finna artist i title ##

    if tag_dict['artist'] != '':
        move_to_artist(file_path, tag_dict)
        
##        print('Move to artist ' + '\n' + file_path + '\n')
##        pp(tag_dict)
        
    else:
        log_file.write('\n' + 'Move to other: ' + '\n' + file_path + '\n')
        print('\n' + 'Move to other: ' + '\n' + file_path + '\n')
        pp(tag_dict)
        move_to_other(file_path, tag_dict)


def move_to_artist(file_path, tag_dict):

        ##----if we have multiple artists----##   
    
    if type(tag_dict['artist']) == list:
        just_album_path = os.path.join(copy_folder, tag_dict['album'])
        
##        print(just_album_path)
        if os.path.isdir(just_album_path):
            pass
        else:
            log_file.write('\n' + 'Making folder: ' + just_album_path)
            print('Making folder: ' + just_album_path)
            os.mkdir(just_album_path)
##            copy_and_rename(just_album_path, file_path, dict)


        ##----if we have one artist----##
    else:
        artist_path = os.path.join(copy_folder , tag_dict['artist'])
        if os.path.isdir(artist_path):
            pass
        else:
            log_file.write('\n' + 'Making folder: ' + artist_path)
            print('\n' + 'Making folder: ' + artist_path)
##            os.mkdir(artist_path)


        ##---- if we have an aritst and an album ----##

            
            
        if tag_dict['album'] != "":            
            album_path = os.path.join(copy_folder, os.path.join(tag_dict['artist'], tag_dict['album']))
            print(album_path)

            if os.path.isdir(album_path):
                pass
            else:
                log_file.write('\n' + 'Making folder: ' + album_path)
                print('\n' + 'Making folder: ' + album_path + '\n'
                      + file_path)
                os.mkdir(album_path)
##            copy_and_rename(album_path, file_path, dict)


        ##---- if we just have an artist but no album ----##
        else:
            pass
##            copy_and_rename(artist_path, file_path, dict)


def move_to_other(file_path, tag_dict):
    
    ##----album er tomt----##

    if tag_dict['album'] == '':
        print("ekki album")
        new_path = os.path.join(os.getcwd(), other_folder)

    else:
        path_other_folder = os.path.join(os.getcwd(), other_folder)
        
        new_path = os.path.join( path_other_folder , tag_dict['album'])

        print('Making: ' + new_path + '\n')
        
        try:
            os.mkdir(new_path)
        except:
            print('Cannot make folder: ' + new_path)


    print('Sending ' + os.path.split(file_path)[1] + '\n'
          'To: ' + new_path + '\n')

    

