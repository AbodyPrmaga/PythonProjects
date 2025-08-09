import random

a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = "1234567890"
d = "!@#$%^&*()-_=+[]{}:;,.?/"

all_ =  str(a+b+c+d)


range_ = int(input("The num of passwords : "))
len_ = int(input("The num of lenth passwords : "))

for i in range(range_):
    passw = "".join(random.sample(all_,len_))
    print(f"password : {passw}")
