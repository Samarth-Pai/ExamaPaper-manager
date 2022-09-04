import os as opers
try: termColum = int(opers.get_terminal_size()[0])
except : termColum = 80 
import time
TimeStart = time.time()
questionsP = {1: 'What is the value of 1 mol', 2: 'What is gram molecular mass?', 3: 'Who is the founder of infosus'}
mcqP = {1: {'a': '1.698 × 10²³', 'b': '1.6022 × 10²³'}, 2: {'a': 'Molar mass ', 'b': 'Empiracal formula mass'}, 3: {'a': 'Narayan murthi', 'b': 'Satya nadella'}}
ansP = {1: 'b', 2: 'a', 3: 'a'}
titleP = f'Tgis is exam'
answered = {}
print(f'{"-"*int((termColum/2-len(titleP)/2))}{titleP}{"-"*int((termColum/2-len(titleP)/2))}')
print("Number of questions : 3")
print("Duration of test : 30 mins")
print('Paper created on Sat Sep  3 21:24:57 2022')
for i,j in questionsP.items():
	if time.time()-TimeStart<=1800:
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