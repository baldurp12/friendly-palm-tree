import stagger
import os
from stagger.id3 import *  

def move_to_artist(): ##file_path, dict
        ##-----if we have multiple artists-----
    
    
    if type(tag_dict['artist']) == list:
        just_album_path = os.path.join(new_path, tag_dict['album'])
        #print(just_album_path)
        os.mkdir(just_album_path)
        ## copy_and_rename(just_album_path, file_path, dict)
        ##-----if we have one artist-------
    else:
        artist_path = os.path.join(new_path, tag_dict['artist'])
        os.mkdir(artist_path)
        if tag_dict['album'] != "":
                ##---- if we have an aritst and an album----
            
            ##print(album_path)
            album_path = os.path.join(new_path, os.path.join(tag_dict['artist'], tag_dict['album']))
            os.mkdir(album_path)
                    ## copy_and_rename(album_path, file_path, dict)
                ## ----if we just have an artist but no album
        ##else:
                ## copy_and_rename(artist_path, file_path, dict) 

  


file_path = r'/Users/berglindliljabjornsdottir/Documents/python/ipod/F02/WKLF.mp3'
new_path = r'/Users/berglindliljabjornsdottir/Documents/python/stagger-test/copy-folder'

tag_dict = {'artist': 'Berglind', 'album': '', 'title': 'Fallinn með 4.9', 'track': '1'}
##print(os.getcwd()) to get path, takk fyrir ekkert mac


move_to_artist()

##tag = stagger.read_tag(file_path)
##print(tag.artist + "woo" + tag.album)
