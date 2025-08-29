import sqlite3
from termcolor import colored

class SkillDB:

    def __init__(self,name="skills.db"):
        """A Function Is Main To Init DataBase"""
        self.name = name
        self.connect()

    def connect(self):
        """A Function To Connect A DataBase And Create Tables"""
        try:
            with sqlite3.connect(self.name) as db:
                db.execute("""CREATE TABLE IF NOT EXISTS skills(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                skill TEXT,
                range INTEGER
                )""")

        except Exception as ex:
            print(f"Error : {ex}!!")

    def get_skills(self):
        """A Function To Get All Skills"""
        try:
            with sqlite3.connect(self.name) as db:
                cur = db.cursor()
                cur.execute("SELECT * FROM skills")
                data = cur.fetchall()
                if data:
                    print(colored("Your Skills".center(70,"="),"magenta"))
                    for row in data:
                        print(f"{colored("ID","red")} : {row[0]} || {colored("Skill","green")} : {row[1]} || {colored("Range","blue")} : {row[2]}%")
                    print(colored("="*70,"magenta"))
                    

                else:
                    print(colored("Not Found Any Skills","red"))
        except Exception as ex:
            print(f"Error : {ex}!!")

    def add_skill(self,skill,range_):
        """A Function To Add A New Skill"""
        try:
            with sqlite3.connect(self.name) as db:
                db.execute("INSERT INTO skills(skill,range) VALUES(?,?)",(skill,range_))
            print(colored(f"Done Add {skill} Skill Succssfully!!","green"))

        except Exception as ex:
            print(f"Error : {ex}!!")

    def update_skill(self,n_skill,n_range_,id_):
        """A Function To Update A Skill"""
        try:
            with sqlite3.connect(self.name) as db:
                db.execute("UPDATE skills SET skill = ? , range = ? WHERE id = ?",(n_skill,n_range_,id_))
                db.commit()
            print(colored(f"Done Update {n_skill} Skill Succssfully!!","green"))

        except Exception as ex:
            print(f"Error : {ex}!!")
        

    def delete_skill(self,id_):
        """A Function To Delete A Skill"""
        try:
            with sqlite3.connect(self.name) as db:
                db.execute("DELETE FROM skills WHERE id = ?",(id_,))
                db.commit()
            print(colored(f"Done Delete Index : {id_} Succssfully!!","green"))

        except Exception as ex:
            print(f"Error : {ex}!!")
        
    def clear_skills(self):
        """A Function To Clear All Skills"""
        try:
            with sqlite3.connect(self.name) as db:
                db.execute("DELETE FROM skills")
                db.commit()
            print(colored(f"Clear All Skills Succssfully!!","green"))

        except Exception as ex:
            print(f"Error : {ex}!!")