import re


print("="*50)
email = input("Enter your email addr : ")

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net",email)

emails_list = []


if search != []:

    emails_list.append(search)
    print("You Email Valid!")


else:

    print("You Email Invalid!")



print("List OF Avalibale Emails".center(50,"="))

for em in emails_list:

    print(em)