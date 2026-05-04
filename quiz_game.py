import time
from colorama import Fore , Style

questions = [
    {
        "question": "What is the capital city of U.S.A. ?",
        "options": ["i) California", "ii) Washington D.C.", "iii) New York", "iv) Texas"],
        "answers": ["ii", "washington d.c.", "ii."]
    },
    {
        "question": "Who invented the number Zero ?",
        "options": ["i) Aarush Bhatt", "ii) Christoper Waramanrty", "iii) Xia lao", "iv) Arya Bhatt"],
        "answers": ["iv", "arya bhatt", "iv."]
    },
    {
        "question": "Odd one out: 8, 27, 64, 100, 125",
        "options": ["i) 8", "ii) 27", "iii) 100", "iv) 125"],
        "answers": ["iii", "100", "iii."]
    },
    {
        "question": "What is the capital of Bhutan ?",
        "options": ["i) Laos", "ii) Taiaga", "iii) Jinping", "iv) Thimpu"],
        "answers": ["iv", "thimpu", "iv."]
    },
    {
        "question": "Find the missing number: 3, 6, 11, 18, 27, __ ?",
        "options": ["i) 36", "ii) 38", "iii) 40", "iv) 42"],
        "answers": ["ii", "38", "ii."]
    },
    {
        "question": "What is the only continent that's on all 4 hemispheres?",
        "options": ["i) Africa", "ii) Asia", "iii) Australia", "iv) South America"],
        "answers": ["i", "africa", "i."]
    },
    {
        "question": "What is the study of knowledge called ?",
        "options": ["i) Aerobics", "ii) Einsteinology", "iii) Epistemology", "iv) Entomology"],
        "answers": ["iii", "epistemology", "iii."]
    },
    {
        "question": "What is the distance between the two rails of a railway track called ?",
        "options": ["i) Seal gauge", "ii) Track guage", "iii) Ammeter", "iv) Railometer"],
        "answers": ["ii", "track gauage", "ii."]
    },
    {
        "question": "What is the first phase of mitosis ?",
        "options": ["i) Anaphase", "ii) Prephase", "iii) Telophase", "iv) Prophase"],
        "answers": ["iv", "prophase", "iv."]
    },
    {
        "question": "What is the world's tallest statue ?",
        "options": ["i) Statue of Buddha", "ii) Statue of Unity", "iii) Statue of Liberty", "iv) Statue of Gengis Khan"],
        "answers": ["ii", "statue of unity", "ii."] 
    },

]

bonus_question = {
        "question": "Who is the artist of 'Love Me Not' Song ?",
        "options": ["i) Jude Daniver", "ii) Ravyn Lenae", "iii) Christ Martin", "iv) Deniver"],
        "answers": ["ii", "ranvyn lenae", "ii."]
    }

#Starting Interface
time.sleep(1)
print(Fore.CYAN + "Quiz Game".center(20, '-') + Style.RESET_ALL)
time.sleep(1)
print(Fore.LIGHTWHITE_EX + "10 questions".center(20, '-') + Style.RESET_ALL)
time.sleep(1.75)
print(Fore.LIGHTYELLOW_EX + "*Type P to play and E to exit*" + Style.RESET_ALL)

while True:
    time.sleep(0.75)
    play_button = input("Enter: ").lower()
    if play_button == "p":
        break
    elif play_button == "e":
        exit()
    else:
        time.sleep(0.5)
        print(Fore.RED + "Wrong input [Type P or E]" + Style.RESET_ALL)  

def end(sc, qu):
    time.sleep(2)
    print(Fore.CYAN + "Processing..." + Style.RESET_ALL)
    time.sleep(3)
    print(Fore.CYAN + "Almost There..." + Style.RESET_ALL)

    time.sleep(3)
    print(Fore.YELLOW + f"You got {sc} out of {len(qu)} questions correct!" + Style.RESET_ALL)
    time.sleep(2)
    print(Fore.YELLOW + f"Score: {(sc / len(qu))*100}%" + Style.RESET_ALL)
    time.sleep(2)
    print(Fore.CYAN + "Thank you for playing this game.\n\n" + Style.RESET_ALL)
    time.sleep(1.5)
    print(Fore.LIGHTCYAN_EX + "Bye".center(25, "-") + Style.RESET_ALL)
    time.sleep(1.5)
    exit()

