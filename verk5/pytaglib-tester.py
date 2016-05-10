from pprint import pprint as pp
import taglib
import string
import eyed3
import os
from os import path as pa
from os.path import join as jo
from stagger import *


def test_pytaglib():

##
    a = r"C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\ipod"

    
    b = [x[0] for x in os.walk(a)]
    test_list = []

    for i in b:
        for j in os.listdir(i):
            curr_path = pa.join(i,j)
            if pa.isfile(curr_path) and curr_path.endswith('.mp3'):
                f = taglib.File(curr_path)
                try:
                    art = f.tags['ARTIST']
                except:
                    print('No artist in: \n' + curr_path)
                    
                try:
                    alb = f.tags['ALBUM']
                except:
                    print('No album in: \n' + curr_path)
                    
                try:
                    tit = f.tags['TITLE']
                except:
                    print('No title in: \n' + curr_path)
                    
                try:
                    tra = f.tags['TRACK']
                except:
                    print('No track in: \n' + curr_path)

                    
    return 5
##
##    f = taglib.File(a)
##    if f.tags['ARTIST'] == None:
##        pp(f.tags)


test_pytaglib()
