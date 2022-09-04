import os as opers
termColum = int(opers.get_terminal_size()[0])
questionsP = {1: 'Akshata', 2: 'nayana'}
mcqP = {1: {'a': 'maths teacher', 'b': 'pacchi', 'c': 'book'}, 2: {'a': 'pacchi', 'b': 'mov', 'c': 'dolo'}}
ansP = {1: 'b', 2: 'a'}
titleP = f'This js tiele'
answered = {}
print(f'{"-"*int((termColum/2-len(titleP)/2))}{titleP}{"-"*int((termColum/2-len(titleP)/2))}')
print('Paper created on Sun Aug  7 07:38:17 2022')
for i,j in questionsP.items():
	print(i,j)