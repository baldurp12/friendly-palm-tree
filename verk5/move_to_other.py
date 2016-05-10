import os
import shutil


def move_to_other(): ##file_path, tag_dict
    
    ##----album er tomt----##

    if tag_dict['album'] == '':
        print("ekki album")
        ##copy_and_rename(new_path, file_path, tag_dict)
    
    else:
        album_path = os.path.join(new_path, tag_dict['album'])
        os.mkdir(album_path)
        ##print(album_path)
        ##copy_and_rename(album_path, file_path, dict)




tag_dict = {'artist' : '', 'album': 'love and peace', 'title': '- . - _'}

file_path = r'/Users/berglindliljabjornsdottir/Documents/python/ipod/F02/WKLF.mp3'
new_path = r'/Users/berglindliljabjornsdottir/Documents/python/stagger-test/copy-folder/00trash'

move_to_other()
