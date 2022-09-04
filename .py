import os as opers
try: termColum = int(opers.get_terminal_size()[0])
except : termColum = 80 
import time
TimeStart = time.time()
questionsP = {1: 'Who is Cs?', 2: 'Who is pm of India?', 3: '1', 4: 'Bro'}
mcqP = {1: {'a': 'ComputerScience', 'b': 'Chandrashekar', 'c': 'N. chandrasekar'}, 2: {'a': 'Modi ji', 'b': 'Rahul Gandhi', 'c': 'Gandhi g'}, 3: {'a': 'Who is ceo of infosus', 'b': '1', 'c': 'Int'}, 4: {'a': 'brother', 'b': 'sister', 'c': 'uncle'}}
ansP = {1: 'b', 2: 'a', 3: 'b', 4: 'a'}
titleP = f'Some basic concept'
answered = {}
print(f'{"-"*int((termColum/2-len(titleP)/2))}{titleP}{"-"*int((termColum/2-len(titleP)/2))}')
print("Number of questions : 4")
print("Duration of test : 1 mins")
print('Paper created on Sat Sep  3 21:29:51 2022')
for i,j in questionsP.items():
	if time.time()-TimeStart<=60:
		print(f"\nQ{i}. {j}")
		for optionAlpha,seeOption in mcqP[i].items():
			print(f"	{optionAlpha}. {seeOption}")
		answerYour=input("Answer : ")
		answered[i]=answerYour
	else:
		remaining_questions = len(ansP)-len(answered)
		for answerLength in range(len(answered)+1,len(ansP)+1):
			answered[answerLength]="null"
input('Test finished, Press enter to continue...')
correctans = 0
for Qno,AnswerNo in ansP.items():
	if AnswerNo==answered[Qno]:
		print(f'Q.{Qno} - correct.')
		correctans+=1
	else:
		print(f'Q.{Qno} - wrong. Correct answer - {ansP[Qno]} , {mcqP[Qno][ansP[Qno]]}')
		correctans-=1
print(f"\nYou scored {correctans} out of {len(ansP)}")
input("Press enter to exit...")