import pytest
import main

class TestMain(object):
    def test_aplications(self):
        aplication = main.Aplication()
        assert aplication.get_aplication("admin")==["Aptitus", "Neo", "Pago Efectivo", "Urbania"]
    
    def test_access_user(self):
        access = main.Access()
        assert access.get_access("user")==["read"]
    
    def test_persons_lastname_name(self):
        name = "Juan"
        last_name = "Valdez"
        person = main.Person(name,last_name)
        assert person.get_lastname_name()==last_name+" "+name
    
    class TestUser(object):

        def setup(self):
            self.name="Juan"
            self.last_name="Valdez"
            self.type="admin"
            self.user=main.User(self.name, self.last_name, self.type)
        
        def test_get_access_admin(self):
            assert self.user.get_access()==["read", "write" , "delete"]
        
        def test_get_aplication_admin(self):
            assert self.user.get_aplication()==["Aptitus", "Neo", "Pago Efectivo", "Urbania"]