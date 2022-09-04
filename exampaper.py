import os,time
dict1 = {1: "Add a question", 2: "View",3:"Edit question",4:"Remove a question",5:"Save anx Exit"}
print("                    Welcome to Samarth Pai paper analyzer")
paperTitle = input("Enter the title of your paper : ")
paperMultiples = int(input("Enter how many choices you want to give each paper: "))
print()
questions = {}
mcq = {}
ans = {}
en = 0
alphas = list("abcdefghijklm")

def paperFormatter(strin):
    terminalColumns = int(os.get_terminal_size()[0])
    with open(f"{strin}.py", "w") as f:
        f.write(f"import os as opers\ntermColum = int(opers.get_terminal_size()[0])\nimport time\n")
        f.write("TimeStart = time.time()")
        f.write(f"questionsP = {questions}\nmcqP = {mcq}\nansP = {ans}\ntitleP = f'{paperTitle}'\nanswered = {{}}\n")
        f.write("print(f'{\"-\"*int((termColum/2-len(titleP)/2))}{titleP}{\"-\"*int((termColum/2-len(titleP)/2))}')\n")
        f.write(f"print('Paper created on {time.asctime(time.localtime())}')\n")
        f.write(f"for en,i,j in enumerate(quetionsP.items()):\n\tprint(en,i,j)")
        
def viewer():
    for i, q in questions.items():
        print(f"\nQ{i}. {q}")
        for options,valueOptions in mcq[i].items():
            print(f"\t{options}. {valueOptions} ")
        print(f"\tAnswer : {ans[i]}")

def quetionEditor(intQuest):
    whatToEdit = {1:"Question statement",2:"Options",3:"Answer of a question"}
    print("What do you wan to edit?")
    for i,j in whatToEdit.items():
        print(f"Enter {i} to edit {j}")
    whatYouWant = int(input("Enter a command : "))
    if whatYouWant==1:
        questionStament = input("Enter new quetion Statement : ")
        questions[intQuest] = questionStament
        print("Successfully changed the quetion statement")
    if whatYouWant==2:
        for i in range(paperMultiples):
            enterMcq = input(f"Enter choice {alphas[i]}: ")
            mcq[intQuest].update({alphas[i]: enterMcq})
            print(mcq)
    if whatYouWant==3:
        answerStatement = input("Enter correct answer : ")
        ans[intQuest]=answerStatement

while 1:
    en += 1
    print()
    for key, value in dict1.items():
        print(f"Enter {key} to {value}")
    choice = int(input("Enter your command : "))
    print()
    if choice == 1:
        quest = input(f"Enter question no.{en} : ")
        print()
        questions[en] = quest
        mcq[en] = dict()
        for i in range(paperMultiples):
            enterMcq = input(f"Enter choice {alphas[i]}: ")
            mcq[en].update({alphas[i]: enterMcq})
            print(mcq)
        ansEnter = input("Enter answer for this question (example: a ): ")
        ans.update({en: ansEnter})
        print(questions)
        print(mcq)
        print(ans)
    elif choice == 2:
        viewer()
        en -= 1
        
    elif choice == 3:
        whichQuestion = int(input("Enter which question no. do you want to edit: "))
        quetionEditor(whichQuestion)
        en-=1
        
    elif choice == 4:
        delQuestion = int(input("Enter the question no. you want to delete : "))
        questions.pop(delQuestion)
        mcq.pop(delQuestion)
        ans.pop(delQuestion)
        questions = dict(zip(range(1,len(ans)+1),questions.values()))
        ans = dict(zip(range(1,len(ans)+1),ans.values()))
        mcq = dict(zip(range(1,len(ans)+1),mcq.values()))
    elif choice==5:
        filename = input("Enter your file name to save").lower()
        paperFormatter(filename)
    else:print("Invalid choice , enter again")