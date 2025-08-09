# The App Slicing An Email :
email = input("Enter Your Email : ")
if email.find("@") >= 0:
    search_letter1 = email.find("@")
    username = email[0:search_letter1]
    domin = email[search_letter1+1:]
    print(f"Yourname : {username} , domin : {domin}")
else:
    print("Find Wrong in Your Input!! -- Try Again")
input()