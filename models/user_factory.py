class User:
    def __init__(self, name):
        self.name = name

class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.role = "admin"

class ClientUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.role = "client"

class UserFactory:
    @staticmethod
    def create_user(user_type, name):
        if user_type == "admin":
            return AdminUser(name)
        elif user_type == "client":
            return ClientUser(name)
        else:
            raise ValueError("Tipo de usuário inválido")
