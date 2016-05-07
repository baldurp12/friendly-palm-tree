import PTN
from pprint import pprint as pp
import os
import shutil




def etst():
    info = PTN.parse('[ www.TorrentDay.com ] - Spy.2011.S02E04.HDTV.XviD-AFG')
    pp(info)
    if 'episode' in info.keys():
        print('Þetta er líklega þáttur maffakka')

etst()
