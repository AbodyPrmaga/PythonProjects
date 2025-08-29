import os
from termcolor import colored
from actions import *



db = SkillDB()

os.system("cls")
print(colored("THE OPTIONS".center(40,"="),"red"))
print(colored("""
----------To Exit To 'exit'----------
1 - Get All Skills
2 - Add A New Skill
3 - Update A Skill
4 - Delete A Skill
5 - Clear ALL
""","green"))

while True:  

    try:
        action_input = input("Entar A Number of Any Action or Exit : ")

        db.connect()

        if action_input == "1":

            db.get_skills()

        elif action_input == "2":

            name_skill = str(input("Enter A neme of Skill : "))
            range_skill = int(input("Enter A Range of Skill : "))
            db.add_skill(name_skill,range_skill)

        elif action_input == "3":

            n_name_skill = str(input("Enter A New neme of Skill : "))
            n_range_skill = int(input("Enter A New Range of Skill : "))
            id_skill = int(input("Enter A Id of Skill : "))
            db.update_skill(n_name_skill,n_range_skill,id_skill)

        elif action_input == "4":

            id_skill = int(input("Enter A Id of Skill For Delete : "))
            db.delete_skill(id_skill)

        elif action_input == "5":
            
            db.clear_skills()

        elif action_input == "exit":
            
            break

        else:
            print("Sorry,Error!!")

    except Exception as ex:
        print(f"Error : {ex}!!")