def ratefunc():
        print(Fore.CYAN + "How much would you like to rate my game 🙂 ?")
        time.sleep(1)
        print(Fore.LIGHTCYAN_EX + "Rating: 0-5 Stars")
        while True:
            time.sleep(0.25)
            rate = input("Rate: ")
            time.sleep(0.25)
            if rate == "5":
                print(Fore.GREEN + "Omgg Yayayy!!" + Style.RESET_ALL)
                break
            elif rate == "4":
                time.sleep(0.25)
                print(Fore.GREEN + "Wohooo!" + Style.RESET_ALL)
                break
            elif rate == "3":
                time.sleep(0.25)
                print(Fore.LIGHTYELLOW_EX + "Huhu, its thatt badd?" + Style.RESET_ALL)
                break
            elif rate == "2":
                time.sleep(0.75)
                print(Fore.YELLOW + "Whyy :(" + Style.RESET_ALL)
                break
            elif rate == "1":
                time.sleep(1)
                print(Fore.RED + "I'm sorry for the bad experience :(" + Style.RESET_ALL)
                break
            elif rate == "0":
                time.sleep(2)
                print(Fore.RED + "...Sorry..." + Style.RESET_ALL)
                break
            else: print(Fore.RED + "Rate between 0 - 5" + Style.RESET_ALL)

score = 0

#Question Generation
for ques in questions:
    time.sleep(1)
    print(Fore.CYAN + ques["question"] + Style.RESET_ALL)
    for opt in ques["options"]:
        time.sleep(0.5)
        print(Fore.LIGHTMAGENTA_EX + opt + Style.RESET_ALL)
    while True:
        answer = input("-> ")
        if answer.lower() in ques["answers"]:
            time.sleep(1.25)
            print(Fore.LIGHTGREEN_EX + "Correct!\n " + Style.RESET_ALL)
            score += 1
            break
        elif answer == "":
            time.sleep(0.25)
            print(Fore.LIGHTRED_EX + "Enter some value!" + Style.RESET_ALL )
        else:
            time.sleep(1.25)
            print(Fore.RED + "Incorrect!\n " + Style.RESET_ALL)
            break

#Bonus Question Asking
time.sleep(1.5)
print(Fore.CYAN + "Do you want a bonus question? (Y or N)" + Style.RESET_ALL)
time.sleep(0.25)
while True:
    extra = input("-> ").lower()
    if extra == "y":
        break
    elif extra == "n":
        while True:
            print("Are you sure? (Y or N)")
            sec_extra = input("-> ").lower()
            if sec_extra == "n":
                break
            else:
                end(score, questions)
        break
    else:
        print("Enter either Y or N.")

#Bonus Question Generation
time.sleep(1)
print(Fore.CYAN + bonus_question["question"] + Style.RESET_ALL)
time.sleep(0.5)
for opt in bonus_question["options"]:
    print(Fore.LIGHTMAGENTA_EX + opt + Style.RESET_ALL)
while True:
    answer = input("-> ")
    if answer.lower() in bonus_question["answers"]:
        time.sleep(1.25)
        print(Fore.LIGHTGREEN_EX + "Correct Answer!\n" + Style.RESET_ALL)
        score += 1
        break
    elif answer == "":
        time.sleep(0.25)
        print(Fore.LIGHTRED_EX + "Enter some value!" + Style.RESET_ALL )
    else:
        time.sleep(1.25)
        print(Fore.RED + "Incorrect!\n " + Style.RESET_ALL)
        break

time.sleep(2)
print(Fore.LIGHTRED_EX + "Loading..." + Style.RESET_ALL)
time.sleep(2)

#rate execution
ratefunc()

#End
end(score, questions)