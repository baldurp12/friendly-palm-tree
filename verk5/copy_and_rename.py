import os
import shutil
from shutil import copy2


final_path = r"C:\Users\Baldur\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\friendly-palm-tree\verk5\endFolder"

file_path = r"C:\Users\Baldur\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\friendly-palm-tree\verk5\fromFolder\text.txt"

tag_dict = {'artist': '', 'album': '', 'title': 'bALDUR', 'track': 999999999999999999999999999999999999999999999999999999999999999}




def copy_and_rename(final_path, file_path, tag_dict):

    old_file_name = os.path.split(file_path)[1]

    new_file_name = old_file_name ##if we dont do any changes to old_file_name we keep the name
    

    
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

 
    new_file_path = os.path.join(final_path, new_file_name)


    if os.path.isfile(new_file_path):
        print(new_file_name + ' ALREADY IN : \n' + final_path + '\n' 'OLD FILE NAME: ' + old_file_name)
    else:
        print('Copy to folder!')
        print (old_file_name + ' was changed to ' + new_file_name)
        copy2(file_path, new_file_path)
    

    
    return 5



        


copy_and_rename(final_path, file_path, tag_dict)
