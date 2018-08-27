class Person(object):
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
    
    def get_lastname_name(self):
        return self.lastname + " " + self.name


class Access(object):
    #def __init__(self, type):
    #    self.type = type
    
    def get_access(self, type):
        access = ["read", "write" , "delete"]
        if type.lower() != "admin":
            access=["read"]
        return access

class Aplication(object):

    def __init__(self):
        self.aplication = ["Aptitus", "Neo", "Pago Efectivo", "Urbania"]

    def get_aplication (self,type):
        if type.lower() != "admin":
            return []
        return self.aplication

class User(Person, Access):
    def __init__(self, name, lastname, type):
        self.type = type
        self.aplication = Aplication()
        super(User, self).__init__(name,lastname)
    
    def get_access(self):
        access = super(User,self).get_access(self.type)
        return access

    def get_aplication(self):
        return self.aplication.get_aplication(self.type)

if __name__ == "__main__":

    """ person = Person("Juan", "Valdez")
    print("Name: {}".format(person.name))
    print("Last name: {}".format(person.lastname))
    print("Nombre completo: {}".format(person.get_lastname_name()))

    user = User("Carlos","Perez","Admin")
    print("Usuario: {}".format(user.get_lastname_name()))
    print("Tipo: {}".format(user.type))
    print("Accesos: {}".format(user.get_access()))
    print("Aplicaciones: {}".format(user.get_aplication()))

    user = User("Maria","Salas","Usuario")
    print("Usuario: {}".format(user.get_lastname_name()))
    print("Tipo: {}".format(user.type))
    print("Accesos: {}".format(user.get_access()))
    print("Aplicaciones: {}".format(user.get_aplication())) """

    users = [
        User("Juan", "Valdez", "Admin"),
        User("Maria","Salas","Usuario"),
        User("Carlos","Perez","Admin")
    ]

    for user in users:
        print("Usuario: {}".format(user.get_lastname_name()))
        print("Tipo: {}".format(user.type))
        print("Accesos: {}".format(user.get_access()))
        print("Aplicaciones: {}".format(user.get_aplication()))
        print("")