from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name:
    pass


class Phone:
    pass


class Email:
    pass


class Birthday:
    def __init__(self, value):
        if type(value) == str:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        elif type(value) == datetime:
            self.value = value

    def __str__(self):
        return str(self.value.strftime("%d.%m.%Y"))

    def __eq__(self, other):
        if type(other) == str:
            return self.value.date == datetime.strptime(other, "%d.%m.%Y").date
        elif type(other) == datetime:
            return self.value.date == other.value.date
        else:
            return False

class Address:
    pass


class Record:
    pass


class AddressBook:
    pass
