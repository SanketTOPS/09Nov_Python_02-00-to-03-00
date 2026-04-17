class master:
    def login(self,unm,pas):
        if unm=="admin" and pas=="tops@123":
            print("Login Successfull!")
        else:
            print("Error!")

class home(master):
    def login(self, unm, pas):
        return super().login(unm, pas)
    
class about(master):
    def login(self, unm, pas):
        return super().login(unm, pas)