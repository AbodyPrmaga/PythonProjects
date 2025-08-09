websites = []

maxnum = 6

while maxnum > 0 :

    web = input("Enter Name Web Only Without (https://) : ")

    maxnum -= 1

    clean_web = web.strip().lower()

    websites.append(f"https://{clean_web}")
    
    print(f"All Websites : {websites}")
    print("="*40)
    print(f"Number of times Free is {maxnum}")

else:
    print("You Full Bookmarks...")

print("The Bookmarks Found".center(40,"="))

if len(websites) > 0 :
    
    index = 0 

    while index < len(websites):
        print(f"#{index+1} : {websites[index]}")
        index += 1
    
    print("This Websites Finding in Bookmarks recently!")

else:
    print("The Bookmarks Empty!")