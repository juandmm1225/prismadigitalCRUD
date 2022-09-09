
class User():

    def __init__(self, id, username=None, password=None, email=None) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def to_JSON(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'email': self.email
        }