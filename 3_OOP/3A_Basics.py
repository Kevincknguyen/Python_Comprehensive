
# DEFINE A CLASS

class User:
    species="Human"
    def __init__(self,name,email="No email provided"):
        self.name=name
        self.email=email
        self.status="Alive"


    def talk(self,message):
        print(self.name,"says",message)

    def perish(self):
        self.status="Dead"
        

# INSTANTIATE AN INSTANCE OF A CLASS
kevin=User("Kevin")
tom=User("Tom")



print(kevin.email)

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