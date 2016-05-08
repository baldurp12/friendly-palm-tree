import PTN
from pprint import pprint as pp
import os
import shutil




def etst():
    info = PTN.parse("30 Rock [1.02] The Aftermath")
    pp(info)
    if 'episode' in info.keys():
        print('Þetta er líklega þáttur maffakka')

etst()
