import os
from pprint import pprint as pp
import PTN
import string


movie_tuple = ('.webm', '.mkv', '.flv', '.vob', '.ogv', '.ogg', '.drc', '.mng', '.avi', '.mov',
            '.qt', '.wmv', '.yuv', '.rm', '.rmvb', '.asf', '.mp4', '.m4p', '.m4v', '.mpg',
            '.mp2', '.mpeg', '.mpe', '.mpv','.mpg', '.mpeg', '.m2v', '.m4v','.3gp' ,'.3g2')

sub_list = ['First Read This Guide.txt', 'spy.2011.s01e02.hdtv.xvid-tla.avi', 'spy.2011.s01e02.hdtv.xvid-tla.nfo', 'www.Torrentday.com.txt']


TV_shows = r'C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\test_folder\00TV_shows'
movies = r'C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\test_folder\00Movie_shows'
curr_dir = r"C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\test_folder"

movie_tuple = ('.webm', '.mkv', '.flv', '.vob', '.ogv', '.ogg', '.drc', '.mng', '.avi', '.mov',
            '.qt', '.wmv', '.yuv', '.rm', '.rmvb', '.asf', '.mp4', '.m4p', '.m4v', '.mpg',
            '.mp2', '.mpeg', '.mpe', '.mpv','.mpg', '.mpeg', '.m2v', '.m4v','.3gp' ,'.3g2')

##files = [os.path.join(TV_shows, f) for f in os.listdir(TV_shows) if os.path.isfile(os.path.join(TV_shows, f))]
files = [f for f in os.listdir(TV_shows) if os.path.isfile(os.path.join(TV_shows, f))]

##
##def list_dir_test():
##
##    x = os.scandir(r"C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\test_folder")
##    pp(x)
##
##    
##
##
##list_dir_test()
##

##def print_PTN():
##    
##    x = PTN.parse(r'C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\test_folder\00TV_shows\The Unbelievable Truth S10E02.mp3')
##
##    if any(invalid_char in set(string.punctuation) for invalid_char in x['title']):
##        print(x['title'], ' Not a valid name for title')
##
##print_PTN()

##def tuple_test():
##   for i in sub_list:
##        #print(i)
##        if str(i).lower().endswith(movie_tuple):
##            print('nojjjjs')




##
##def title_test():
##
##    for i in files:
##        get_title(i)

##title_test()

##def get_title(in_path):
##
##        x = PTN.parse(str(in_path))
####        print(x)
##        
##        if any(invalid_char in set(string.punctuation) for invalid_char in str(x['title'])):
##            print(x['title'], ' Not a valid name for title')
##        else:
##            print(x['title'], 'Wow, what a name for a title, you are so sexy and funny, hahaha!')
##
##title_test()
##    
####
##
##def file_parse_shit():
##    x = [y[0] for y in os.walk(TV_shows)]
##
##    listi_a = []
##
##    for i in x[1:]:
##        for j in [y[2] for y in os.walk(i)]:
##            for k in j:
####                print('Folder: ' + i +  '\n' + 'File: ' + k)
####                listi_a.append(os.path.isfile(os.path.join(i,k)))
##                
####                listi_a.append(os.path.join(i,k))
####    pp(listi_a)
##
##file_parse_shit()
##
##




