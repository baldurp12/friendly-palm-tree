import os
import shutil

copy_folder = '00_copy_folder'
other_folder = '00_Other'

def move_to_other(file_path, tag_dict): ##file_path, tag_dict
    
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

##        copy_and_rename(new_path, file_path, tag_dict)



tag_dict = {'artist' : '', 'album': 'love and peace', 'title': '- . - _', 'track': 'Feel the bern'}

file_path = r"C:\Users\Baldur\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\ipod\F02\WKLF.mp3"  #### WINDOWS 
##file_path = r'/Users/berglindliljabjornsdottir/Documents/python/ipod/F02/WKLF.mp3' #### MAC OS X
##new_path = r'/Users/berglindliljabjornsdottir/Documents/python/stagger-test/copy-folder/00trash'

move_to_other(file_path, tag_dict)
