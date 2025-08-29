base_file = None
the_tries = 4

while the_tries > 0:

    try :

        print("Enter an ABS File | As =>> file.ext")
        print(f"You have A : {the_tries} tries")
        file_input = input("Enter a path of file : ").strip()
        print("="*60)
        base_file = open(file_input,"r")
        print(base_file.read())
        print("="*60)

        break

    except FileNotFoundError:

        print("Error : The File Not Found!!")
        the_tries -= 1
        print(f"The Tries enough : {the_tries}")

    except Exception as ex:
    
        print(f"Error : {ex}!!")

    finally :

        if base_file is not None:

            base_file.close()
            print("The File Is Close!!")


else:
    print("All Tries all done!!") 