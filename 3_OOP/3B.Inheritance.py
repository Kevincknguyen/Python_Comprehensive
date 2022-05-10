#USING THE PRIOR CLASS AS AN EXAMPLE

class User:
    species="Human"
    all_peoples=[]
    def __init__(self,name,email="Default message:No email provided"):
        self.name=name
        self.email=email
        self.status="Alive"
        User.all_peoples.append(self)

    def talk(self,message):
        print(self.name,"says",message)

    def perish(self):
        self.status="Dead"
        
    @classmethod
    def all_people(cls):
        for x in cls.all_peoples:
            print(x.name)

    @classmethod
    def change_species(cls):
        cls.species="Unknown"

    @staticmethod
    def definition():
        print(f"Static methods organize code. Methods that are unrelated directly to a class,but is categorized under the class.  \n Essentially static methods can be used to place a method that you would primarily use for all instances of a specific class, but is not beholden to  the attributes or other methods of a class")


#INHERITANCE

class Runner(User):
    #IN THE INIT INCLUDE EVERYTHING, INCLUDING THE TRAITS INHERITED FROM SUPER
    def __init__(self,name,speed,email):
        super().__init__(name,email)
        self.speed=speed

    def talk(self,message):
        super().talk(message)
        print(self.name,"says","I'm also a runner")

#INHERITANCE #2
class Crazy(User):
    def talk(self):
        print("hoopla")





kevin=Runner("Kevin",5,"kevin.ck.nguyen@gmail.com")
tim=User("Tim")
crazy=Crazy("Crazy")



kevin.talk("This is an example")

tim.talk("Hello")
crazy.talk()