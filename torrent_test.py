import PTN
from pprint import pprint as pp
import os
from os import path
import glob
import shutil
import re
import string


def torr_test():

    working_dir = os.walk(curr_dir)

    subdirs = [x[0] for x in working_dir]
    files = [os.path.join(curr_dir, f) for f in os.listdir(curr_dir) if os.path.isfile(os.path.join(curr_dir, f))]



    if os.path.isdir(TV_shows):
        pass
    else:
        try:
            os.mkdir(TV_shows)
        except:
            print('mkdir: ' + TV_shows + '  failed !') 
    if os.path.isdir(movies):
        pass
    else:
        try:
            os.mkdir(movies)
        except:
            print('mkdir: ' + TV_shows + '  failed !') 

        
    ### checking and moving folders ##
    for i in subdirs[1:]:
        if os.path.isdir(i) and contains_tv_show(i):
            try:
                shutil.move(i, TV_shows)
            except:
                print('Error when trying to move: ' + i + '\n' + 'To: ' + TV_shows)
        elif os.path.isdir(i) and is_a_movie_perhaps(i):
            try:
                shutil.move(i, movies)
            except:
                print('Error when trying to move: ' + i + '\n' + 'To: ' + movies)
    for j in files:
        if contains_tv_show(j):
            try:
                shutil.move(j, TV_shows)
            except:
                print('Error when trying to move: ' + j + '\n' + 'To: ' + TV_shows)
        elif is_a_movie_perhaps(j):
            try:
                shutil.move(j, movies)
            except:
                print('Error when trying to move: ' + j + '\n' + 'To: ' + movies)


       
    ### sorting tv_shows by title ###
    sort_file_list = [f for f in os.listdir(TV_shows) if os.path.isfile(os.path.join(TV_shows, f))]

    folder_list = []
    for i in sort_file_list:

        x = PTN.parse(str(i))
        
        if any(invalid_char in set(string.punctuation) for invalid_char in str(x['title'])):
            print(x['title'], ' Not a valid name for title')
        else:
            folder_list.append(x['title'].lower())
            
    for i in set(folder_list):
        if (len(i) > 2 and os.path.isdir(os.path.join(TV_shows, i)) == False):
            try:
                os.mkdir(os.path.join(TV_shows, i))
            except:
                print('Error when trying to make folder: ' + os.path.join(TV_shows, i))

##    love_peace = [y[0] for y in os.walk(TV_shows)]
  
####    ### moving files to folders ###
            
##    love_peace = [y[0] for y in os.walk(TV_shows)]
##    for i in love_peace[1:]:
##        for j in [y[2] for y in os.walk(i)][:1]:
##            for k in j:
##                if os.path.isfile(os.path.join(i,k)) and check_title(k) and str(k).lower().endswith(movie_tuple):
##                    try:
####                        print("Im now moving: " + os.path.join(i,k) + '\n' + "To the: " + os.path.join(TV_shows, PTN.parse(str(k).lower())['title']) + ' folder')
####                        print(os.path.join(TV_shows, PTN.parse(str(k).lower())['title']))
##                        if os.path.isdir(os.path.join(TV_shows, PTN.parse(str(k).lower())['title'])):
##                            shutil.move(os.path.join(i,k), os.path.join(TV_shows, PTN.parse(str(k).lower())['title']))
##                        else:
##                            os.mkdir(os.path.join(TV_shows, PTN.parse(str(k).lower())['title']))
##                            shutil.move(os.path.join(i,k), os.path.join(TV_shows, PTN.parse(str(k).lower())['title']))
##                    except:
##                        print('Slight error')
##                    else:
##                        pass
####                    print("Im now moving: " + os.path.join(i,k) + '\n' + "To the: " + PTN.parse(k)['title'] + ' folder')


    ### Make TV_trash ###
    tv_folders = [y[0] for y in os.walk(TV_shows)]
    for i in tv_folders[1:]:
##        print(i, 'Is being tested')
        if os.path.isdir(i) and (contains_movie_files(i) == False):
##            print(i, 'Is a TV show')
            try:
                shutil.move(i, TV_trash)
            except:
                print('Failed to move' + i + '\n To: ' + TV_trash)

    ### Make movie_trash ###
    movie_folders = [g[0] for g in os.walk(movies)]
    for i in movie_folders[1:]:
##        print(i, 'Is being tested')
        if os.path.isdir(i) and (contains_movie_files(i) == False):
##            print(i, 'Is a TV show')
            try:
                shutil.move(i, movie_trash)
            except:
                print('Failed to move' + i + '\n To: ' + movie_trash)

##    for dirpath, dirnames, filenames in os.walk(TV_shows):
##        for i in filenames:
##        print('checking', filenames)
##        if os.path.isfile(os.path.join(dirpath, filenames)) and check_title(filenames):
##            print(PTN.parse(filenames)['title'])
##            ##shutil.move(i, TV_shows)
    
            
def check_title(in_path):
    x = PTN.parse(str(in_path))
        
    if any(invalid_char in set(string.punctuation) for invalid_char in str(x['title'])):
        #print(x['title'], ' Not a valid name for title')
        return False
    else:
        return True


                
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

def contains_movie_files(in_path):
    if os.path.isdir(in_path):
        sub_list = [x[2] for x in os.walk(in_path)]
        ##print(sub_list)
        for i in sub_list:
            for j in i:
                if str(j).lower().endswith(movie_tuple):
                    return True
        return False


TV_shows = r'C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\test_folder\00TV_shows'
movies = r'C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\test_folder\00Movie_shows'

curr_dir = r"C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\test_folder"

TV_trash = r'C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\test_folder\00TV_shows\trash'
movie_trash = r'C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\test_folder\00Movie_shows\trash'

movie_tuple = ('.webm', '.mkv', '.flv', '.vob', '.ogv', '.ogg', '.drc', '.mng', '.avi', '.mov',
            '.qt', '.wmv', '.yuv', '.rm', '.rmvb', '.asf', '.mp4', '.m4p', '.m4v', '.mpg',
            '.mp2', '.mpeg', '.mpe', '.mpv','.mpg', '.mpeg', '.m2v', '.m4v','.3gp' ,'.3g2')



torr_test()
