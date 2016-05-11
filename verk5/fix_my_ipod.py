import os
from os import path as pa
from os.path import join as jo
from stagger import *           ## Stagger: pip install stagger
from pprint import pprint as pp ## Used for 'debugging'
import shutil
from shutil import copy2 as copy2
import datetime


copy_folder = '00_copy_folder'
other_folder = '00_Other'




def fix_my_ipod():
    global log_file
    log_file = open('ERROR_LOG.log', 'a')   

    ##---- Making copy_folder and other_folder ----##
    
    try:
        os.mkdir(os.path.join(os.getcwd(), copy_folder))
    except:
        if os.path.isdir(os.path.join(os.getcwd(), copy_folder)):
            pass
        else:
            timestamp = str(datetime.datetime.now()).split('.')[0]
            log_file.write('\n' + timestamp + ' ERROR While making folder: ' + copy_folder + '\n')
            return 0 ##Abort if cant make copy_folder and copy_folder doesnt exist


    try:
        os.mkdir(os.path.join(os.getcwd(), other_folder))
    except:
        if os.path.isdir(os.path.join(os.getcwd(), other_folder)):
            pass
        else:
            timestamp = str(datetime.datetime.now()).split('.')[0]
            log_file.write('\n' + timestamp + ' ERROR While making folder: ' + other_folder +'\n')
            return 0    ##Abort if cant make other_folder and other_folder doesnt exist



    ##---- Start walking through folders ----#
    a = [x[0] for x in os.walk(os.getcwd())]
    test_list = []
    for i in a[1:]:
        for j in os.listdir(i):
            curr_path = pa.join(i,j)
            if pa.isfile(curr_path) and j.endswith('.mp3'):
                file_parser(curr_path)
 
        
    log_file.close()


def file_parser(file_path):

    ##---- Create dictionary with stagger ----##
    
    tag_dict = {}
    try:
        tag = stagger.read_tag(file_path)
        tag_dict['artist'] = (''.join(x for x in tag.artist if x not in ',<>:"/\\|?*\'')).strip() or ''
        tag_dict['title'] = (''.join(y for y in tag.title if y not in ',<>:"/\\|?*\'')).strip() or ''
        tag_dict['album'] = (''.join(z for z in tag.album if z not in ',<>:"/\\|?*\'')).strip() or ''
        tag_dict['track'] = tag.track or 0
    except:
        timestamp = str(datetime.datetime.now()).split('.')[0]
        log_file.write('\n' + timestamp + ' ERROR Something went wrong when compiling META of file: \n' + file_path)
        tag_dict = {'artist': '', 'album': '', 'title': '', 'track': 0} ## If stagger can't read the ID3, we put placeholders in the values we need




##Kanski tjékka hvort að það sé hægt að finna artist i title ##

    if tag_dict['artist'] != '':
        move_to_artist(file_path, tag_dict)
        
##        print('Move to artist ' + '\n' + file_path + '\n')
##        pp(tag_dict)
        
    else:
##        log_file.write('\n' + 'Move to other: ' + '\n' + file_path + '\n')
##        print('\n' + 'Move to other: ' + '\n' + file_path + '\n')
##        pp(tag_dict)
        move_to_other(file_path, tag_dict)


def move_to_artist(file_path, tag_dict):

        ##----if we have multiple artists----##   
    path_to_copy_folder = os.path.join(os.getcwd(),copy_folder)
    
    if type(tag_dict['artist']) == list:
        just_album_path = os.path.join(path_to_copy_folder, tag_dict['album'])

        if os.path.isdir(just_album_path):
            pass
        else:
            
            os.mkdir(just_album_path)
            copy_and_rename(just_album_path, file_path, dict)


        ##----if we have one artist----##
    else:
        artist_path = os.path.join(path_to_copy_folder , tag_dict['artist'])
        if os.path.isdir(artist_path):
            pass
        else:
##            log_file.write('\n' + 'Making folder: ' + artist_path)
##            print('\n' + 'Making folder: ' + artist_path)
            os.mkdir(artist_path)


        ##---- if we have an aritst and an album ----##
    
        if tag_dict['album'] != "":            

            artist_album = os.path.join(tag_dict['artist'], tag_dict['album'])
            
            album_path = os.path.join(path_to_copy_folder, artist_album)
##            print(album_path)

            if os.path.isdir(album_path):
                pass
            else:
##                log_file.write('\n' + 'Making folder: ' + album_path)
##                print('\n' + 'Making folder: ' + album_path + '\n'
##                      + file_path)
                os.makedirs(album_path) ## Using makedirs instead of mkdir because we try to make folder/child folder in one move

            copy_and_rename(album_path, file_path, tag_dict)


        ##---- if we just have an artist but no album ----##
        else:
            copy_and_rename(artist_path, file_path, dict)


def move_to_other(file_path, tag_dict):
    
    path_to_other_folder = os.path.join(os.getcwd(), other_folder)
    
    ##----album er tomt----##

    if tag_dict['album'] == '':
##        print("ekki album")
        new_path = path_to_other_folder

    else:
        new_path = os.path.join( path_to_other_folder , tag_dict['album'])

##        print('Making: ' + new_path + '\n')
       
        try:
            os.mkdir(new_path)
        except:
            timestamp = str(datetime.datetime.now()).split('.')[0]
            log_file.write('\n' + timestamp + ' ERROR While making folder: ' + new_path)
##            print('Cannot make folder: ' + new_path)

##    print('Sending ' + os.path.split(file_path)[1] + '\n'
##          'To: ' + new_path + '\n')

    copy_and_rename(new_path, file_path, tag_dict)

def copy_and_rename(final_path, file_path, tag_dict):


    old_file_name = os.path.split(file_path)[1]

    new_file_name = old_file_name ##if we dont do any changes to old_file_name we keep the name
##
##    print('final_path: \n' +
##          final_path + '\n' +
##          'file_path: ' +
##          file_path)
##    
##    log_file.write('\n' +  'final_path: \n' +
##          final_path + '\n' +
##          'file_path: ' +
##          file_path)

    try:
        if tag_dict['title'] == '':
            if tag_dict['track'] == 0:
                pass
            else:
                new_file_name = str(tag_dict['track']) + old_file_name
        else:
            if tag_dict['track'] == 0:
                new_file_name = tag_dict['title'] + '.mp3'
            else:
                if tag_dict['track']:
                    new_file_name = '0' + str(tag_dict['track']) + ' - ' + tag_dict['title'] + '.mp3'
                else:
                    new_file_name = str(tag_dict['track']) + '-' + tag_dict['title'] + '.mp3'
    except:
        timestamp = str(datetime.datetime.now()).split('.')[0]
        log_file.write('\n' + timestamp + ' FAILED WHEN TRYING TO CHECK: ' + '\n' + file_path)

 
    new_file_path = os.path.join(final_path, new_file_name)

    if os.path.isfile(new_file_path):
        timestamp = str(datetime.datetime.now()).split('.')[0]
        log_file.write('\n' + timestamp + ' ' + new_file_name + ' ALREADY IN : \n' + final_path + '\n' 'OLD FILE NAME: ' + old_file_name)
##        print(new_file_name + ' ALREADY IN : \n' + final_path + '\n' 'OLD FILE NAME: ' + old_file_name)
    else:
##        print('Copy to folder!')
##        print (old_file_name + ' was changed to ' + new_file_name)
        try:
            copy2(file_path, new_file_path)
        except:
            timestamp = str(datetime.datetime.now()).split('.')[0]
            log_file.write('\n' + timestamp + ' ERROR Something went wrong when trying to copy' + file_path)


    

