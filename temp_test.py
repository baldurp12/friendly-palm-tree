import PTN
from pprint import pprint as pp
import os
import shutil




def etst():
    info = PTN.parse(r"C:\Users\baldu\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\test_folder\Big Bang Theory\Season.06\The.Big.Bang.Theory.S06E01.HDTV.x264-LOL.mp4")
    pp(info)
    if 'episode' in info.keys():
        print('Þetta er líklega þáttur maffakka')

etst()
