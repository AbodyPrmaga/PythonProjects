def decornum1(fun):

    def decor(num1,num2):

        if num1 < 0 or num2 <0 :

            print("[+] Find a Number is negative!!")


        print("TOTAL :",end=" ")

        fun(num1,num2)

    return decor

def decornum2(fun):

    def decor(num1,num2):

        print("="*50)
        fun(num1,num2)
        print("="*50)

    return decor


print("(: Calc Simply :)".center(50,"="))
@decornum2
@decornum1
def calc(num1,num2):


    print(num1+num2)


n1 = int(input("Enter One Number : "))

n2 = int(input("Enter Two Number : "))

calc(n1,n2)