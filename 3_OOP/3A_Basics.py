
# DEFINE A CLASS

class User:
    #THINK OF THESE AS ATTRIBUTES OF THE CLASS, AND NOT ATTRIBUTES OF INSTANCES OF THE CLASS
    species="Human"
    all_peoples=[]

    #SO THINK OF THESE AS ATTRIBUTES OF THE INSTANCE OF THE CLASS, BUT THAT THE CLASS ITSELF INHERENTLY DOES NOT HAVE
    def __init__(self,name="Default settings are here",email="Default message:No email provided"):
        self.name=name
        self.email=email
        self.status="Alive"
        User.all_peoples.append(self)

    #STANDARD METHODS
    def talk(self,message):
        print(self.name,"says",message)

    def perish(self):
        self.status="Dead"
        
    #CLASS METHOD
    @classmethod
    def all_people(cls):
        for x in cls.all_peoples:
            print(x.name)

    @classmethod
    def change_species(cls):
        cls.species="Unknown"

    #STATIC METHOD
    @staticmethod
    def definition():
        print(f"Static methods organize code. Methods that are unrelated directly to a class,but is categorized under the class.  \n Essentially static methods can be used to place a method that you would primarily use for all instances of a specific class, but is not beholden to  the attributes or other methods of a class")

# INSTANTIATE AN INSTANCE OF A CLASS
kevin=User("Kevin")
tom=User("Tom")



#REASSIGN ATTRIBUTES LIKE SO

kevin.email="kevin.ck.nguyen@gmail.com"
tom.species="Alien"


#ACCESS ATTRIBUTES
print("Kevins email: ",kevin.email)
print("Kevins species: ",kevin.species)



print("Toms species: ",tom.species)
print("Kevins species remains unchanged: ",kevin.species)

print("Toms status: ",tom.status)


#ACCESS METHODS

kevin.talk("Hello there")
tom.perish()
print("Toms status: ",tom.status)


#class methods: APPLIES TO CLASS ITSELF

User.all_people()

User.change_species()

    # THIS CHANGES KEVIn
print(kevin.species)
    #...BUT NOT TOM
print(tom.species)

tom.definition()