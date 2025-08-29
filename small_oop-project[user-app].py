class User:

    def __init__(self,fname,mname,lname,gender):

        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.gender = gender

    def get_great_name(self):
        
        already_gender = ""

        if self.gender == "Male":

            already_gender = "Mr"

        elif self.gender == "Female":

            already_gender = "Miss"

        else:

            return "Error"

        return f"Hi {already_gender} : {self.fname}!!"

    def all_name(self):

        self.gname = f"Hi {self.fname} , {self.mname} , {self.lname} !!"

        return "="*50 + "\n" + self.gname



user1 = User("Mawda","Mohamed","Samir","Female")

print(user1.all_name())