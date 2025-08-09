admins = ["Abdelrahman","Mohamed","Taher"]
name = str(input("Enter Your Name : ")).capitalize().strip()
if name in admins:
    print(f"Hi {name} you are admin..")
    command = str(input("Enter Command (delete or update) : ")).lower()
    if command == "update":
        new_name = str(input("Enter Your New Name : ")).capitalize().strip()
        admins[admins.index(name)] = new_name
        print("Done Update Name Succssfully!!")
        print(admins)
    elif command == "delete":
        admins.remove(name)
        print("Done Delete Name Succssfully!!")
        print(admins)
else:
    print("Sorry!! Your Aren't Admin..")