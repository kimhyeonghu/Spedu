class User:
    def __init__(self, username, email, password, id):
        self.__user_id = id
        self.__email = email
        self.__username = username
        self.__password = password

    def get_user_id(self):
        return self.__user_id

    def get_email(self):
        return self.__email

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_email(self, email):
        self.__email = email

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

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


class Trainee(User):
    def __init__(self, email, username, password, id):
        super().__init__(email, username, password, id)
        self.__account_type = "Trainee"
        self.__qns1 = None
        self.__ans1 = None
        self.__qns2 = None
        self.__ans2 = None
        self.__qns3 = None
        self.__ans3 = None
        self.__first_name = None
        self.__last_name = None
        self.__address = None
        self.__phone = None
        self.__credit_card = None

    def get_account_type(self):
        return self.__account_type

    def get_qns1(self):
        return self.__qns1

    def get_ans1(self):
        return self.__ans1

    def get_qns2(self):
        return self.__qns2

    def get_ans2(self):
        return self.__ans2

    def get_qns3(self):
        return self.__qns3

    def get_ans3(self):
        return self.__ans3

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_credit_card(self):
        return self.__credit_card

    def set_account_type(self, account_type):
        self.__account_type = account_type

    def set_qns1(self, qns1):
        self.__qns1 = qns1

    def set_ans1(self, ans1):
        self.__ans1 = ans1

    def set_qns2(self, qns2):
        self.__qns2 = qns2

    def set_ans2(self, ans2):
        self.__ans2 = ans2

    def set_qns3(self, qns3):
        self.__qns3 = qns3

    def set_ans3(self, ans3):
        self.__ans3 = ans3

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def set_credit_card(self, credit_card):
        self.__credit_card = credit_card
