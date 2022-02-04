class Promo_code_data:
    def __init__(self, code_name, code_value):
        self.__code_name = code_name
        self.__code_value = code_value

    def get_code_name(self):
        return self.__code_name
    def get_code_value(self):
        return self.__code_value
    def set_code_name(self, code_name):
        self.__code_name = code_name
    def set_code_value(self, code_value):
        self.__code_value = code_value