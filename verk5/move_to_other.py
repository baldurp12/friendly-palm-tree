import os
import shutil

copy_folder = r'file_path = r"C:\Users\Baldur\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\ipod\00_copy_folder'
other_folder = '00_Other'

def move_to_other(): ##file_path, tag_dict
    
    ##----album er tomt----##

    if tag_dict['album'] == '':
        print("ekki album")
        new_path = os.path.join(os.getcwd(), other_folder)

        print('Sending ' + os.path.split(file_path)[1] + '\n'
            'To: ' + new_path + '\n')
    ##        copy_and_rename(new_path, file_path, tag_dict)
    
    else:
        album_path = os.path.join( os.path.join(os.getcwd,other_folder) , tag_dict['album'])

        print('Making: ' + album_path)
        try:
            os.mkdir(album_path)
        except:
            print('Cannot make folder: ' + album_path)
        ##print(album_path)
        ##copy_and_rename(album_path, file_path, dict)




tag_dict = {'artist' : '', 'album': 'love and peace', 'title': '- . - _'}

file_path = r"C:\Users\Baldur\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\ipod\F02\WKLF.mp3"
##file_path = r'/Users/berglindliljabjornsdottir/Documents/python/ipod/F02/WKLF.mp3'
##new_path = r'/Users/berglindliljabjornsdottir/Documents/python/stagger-test/copy-folder/00trash'

move_to_other()
