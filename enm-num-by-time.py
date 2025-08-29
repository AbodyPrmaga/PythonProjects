from time import time

def decoratest(fun):

    def decora():

        start = time()
        fun()
        end = time()

        timer = end - start

        tx = "s"

        if timer >= 60 :

            tx = "m"
            timer = timer / 60
        
        else:

            pass

        print(f"The Operation Take : {timer:.2f}{tx}")

    return decora



numb = int(input("Enter Any number Without Zero : "))

if numb != 0 : 
    pass 
else : 
    print("The Num Equal Zero!")

@decoratest
def loop():
    for i in range(1,numb):
        print(i)
loop()