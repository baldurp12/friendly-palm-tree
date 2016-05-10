import os
import shutil


def move_to_other(file_path, tag_dict):
    
    copy_path = os.path.join(os.getcwd(), 'copy_folder')

    if os.path.isdir(copy_path):
        pass
    else:
        os.mkdir(copy_path)
      
    if tag_dict['album'] == '':
        print(r'final_path = copy_folder/other/')
    
    else:
        try:
            print(r' trying to make album folder in copy_folder/other')
            print(r'final_path = copy_folder/other/album/')
        except:
            print(r'Makeing the album folder failed')
        


##    copy_and_rename(final_path, file_path, dict)




dick = {'artist' : '', 'album': 'love and peace', 'title': '- . - _'}

move_to_other('jon', dick)
