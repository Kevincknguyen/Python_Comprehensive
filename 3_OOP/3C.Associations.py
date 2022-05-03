
#LET US REPURPOSE

class User:
    species="Human"
    all_peoples=[]
    def __init__(self,name,email):
        self.name=name
        self.status="Alive"
        User.all_peoples.append(self)
        self.pets=[]
        self.email= Email(email)

    def addPet(self,Pets):
        self.pets.append(Pets)
    @classmethod
    def all_people(cls):
        for x in cls.all_peoples:
            print(x.name)


class Email:
    def __init__(self,emailAddress,password="Default"):
        self.emailAddress=emailAddress
        self.password=password

    def print(self):
        print(self.emailAddress)
        print(self.password)

    def setPassword(self,password):
        self.password=password


class Pets:
    def __init__(self,name,species):
        self.name=name
        self.species=species

kevin=User("Kevin","kevin.ck.nguyen@gmail.com")

kevin.email.print()
kevin.email.setPassword("1123123")
kevin.email.print()


kevin.addPet(Pets("Kitty","Cat"))
kevin.addPet(Pets("Doggie","Dog"))


print(kevin.pets)