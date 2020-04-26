#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia':
'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.
for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile=open(r'C:\Users\69421\Desktop\python\quizfiles\captialquiz%s.txt'\
              %(quizNum+1),'w')
    keyFile=open(r'C:\Users\69421\Desktop\python\quizfiles\captialkey%s.txt'\
              %(quizNum+1),'w')
    quizFile.write(' '*100+'Geography Quiz\n')
    quizFile.write(' '*75+'Name:_____'+' '*40+'Class:_____')
    quizFile.write('\n\n')
    

    # Shuffle the order of the states.
    states=list(capitals.keys())
    random.shuffle(states)

    # Write 50 different questions.
    for Qnum in range(50):
        quizFile.write('%s. What\'s the captial of %s?\n'%(Qnum+1,states[Qnum]))
        # Write wrong options.
        wronganswers=list(capitals.values())
        del wronganswers[wronganswers.index(capitals[states[Qnum]])]
        ordered_answer=random.sample(wronganswers,3)
        # Write correct options.
        ordered_answer.append(capitals[states[Qnum]])
        # Shuffle the order of the options.
        random.shuffle(ordered_answer)
        orders='ABCD'
        
        for i in range(4):
            quizFile.write('    %s. %s\n'%(orders[i],ordered_answer[i]))
        quizFile.write('\n')

        # Find correct orders.
        order=orders[ordered_answer.index(capitals[states[Qnum]])]
        # Write correct answers.
        keyFile.write('%s. %s\n'%(Qnum+1,order))

    keyFile.close()
    quizFile.close()

















