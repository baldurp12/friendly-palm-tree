import PTN
from pprint import pprint as pp
import os
from os import path
import glob
import shutil
import re


def torr_test():

    working_dir = os.walk(curr_dir)
##    working_fil = [os.path.join(curr_dir, x[2]) for x in working_dir]
    subdirs = [x[0] for x in working_dir]
    files = [os.path.join(curr_dir, f) for f in os.listdir(curr_dir) if os.path.isfile(os.path.join(curr_dir, f))]
##    print(files)
##    return 5
##    subdirs[5] = 'c:\mappa\sem\er\ekki\til'

##    TV_shows = os.path.join(working_dir, input())
    if os.path.isdir(TV_shows):
        pass
    else:
        os.mkdir(TV_shows)
    if os.path.isdir(movies):
        pass
    else:
        os.mkdir(movies) 
##    
##
        
    ### checking and moving folders ##
    for i in subdirs[1:]:
##        print(i, 'Is being tested')
        if os.path.isdir(i) and contains_tv_show(i):
##            print('ooa')
##            break
##            print(i, 'Is a TV show')
            shutil.move(i, TV_shows)
        elif os.path.isdir(i) and is_a_movie_perhaps(i):
            print(i, ' IS A MOVIE (perhaps)')
            shutil.move(i, movies)

    for j in files:
        if contains_tv_show(j):
            shutil.move(j, TV_shows)
##            print('Moving the tv show: ', j)
        elif is_a_movie_perhaps(j):
            shutil.move(j, movies)
##            print('Moving the movie: ', j)
            
    ### sorting tv_shows by title ###

    #tv_Folder = [x[0] for x in os.walk(TV_shows)]
    

##            
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
    
    if os.path.isdir(in_path):
        sub_list = [x[2] for x in os.walk(in_path)]
        for i in sub_list:
    ##        print(i, 'hmmmmm...')
            if 'episode' in PTN.parse(str(i)).keys():
                return True
        return False

    if os.path.isfile(in_path):
        if 'episode' in PTN.parse(str(in_path)).keys():
            return True
        else:
            return False

def is_a_movie_perhaps(in_path):

    if os.path.isdir(in_path):
        #print('tipi')
        sub_list = [x[2] for x in os.walk(in_path)]
        ##print(sub_list)
        for i in sub_list:
            for j in i:
                if str(j).lower().endswith(movie_tuple):
                    #print('noiiiijsss')
                    return True
        return False

    if os.path.isfile(in_path):
        if str(in_path).lower().endswith(movie_tuple):
            #print('noiiiijsss')
            return True
    return False
    


TV_shows = r'C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\test_folder\00TV_shows'
movies = r'C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\test_folder\00Movie_shows'
curr_dir = r"C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\test_folder"

movie_tuple = ('.webm', '.mkv', '.flv', '.vob', '.ogv', '.ogg', '.drc', '.mng', '.avi', '.mov',
            '.qt', '.wmv', '.yuv', '.rm', '.rmvb', '.asf', '.mp4', '.m4p', '.m4v', '.mpg',
            '.mp2', '.mpeg', '.mpe', '.mpv','.mpg', '.mpeg', '.m2v', '.m4v','.3gp' ,'.3g2')



torr_test()
