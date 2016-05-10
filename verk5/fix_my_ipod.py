import os
from os import path as pa
from os.path import join as jo
from stagger import *
from pprint import pprint as pp

copy_folder = '00_copy_folder'
other_folder = '00_Other'
log_file = open('resaults.log', 'a')

def list_dir_test():
    multi_pass_check = [] ## Hluti af testi, ma henda i tiltekt
    
    ##----MAKE COPY FOLDER AND OTHER FOLDER----##


    
    try:
        os.mkdir(os.path.join(os.getcwd(), copy_folder))
    except:
        log_file.write('Could not create the folder: ' + copy_folder)
        print('Could not create the folder: ' + copy_folder)

    try:
        os.mkdir(os.path.join(os.getcwd(), other_folder))
    except:
        log_file.write('Could not create the folder: ' + other_folder)
        print('Could not create the folder: ' + other_folder)
##        print('enter "y" to continue')
##        user_choice = input()
##        if user_choice == ('y'):
##            pass
##        else:
##            print('User aborted')
##            return 0
    

    
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
        move_to_artist(file_path, tag_dict)
##        print('Move to artist ' + '\n' + file_path + '\n')
##        pp(tag_dict)
    else:
        log_file.write('\n' + 'Move to other: ' + '\n' + file_path + '\n')
        print('\n' + 'Move to other: ' + '\n' + file_path + '\n')
        pp(tag_dict)
##		move_to_other(file_path, tag_dict)



def move_to_artist(file_path, tag_dict):

        ##----if we have multiple artists----##   
    
    if type(tag_dict['artist']) == list:
        just_album_path = os.path.join(copy_folder, tag_dict['album'])
        #print(just_album_path)
        if os.path.isdir(just_album_path):
            pass
        else:
            log_file.write('\n' + 'Making folder: ' + just_album_path)
            print('Making folder: ' + just_album_path)
##            os.mkdir(just_album_path)
        ## copy_and_rename(just_album_path, file_path, dict)
        ##----if we have one artist----##
    else:
        artist_path = os.path.join(copy_folder , tag_dict['artist'])
        if os.path.isdir(artist_path):
            pass
        else:
            log_file.write('\n' + 'Making folder: ' + artist_path)
            print('\n' + 'Making folder: ' + artist_path)
##            os.mkdir(artist_path)

        if tag_dict['album'] != "":
                ##---- if we have an aritst and an album----##
            
            ##print(album_path)
            album_path = os.path.join(copy_folder, os.path.join(tag_dict['artist'], tag_dict['album']))
            if os.path.isdir(album_path):
                pass
            else:
                log_file.write('\n' + 'Making folder: ' + album_path)
                print('\n' + 'Making folder: ' + album_path)
##                os.mkdir(album_path)
                    ## copy_and_rename(album_path, file_path, dict)
                ## -----if we just have an artist but no album-----##
        ##else:
                ## copy_and_rename(artist_path, file_path, dict) 

    

list_dir_test()

