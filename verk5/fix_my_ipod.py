import os
from os import path as pa
from os.path import join as jo
from stagger import *
def list_dir_test():
    a = [x[0] for x in os.walk(os.getcwd())]
    test_list = []
    for i in a[1:]:
        for j in os.listdir(i):
            curr_path = pa.join(i,j)
            if pa.isfile(curr_path) and j.endswith('.mp3'):
                try:
                    tag = stagger.read_tag(curr_path)
                    test_list.append(tag.artist)
                except:
                    print(curr_path)

    print(set(test_list))
    
        
        


list_dir_test()
