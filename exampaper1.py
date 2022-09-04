import os,time
dict1 = {1: "Add a question", 2: "View",3:"Edit question",4:"Remove a question",5:"Save and Exit"}
titleText = "Welcome to chro MCQ question paper maker"
try: termColum = int(opers.get_terminal_size()[0])
except : termColum = 80
print(f'{"-"*int((termColum/2-len(titleText)/2))}{titleText}{"-"*int((termColum/2-len(titleText)/2))}')
paperTitle = input("Enter the title of your paper : ")
paperMultiples = int(input("Enter how many choices you want to give each paper: "))
negativeMarking = input("Enable negative marking?[yes/no]")
duration = int(input("Enter duration of test in minutes:"))
print()
questions = {}
mcq = {}
ans = {}
en = 0
alphas = list("abcdefghijklm")
def paperFormatter(strin):
    global negativeMarking
    with open(f"{strin}.py", "w") as f:
        f.write(f"import os as opers\ntry: termColum = int(opers.get_terminal_size()[0])\nexcept : termColum = 80 \nimport time\n")
        f.write("TimeStart = time.time()\n")
        f.write(f"questionsP = {questions}\nmcqP = {mcq}\nansP = {ans}\ntitleP = f'{paperTitle}'\nanswered = {{}}\n")
        f.write("print(f'{\"-\"*int((termColum/2-len(titleP)/2))}{titleP}{\"-\"*int((termColum/2-len(titleP)/2))}')\n")
        f.write(f"print(\"Number of questions : {len(mcq)}\")\n")
        f.write(f"print(\"Duration of test : {duration} mins\")\n")
        f.write(f"print('Paper created on {time.asctime(time.localtime())}')\n")
        f.write("for i,j in questionsP.items():\n\tif time.time()-TimeStart<="+str(int(duration*60))+":\n\t\tprint(f\"\\nQ{i}. {j}\")\n\t\tfor optionAlpha,seeOption in mcqP[i].items():\n\t\t\tprint(f\"	{optionAlpha}. {seeOption}\")\n\t\tanswerYour=input(\"Answer : \")\n\t\tanswered[i]=answerYour\n\telse:\n\t\tremaining_questions = len(ansP)-len(answered)\n\t\tfor answerLength in range(len(answered)+1,len(ansP)+1):\n\t\t\tanswered[answerLength]=\"null\"\n")
        if negativeMarking=="yes" or "Yes" or "YES":
            f.write("input('Test finished, Press enter to continue...')\ncorrectans = 0\nfor Qno,AnswerNo in ansP.items():\n\tif AnswerNo==answered[Qno]:\n\t\tprint(f'Q.{Qno} - correct.')\n\t\tcorrectans+=1\n\telse:\n\t\tprint(f'Q.{Qno} - wrong. Correct answer - {ansP[Qno]} , {mcqP[Qno][ansP[Qno]]}')\n\t\tcorrectans-=1\n")
        else:
            f.write(
                "input('Test finished, Press enter to continue...')\ncorrectans = 0\nfor Qno,AnswerNo in ansP.items():\n\tif AnswerNo==answered[Qno]:\n\t\tprint(f'Q.{Qno} - correct.')\n\t\tcorrectans+=1\n\telse:\n\t\tprint(f'Q.{Qno} - wrong. Correct answer - {ansP[Qno]} , {mcqP[Qno][ansP[Qno]]}')\n")
        f.write("print(f\"\\nYou scored {correctans} out of {len(ansP)}\")\ninput(\"Press enter to exit...\")")

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
        while True:
            ansEnter = input("Enter answer for this question (example: a ): ")
            if ansEnter in alphas[:paperMultiples]:
                ans.update({en: ansEnter})
                break
            else:
                print("Invalid option , try again")
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
        filename = input("Enter your file name to save : ").lower()
        paperFormatter(filename)
        input("Thanks for using me, please come back later...")
        exit()
    else:print("Invalid choice , enter again")