import PTN
from pprint import pprint as pp
import os
import shutil




def etst():
    info = PTN.parse(''.join("Arrested Development - S2 E 01 - The One Where Michael Leaves").replace(' ', ''))
    pp(info)
    if 'episode' in info.keys():
        print('Þetta er líklega þáttur maffakka')

etst()
