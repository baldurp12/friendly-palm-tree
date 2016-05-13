import stagger
from stagger import *
from pprint import pprint as pp

file_path = r"C:\Users\Baldur\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\ipod\F38\YUQY.mp3"

def stagger_test():

##
##    
##    b = [x[0] for x in os.walk(a)]
##    test_list = []
##
##    for i in b:
##        for j in os.listdir(i):
##            curr_path = pa.join(i,j)
##            if pa.isfile(curr_path) and curr_path.endswith('.mp3'):
##                f = taglib.File(curr_path)
##                pp(f.tags)
##
##    

    
    tag_dict = {}
    try:
        tag = stagger.read_tag(file_path)
        tag_dict['artist'] = (''.join(x for x in tag.artist if x not in ',<>:"/\\|?*\'')).strip() or ''
        tag_dict['title'] = (''.join(y for y in tag.title if y not in ',<>:"/\\|?*\'')).strip() or ''
        tag_dict['album'] = (''.join(z for z in tag.album if z not in ',<>:"/\\|?*\'')).strip() or ''
        tag_dict['track'] = tag.track or 0
    except:
        print('failed')
        tag_dict = {'artist': '', 'album': '', 'title': '', 'track': 0} ## If stagger can't read the ID3, we put placeholders in the values we need

    if tag_dict['track'] == '':
        print('wat')
    
    print(tag_dict['artist'])
    print(tag_dict['title'])
    print(tag_dict['album'])
    print(tag_dict['track'])



stagger_test()
##
##testString = 'Badlur'
##
##def testtest():
##    global testString
##    testString =  'Ekkitil'
##
##
##def second():
##    print(testString)
##
##testtest()
##second()
##        

    
