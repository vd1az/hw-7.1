from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[str(record.name)] = record


class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phones = [Phone(phone)]

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __str__(self):
        return str(self.value)


if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert str(ab['Bill'].phones[0].value) == '1234567890'
    print('All Ok')