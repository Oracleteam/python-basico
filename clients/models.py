import uuid


class Client:

    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4()

    def get_name(self):
        return self.name

    def get_company(self):
        return self.company

    def get_email(self):
        return self.email

    def get_position(self):
        return self.position

    def set_name(self, name):
        self.name = name
        return self.name

    def set_company(self, company):
        self.company = company
        return self.company

    def set_position(self, position):
        self.position = position
        return self.position

    def set_email(self, email):
        self.email = email
        return self.email

    def to_dict(self):
        return vars(self)

    @staticmethod
    def schema():
        return ["name", "company", "email", "position", "uid"]
