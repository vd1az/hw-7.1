from datetime import datetime, timedelta

class Field:
    def __init__(self, value=None):
        self._value = value

    def __repr__(self):
        return f'{self.__class__.__name__}(value={self._value})'

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value


class Phone(Field):
    def set_value(self, value):
        # Проверяем корректность введенного номера телефона
        if not isinstance(value, str):
            raise ValueError("Phone number must be a string.")
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits.")
        if len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        self._value = value


class Birthday(Field):
    def set_value(self, value):
        # Проверяем корректность введенной даты рождения
        if not isinstance(value, str):
            raise ValueError("Birthday must be a string.")
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid birthday format. It should be YYYY-MM-DD.")
        self._value = value


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if self.birthday.get_value():
            today = datetime.now().date()
            next_birthday_year = today.year
            birthday = datetime.strptime(self.birthday.get_value(), "%Y-%m-%d").date()
            next_birthday = birthday.replace(year=next_birthday_year)

            if next_birthday < today:
                next_birthday = birthday.replace(year=next_birthday_year + 1)

            days_left = (next_birthday - today).days
            return days_left
        return None


class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def remove_record(self, record):
        self.records.remove(record)

    def __iter__(self):
        return iter(self.records)


# Пример использования классов

address_book = AddressBook()

record1 = Record("John Doe", phone="1234567890", birthday="1990-05-01")
address_book.add_record(record1)

record2 = Record("Jane Smith", phone="9876543210", birthday="1995-10-15")
address_book.add_record(record2)

record3 = Record("Bob Johnson", phone="5555555555", birthday="1988-12-25")
address_book.add_record(record3)

for record in address_book:
    print(record.name, record.phone.get_value(), record.birthday.get_value())

# Вывод количества дней до дня рождения
for record in address_book:
    days_left = record.days_to_birthday()
    if days_left is not None:
        print(f"Days left for {record.name}'s birthday: {days_left}")
    else:
        print(f"No birthday information available for {record.name}.")
