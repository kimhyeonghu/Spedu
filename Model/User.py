class User:
    def __init__(self, username, email, password, id):
        self.__user_id = id
        self.__email = email
        self.__username = username
        self.__password = password
        self.__account_type = "Trainee"
        self.__security_qns = None
        self.__user_info = None
        self.__cart = None

    def get_email(self):
        return self.__email

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_account_type(self):
        return self.__account_type

    def get_security_qns(self):
        return self.__security_qns

    def get_user_info(self):
        return self.__user_info

    def get_cart(self):
        return self.__cart

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_email(self, email):
        self.__email = email

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_account_type(self, account_type):
        self.__account_type = account_type

    def set_security_qns(self, security_qns):
        self.__security_qns = security_qns

    def set_user_info(self, user_info):
        self.__user_info = user_info

    def set_cart(self, cart):
        self.__cart = cart

    def is_active(self):
        return True

    def get_id(self):
        return self.__user_id

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    @staticmethod
    def from_dict(source):
        user = User(source["username"], source["email"], source["password"], source["id"])
        return user

    def to_dict(self):
        user_dict = {"username": self.__username, "email": self.__email, "password": self.__password, "id": self.__user_id}
        return user_dict


class Trainer(User):
    def __init__(self, email, username, password, id):
        super().__init__(email, username, password, id)
