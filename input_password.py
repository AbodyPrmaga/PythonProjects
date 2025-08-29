tries = 3

correct_password = "qwerty"

user_password = input("Enter The PassWord : ").strip()

while user_password != correct_password:

    tries -= 1 

    print(f"The PassWord Incorrect , {'Last' if tries == 0 else tries} Chance Left")

    user_password = input("Enter The PassWord : ").strip()

    if tries == 0 :

        print("All Chances Are Finshed!")

        break

else:
    print("The PassWord Is correct..")