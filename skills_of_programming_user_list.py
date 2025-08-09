my_tuple = ()

my_dict = {

}

def skill(name,*skills ,**skillsbyprogress):
    print(f"Hi {name}..")
    print(f"Your Skills Without Progress : ")
    for skill in skills:
        print(f"- {skill}")
    print(f"Your Skills With Progress : ")
    for key,value in skillsbyprogress.items():
        print(f"- {key} : {value}")

list_of_tuple = list(my_tuple)
for i in range(3):
    tuple_input = str(input("Enter A Language Of Programming : "))
    list_of_tuple.append(tuple_input)
tuple(list_of_tuple)

print("="*60)

for i in range(4):
    dict_input = str(input("Enter A Language Of Programming : "))
    dict_progress = str(input(f"Enter A Progress Of {dict_input} : "))
    my_dict[dict_input] = dict_progress

user_name = str(input("Enter your name : "))

skill(user_name,*list_of_tuple,**my_dict)