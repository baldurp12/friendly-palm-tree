import json
import os
from os import path
from pprint import pprint as pp

def quiz_maker_2000():


    q_fold = sorted(os.listdir(os.path.join(os.getcwd(), 'questions')))
    a_fold = sorted(os.listdir(os.path.join(os.getcwd(), 'answers')))

    print(q_fold)

    topics = []
    for i in q_fold:
        topics.append(i.split(sep='-'))
        
    print(topics)
    
##    a = open(spurningar, 'r', encoding='utf-8')
##    b = open(svor, 'r', encoding='utf-8')
##
##
##    json_writer = open('tester.json', 'a', encoding='utf-8')
##
##    
##
##    
##    x = a.read().splitlines()
##    y = b.read().splitlines()
##
##    
##    test_dict = {topic: []}
##
##    
##    for i in range( len(x) ):
##        test_dict[topic].append({ str( "q" + str(i+1) + "-question" ): str(x[i]) })
##        test_dict[topic].append({ str( "q" + str(i+1) + "-answer" ): str(y[i]) })
##
##    abc = json.dumps(test_dict)
##    
##
##
##    
##
##    c.write(abc)
##    print(json.loads(abc))



        
quiz_maker_2000()

            
