# contacts class

from db_operations import db_operations as db_operations


class contacts:

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, phone_no):
        self._phone_no = phone_no

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def add(self, contact):
        # need to call db operations
        db_operations.add_contact(self, contact)
        db_operations.get_all(self)

    def update(self, contact, id):
        # need to call db operations
        db_operations.update_contact(self, contact, id)
        db_operations.get_all(self)

    def delete(self, id):
        db_operations.delete_contact(self, id)
        db_operations.get_all(self)

    def get_contact(self, id):
        rows = db_operations.get_contact(self, id)
        return rows

    def is_empty(self):
        #print(f'printing self {type(self)}')
        #print(f'{self.name}_{self.address}_{self.email}_{self.phone_no}', sep='')
        #if self.name == None | self.address == None | self.phone_no == None | self.email == None:
        if hasattr(self, 'name') | hasattr(self, 'address') | hasattr(self, 'email') | hasattr(self, 'phone_no'):
            return False
        else: 
            return True

while True:
    option = input('\n\nChoose from follwing options:\n\n1. Add contact.\n2. Update contact\n3. Delete contact.\n4. Exit.\n\nEnter option = ')

    if option == '1':
        name = input('Enter the name = ')
        address = input('Enter the address = ')
        while True:
            try:
                phone_no = int(input('Enter the phone no = '))
            except ValueError:
                print('phone no should be integer')
                op = int(
                    input('\n\nDo you want to continue?\n1. Yes.\n2.No\n\nEnter choice = '))
                if op == 2:
                    break
            else:
                while True:
                    try:
                        email = input('Enter the email = ')
                        if email.find('@') == -1 | email.find('.') == -1:
                            raise Exception("email is not valid")
                    except Exception as error:
                        print(error.args[0])
                        op2 = int(
                            input('\n\nDo you want to continue?\n1. Yes.\n2.No\n\nEnter choice = '))
                        if op2 == 2:
                            break
                    else:
                        contact = contacts()
                        contact.name = name
                        contact.address = address
                        contact.phone_no = phone_no
                        contact.email = email
                        contact.add(contact)
                        break
                break

    elif option == '2':
        try:
            id = int(input('Enter the ID = '))
        except ValueError:
            print('id should be integer')
        else:
            contact = contacts()
            old_contact = contact.get_contact(id)
            old_contact1 = ()

            for row in old_contact:
                old_contact1 = row

            if old_contact1:
                while True:
                    choice = input('\n\nChoose from following choices:\n\n1. Edit All.\n2. Choose Field.\n3. Exit.\n\nEnter choice = ')
                    if choice == '1':
                        name2 = input('Enter the name = ')
                        address2 = input('Enter the address = ')
                        while True:
                            try:
                                phone_no2 = int(input('Enter the phone no = '))
                            except ValueError:
                                print('phone no should be integer')
                                op = int(input('\n\nDo you want to continue?\n1. Yes.\n2.No\n\nEnter choice = '))
                                if op == 2:
                                    break
                            else:
                                while True:
                                    try:
                                        email2 = input('Enter the email = ')
                                        if email2.find('@') == -1 | email.find('.') == -1:
                                            raise Exception("email is not valid")
                                    except Exception as error:
                                        print(error.args[0])
                                        op2 = int(
                                            input('\n\nDo you want to continue?\n1. Yes.\n2.No\n\nEnter choice = '))
                                        if op2 == 2:
                                            break
                                    else:
                                        contact = contacts()
                                        contact.name = name2
                                        contact.address = address2
                                        contact.phone_no = phone_no2
                                        contact.email = email2
                                        contact.update(contact, id)
                                        break
                                break
                    

                    if choice == '2':

                        new_contact = contacts()
                        field = int(input('enter the field to update\n1. Name\n2. Address\n3. Phone no\n4.Email =  '))
                        flag = False
                        while True:
                            updatedValue = input('enter updated value = ')
                            if field == 1:
                                new_contact.name = updatedValue
                                new_contact.address = old_contact1[2]
                                new_contact.phone_no = old_contact1[3]
                                new_contact.email = old_contact1[4]
                                break
                            elif field == 2:
                                new_contact.name = old_contact1[1]
                                new_contact.address = updatedValue
                                new_contact.phone_no = old_contact1[3]
                                new_contact.email = old_contact1[4]
                                break
                            elif field == 3:
                                try:
                                    updatedValue = int(updatedValue)
                                except ValueError:
                                    print('phone number should be integer.\n')
                                    op = int(input('\n\nDo you want to continue?\n1. Yes.\n2. No\n\nEnter choice = '))
                                    if op == 2:
                                        break
                                    elif op == 1:
                                        flag=True
                                else:
                                    new_contact.name = old_contact1[1]
                                    new_contact.address = old_contact1[2]
                                    new_contact.phone_no = updatedValue
                                    new_contact.email = old_contact1[4]
                                    break
                            elif field == 4:
                                new_contact.name = old_contact1[1]
                                new_contact.address = old_contact1[2]
                                new_contact.phone_no = old_contact1[3]
                                new_contact.email = updatedValue

                            if not flag:  
                                new_contact.update(new_contact, id)
                                break

                    if choice == '3':
                        break
            else:
                print('contact not found')

    elif option == '3':
        try:
            id = int(input('Enter the ID = '))
        except ValueError:
            print('id should be integer')
        else:
            contact = contacts()
            old_contact = contact.get_contact(id)
            old_contact1 = ()

            for row in old_contact:
                old_contact1 = row

            if old_contact1:
                contact1 = contacts()
                contact1.delete(id)
            else:
                print('contact not found')

    elif option == '4':
        break

    else:
        print('enter correct option')
