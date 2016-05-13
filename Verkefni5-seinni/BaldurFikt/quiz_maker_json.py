import json
import os
from os import path
from pprint import pprint as pp

def quiz_maker_2000():



    
    question_path = os.path.join(os.getcwd(), 'questions')
    answers_path = os.path.join(os.getcwd(), 'answers')
    
    q_files = sorted(os.listdir(question_path))
    a_files = sorted(os.listdir(answers_path))


    print(q_files)
    topics = []
    
    for i in q_files:
        topics.append(i.split(sep='-')[0])

    test_dict = {}
    
    for ind, top in enumerate(topics):
        a = open(os.path.join(question_path, q_files[ind]), 'r', encoding='utf-8')
        b = open(os.path.join(answers_path, a_files[ind]), 'r', encoding='utf-8')
        x = a.read().splitlines()
        y = b.read().splitlines()

        a.close()
        b.close()
        
        test_dict[top] = []
        for i in range( len(x) ):
            test_dict[top].append({ str( "q" + str(i+1) + "-question" ): str(x[i]) })
            test_dict[top].append({ str( "q" + str(i+1) + "-answer" ): str(y[i]) })

    abc = json.dumps(test_dict)

    json_writer = open('tester.json', 'w', encoding='utf-8')

    json_writer.write(abc)
    


                    
                
        
        

    
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

            
