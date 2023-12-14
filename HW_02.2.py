"""Розробіть систему для управління адресною книгою.

Сутності:

1. Field: Базовий клас для полів запису.
2. Name: Клас для зберігання імені контакту. Обов'язкове поле.
3. Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
4. Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
5. AddressBook: Клас для зберігання та управління записами.

Функціональність:

AddressBook:
- Додавання записів.
- Пошук записів за іменем.
- Видалення записів за іменем.

Record:
- Додавання телефонів.
- Видалення телефонів.
- Редагування телефонів.
- Пошук телефону.

Критерії оцінювання
Клас AddressBook:
- Реалізовано метод add_record, який додає запис до self.data.
- Реалізовано метод find, який знаходить запис за ім'ям.
- Реалізовано метод delete, який видаляє запис за ім'ям.

Клас Record:
- Реалізовано зберігання об'єкта Name в окремому атрибуті.
- Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
- Реалізовано методи для додавання - add_phone/видалення - remove_phone/редагування - edit_phone/пошуку об'єктів Phone - find_phone.

Клас Phone:
- Реалізовано валідацію номера телефону (має бути 10 цифр).

"""


from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(
            value
        )  # ініціалізація атрибутів батьківського класу Field для Name


class Phone(Field):
    def __init__(self, value):
        super().__init__(
            value
        )  # ініціалізація атрибутів батьківського класу Field для Phone

    def validate_phone(self):
        if not (
            len(self.value) == 10 and self.value.isdigit()
        ):  # валідація номера телефону (має бути 10 цифр).
            raise ValueError("Не правильний формат, мав би складатись з 10 чисел")


class Record:
    def __init__(self, name):
        self.name = Name(name)  # зберігання об'єкта Name в окремому атрибуті.
        self.phones = []

    def add_phone(self, phone):  # метод для додавання - add_phone
        new_phone = Phone(
            phone
        )  # зберігання списку об'єктів Phone в окремому атрибуті.
        new_phone.validate_phone()
        self.phones.append(new_phone)

    def remove_phone(self, phone):  # метод для видалення - remove_phone.
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                self.phones.remove(phone_obj)
                return
        raise ValueError(
            "UPS ... Такого номеру телефону не знайдено в телефонній книзі"
        )

    def edit_phone(self, old_phone, new_phone):  # редагування - edit_phone
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        raise ValueError(
            "UPS ... Такого номеру телефону не знайдено в телефонній книзі"
        )

    def find_phone(self, phone):  # пошук об'єктів Phone - find_phone.
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj.value
        raise ValueError("UPS ... по даному номеру нічого не знайдено")

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):  # метод add_record, який додає запис до self.data
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):  # метод delete, який видаляє запис за ім'ям
        del self.data[name]

    def find(self, name):  # метод find, який знаходить запис за ім'ям
        return self.data[name]


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
