import time
from colorama import Fore , Style

time.sleep(0.25)
print(Fore.CYAN + "-----QUIZ GAME-----" + Style.RESET_ALL)
time.sleep(0.5)
print(Fore.LIGHTBLACK_EX + "--10 questions--")
time.sleep(1.5)
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
    
score = 0

#End
def end():
    time.sleep(1)
    print(Fore.CYAN + "Processing..." + Style.RESET_ALL)
    time.sleep(2.5)
    print(Fore.CYAN + "Almost There..." + Style.RESET_ALL)

    time.sleep(3)
    print(Fore.YELLOW + f"You got {score} questions correct out of 10." + Style.RESET_ALL)
    time.sleep(1.5)
    print(Fore.YELLOW + f"That is equal to {(int(score)/10)*100}% score." + Style.RESET_ALL)
    time.sleep(2)
    print(Fore.CYAN + "Thank you for playing this game.\nBye Byee!" + Style.RESET_ALL)
    time.sleep(1)
    exit()

#Q1
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "What is the capital city of U.S.A. ?\n| i) California | ii) Washington D.C. | iii) New York | iv) Texas |" + Style.RESET_ALL)

while True:
    ans1 = ["ii", "washington d.c.", "ii."]
    give_ans1 = input("-> ").lower()
    if give_ans1 in ans1:
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX + "Correct Answer!" + Style.RESET_ALL)
        score += 1
        break
    elif give_ans1 == "":
        print("Enter some value!")
    else:
        time.sleep(1.25)
        print(Fore.RED + "Wrong Answer!" + Style.RESET_ALL)
        break

#Q2
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "Who invented the number Zero ?\n| i) Aarush Bhatt | ii) Christoper Waramanrty | iii) Xia lao | iv) Arya Bhatt |" + Style.RESET_ALL)

while True:
    ans1 = ["iv", "arya bhatt", "iv."]
    give_ans1 = input("-> ").lower()
    if give_ans1 in ans1:
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX + "Correct Answer!" + Style.RESET_ALL)
        score += 1
        break
    elif give_ans1 == "":
        print("Enter some value!")
    else:
        time.sleep(1.25)
        print(Fore.RED + "Wrong Answer!" + Style.RESET_ALL)
        break

#Q3
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "Odd one out: 8, 27, 64, 100, 125\n| i) 8 | ii) 27 | iii) 100 | iv) 125 |" + Style.RESET_ALL)

while True:
    ans1 = ["iii", "100", "iii."]
    give_ans1 = input("-> ").lower()
    if give_ans1 in ans1:
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX + "Correct Answer!" + Style.RESET_ALL)
        score += 1
        break
    elif give_ans1 == "":
        print("Enter some value!")
    else:
        time.sleep(1.25)
        print(Fore.RED + "Wrong Answer!" + Style.RESET_ALL) 
        break

#Q4
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "What is the capital of Bhutan ?\n| i) Laos | ii) Taiaga | iii) Jinping | iv) Thimpu |" + Style.RESET_ALL)

while True:
    ans1 = ["iv", "thimpu", "iv."]
    give_ans1 = input("-> ").lower()
    if give_ans1 in ans1:
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX + "Correct Answer!" + Style.RESET_ALL)
        score += 1
        break
    elif give_ans1 == "":
        print("Enter some value!")
    else:
        time.sleep(1.25)
        print(Fore.RED + "Wrong Answer!" + Style.RESET_ALL)
        break

#Q5
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "Find the missing number: 3, 6, 11, 18, 27, __ ?\n| i) 36 | ii) 38 | iii) 40 | iv) 42 |" + Style.RESET_ALL)

while True:
    ans1 = ["ii", "38", "ii."]
    give_ans1 = input("-> ").lower()
    if give_ans1 in ans1:
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX + "Correct Answer!" + Style.RESET_ALL)
        score += 1
        break
    elif give_ans1 == "":
        print("Enter some value!")
    else:
        time.sleep(1.25)
        print(Fore.RED + "Wrong Answer!" + Style.RESET_ALL)
        break

