import json
import os
from os import path
from pprint import pprint as pp

spurningar = r"C:\Users\baldur\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\friendly-palm-tree\verk5\stora-verk\animal-spurningar.txt"
svor = r"C:\Users\baldur\Dropbox\Bs.C-Hugb\4.önn\PRAL\verk4\friendly-palm-tree\verk5\stora-verk\animal-svör.txt"


def quiz_maker_2000():
    a = open(spurningar, 'r', encoding='utf-8')
    b = open(svor, 'r', encoding='utf-8')


    topic = "animals"
    
    x = a.read().splitlines()
    y = b.read().splitlines()

    test_dict = {topic: []}

    
    for i in range( len(x) ):
        test_dict[topic].append({ str( "q" + str(i+1) + "-question" ): str(x[i]) })
        test_dict[topic].append({ str( "q" + str(i+1) + "-answer" ): str(y[i]) })

    abc = json.dumps(test_dict)
    


    c = open('tester.json', 'w', encoding='utf-8')

    c.write(abc)
    print(json.loads(abc))



    

    
    

        
quiz_maker_2000()

            
