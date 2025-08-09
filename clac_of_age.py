# Clac Your Age
print("#" * 100)
print("You can choose by name unit or first latter only😊".center(80,"#"))
print("#" * 100)
##############
input_user = input("Enter Unit Or First Latter : ")
age = int(input('Enter your age : ').strip())
##########
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
##########
if input_user == "months" or "m":
    print(f"You Lived For {months} months😊")
    print("🌹"*50)
#########################
elif input_user == "weeks" or "w":
    print(f"You Lived For {weeks} months😊")
    print("🌹"*50)
#########################
elif input_user == "days" or "d":
    print(f"You Lived For {days} days😊")
    print("🌹"*50)
#########################
elif input_user == "hours" or "h":
    print(f"You Lived For {hours} hours😊")
    print("🌹"*50)
#########################
elif input_user == "minutes" or "ms":
    print(f"You Lived For {months} minutes😊")
    print("🌹"*50)
#########################
elif input_user == "seconds" or "s":
    print(f"You Lived For {months} seconds😊")
    print("🌹"*50)
else:
    print("Find Error Sorry Cheak your Input 🤔")
input()