#Q6
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "What is the only continent that's on all 4 hemispheres?\n| i) Africa | ii) Asia | iii) Australia | iv) South America |" + Style.RESET_ALL)

while True:
    ans1 = ["i", "africa", "i."]
    give_ans1 = input("-> ").lower()
    if give_ans1 in ans1:
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX + "Correct Answer!" + Style.RESET_ALL)
        score += 1
        break
    elif give_ans1 == "":
        print("Enter some value!")
    else:
        time.sleep(1.25)
        print(Fore.RED + "Wrong Answer!" + Style.RESET_ALL)
        break

#Q7
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "What is the study of knowledge called ?\n| i) Aerobics | ii) Einsteinology | iii) Epistemology | iv) Entomology |" + Style.RESET_ALL)

while True:
    ans1 = ["iii", "epistemology", "iii."]
    give_ans1 = input("-> ").lower()
    if give_ans1 in ans1:
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX + "Correct Answer!" + Style.RESET_ALL)
        score += 1
        break
    elif give_ans1 == "":
        print("Enter some value!")
    else:
        time.sleep(1.25)
        print(Fore.RED + "Wrong Answer!" + Style.RESET_ALL)
        break

#Q8
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "What is the distance between the two rails of a railway track called ?\n| i) Seal gauge | ii) Track guage | iii) Ammeter | iv) Railometer |" + Style.RESET_ALL)

while True:
    ans1 = ["ii", "track gauage", "ii."]
    give_ans1 = input("-> ").lower()
    if give_ans1 in ans1:
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX + "Correct Answer!" + Style.RESET_ALL)
        score += 1
        break
    elif give_ans1 == "":
        print("Enter some value!")
    else:
        time.sleep(1.25)
        print(Fore.RED + "Wrong Answer!" + Style.RESET_ALL)
        break

#Q9
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "What is the first phase of mitosis ?\n| i) Anaphase | ii) Prephase | iii) Telophase | iv) Prophase |" + Style.RESET_ALL)

while True:
    ans1 = ["iv", "prophase", "iv."]
    give_ans1 = input("-> ").lower()
    if give_ans1 in ans1:
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX + "Correct Answer!" + Style.RESET_ALL)
        score += 1
        break
    elif give_ans1 == "":
        print("Enter some value!")
    else:
        time.sleep(1.25)
        print(Fore.RED + "Wrong Answer!" + Style.RESET_ALL)
        break

#Q10
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "What is the world's tallest statue ?\ni) Statue of Buddha\nii) Statue of Unity\niii) Statue of Liberty\niv) Statue of Gengis Khan" + Style.RESET_ALL)

while True:
    ans1 = ["ii", "38", "ii."]
    give_ans1 = input("-> ").lower()
    if give_ans1 in ans1:
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX + "Correct Answer!" + Style.RESET_ALL)
        score += 1
        break
    elif give_ans1 == "":
        print("Enter some value!")
    else:
        time.sleep(1.25)
        print(Fore.RED + "Wrong Answer!" + Style.RESET_ALL)
        break

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
                end()
        break
    else:
        print("Enter either Y or N.")

#QBonus
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "Who is the artist of 'Love Me Not' Song ?\n| i) Jude Daniver | ii) Ravyn Lenae | iii) Christ Martin | iv) Deniver |" + Style.RESET_ALL)

while True:
    ans1 = ["ii", "ranvyn lenae", "ii."]
    give_ans1 = input("-> ").lower()
    if give_ans1 in ans1:
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX + "Correct Answer!" + Style.RESET_ALL)
        score += 1
        break
    elif give_ans1 == "":
        print("Enter some value!")
    else:
        time.sleep(1.25)
        print(Fore.RED + "Wrong Answer!" + Style.RESET_ALL)
        break
time.sleep(2)
print(Fore.LIGHTRED_EX + "Loading..." + Style.RESET_ALL)

#Rate the game
time.sleep(2)
print(Fore.CYAN + "How much would you like to rate my game :) ?")
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

end()



