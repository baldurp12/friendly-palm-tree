import json
import os
from os import path
from pprint import pprint as pp

def quiz_maker_2000():


    question_path = os.path.join(os.getcwd(), 'questions')
    answers_path = os.path.join(os.getcwd(), 'answers')
    
    q_files = sorted(os.listdir(question_path))
    a_files = sorted(os.listdir(answers_path))


##    print(q_files)

    topics = []
   
    for i in q_files:
        topics.append(i.split(sep='-')[0])

    q_a_dict = {}
    
    for index, top in enumerate(topics):
        a = open(os.path.join(question_path, q_files[index]), 'r', encoding='utf-8')
        b = open(os.path.join(answers_path, a_files[index]), 'r', encoding='utf-8')
        x = a.read().splitlines()
        y = b.read().splitlines()

        a.close()
        b.close()
        
        temp_dict = {}

        for i in range( len(x) ): ## len(x) ætti að vera == len(y)
            
            temp_dict[str('question' + str(i+1).zfill(2))] = str(x[i])
            temp_dict[str('answer' + str(i+1).zfill(2))] = str(y[i])

        q_a_dict[top] = temp_dict

    with open("QandA.json", "w", encoding='utf_8') as js:
        json.dump(q_a_dict,js, indent=4, sort_keys=True)
            
        
##        test_dict[top] = []
##        for i in range( len(x) ):
##            test_dict[top].append({ str( "question"+ str(i+1)): str(x[i]) })
##            test_dict[top].append({ str( "answer" + str(i+1)): str(y[i]) })
##
##    abc = json.dumps(test_dict)
##
##    json_writer = open('tester.json', 'w', encoding='utf-8')
##
##    json_writer.write(abc)
##
##    
####    print(sorted(topics) == sorted(list(test_dict.keys())))
##
##    print(test_dict['animal'][3])
##    print(test_dict[   sorted(list(test_dict.keys()))[0]   ]   [1]['answer1']   ) 
    

        
quiz_maker_2000()

            
