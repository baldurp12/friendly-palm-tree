import PTN
from pprint import pprint as pp
import os
import shutil


def torr_test():

    working_dir = os.walk(os.path.join(os.getcwd(), 'test_folder'))
    subdirs = [x[0] for x in working_dir]
##    pp(subdirs)
##
##    subdirs[5] = 'c:\mappa\sem\er\ekki\til'

##    TV_shows = os.path.join(working_dir, input())
    if os.path.isdir(TV_shows):
        pass
    else:
        os.mkdir(TV_shows)
##    
##    
    for i in subdirs[1:]:
        if os.path.isdir(i) and contains_tv_show(i):
##            print(i,'oooooooyeaaaa')
##            break
            shutil.move(i, TV_shows)
            
##shutil.move(i, TV_shows)
##        
##
##        
##    pp(subdirs[0:10])
    
##    info = PTN.parse(r'C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\test_folder\Season 4')
##    pp(info)
##    if 'episode' in info.keys():
##        print('Þetta er líklega þáttur maffakka')
##    
##
##  if os.path.isdir(i):
##            return contains_tv_show(i)
##
                
def contains_tv_show(in_path):
    sub_list = [x[2] for x in os.walk(in_path)]
    for i in sub_list[1:]:
        if 'episode' or 'season' in PTN.parse(str(i)).keys():
            return True
    return False
##    if sub_list == []:
##        return False
##    else:
##        return True

##    isinstance(
##        any(
##    any([1, 2, 'joe'], lambda e: isinstance(e, int) and e > 0)
##    info = PTN.parse()
##    if 'episode' in info.keys():
##        return True
##    
    
        
    
    


TV_shows = r'C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\test_folder\asdf'


torr_test()
