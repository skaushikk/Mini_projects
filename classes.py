'''
Created Date: Friday September 4th 2020
Author: skaushikk
-----
Last Modified:
Modified By:
-----
Copyright (c) 2020 Your Company
'''


class Employee:
    raise_percent = 4

    def __init__(self, firstname, lastname, occupation, id, pay, department):
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname + '.' + lastname + '@email.com'
        self.occupation = occupation
        self.id = id
        self.pay = pay
        self.department = department

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def apply_raise(self):
        if self.department == 'Engineering':
            self.pay = int(self.pay * (1 + self.raise_percent / 100))

        elif self.department == 'Management':
            self.pay = int(self.pay * (1 + 2 * self.raise_percent / 100))


class Developer(Employee):
    pass


tom = Developer('Tom', 'Cruise', 'Programmer', '20122', 25000, 'Engineering')
harry = Employee('Tom', 'Cruise', 'Programmer', '20122', 25000, 'Management')
print(tom.pay, harry.pay)
tom.apply_raise()
harry.apply_raise()

print(tom.pay, harry.pay)
print(tom.email)