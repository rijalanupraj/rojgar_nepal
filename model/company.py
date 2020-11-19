class Company:
    def __init__(self, name, username, phone, address, password):
        self.id = ''
        self.name = name
        self.username = username
        self.phone = phone
        self.address = address
        self.password = password

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address
