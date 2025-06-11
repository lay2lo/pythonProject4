# class Physics:
#     gravity=  9.8
#     def potentialEnergy(self,mass,height):
#         return mass*self.gravity*height
#
#
#     physics = Physics()
#     physics.potentialEnergy()



class User:
    def __init__(self,gender,weight,height,name,role):
     self.gender = gender
     self.weight = weight
     self.height = height
     self.name = name
     self.role = role
    def login(self,username,password):
        if username=="Ade" and password=="123":
            return True
        else:
            return False



# customer = User("female",50,120, "Jane","Admin")
def login()