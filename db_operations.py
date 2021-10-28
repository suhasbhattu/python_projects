import sqlite3


class db_operations:

    def connect_to_db(self):
        con = sqlite3.connect('contact_book.db')
        print('Connected to database')
        return con

    def add_contact(self, contact):
        con = db_operations.connect_to_db(self)
        cur = con.cursor()
        cur.execute(
            f'''INSERT INTO Contacts(name, address, phoneNo, email) VALUES('{contact.name}', '{contact.address}', '{contact.phone_no}', '{contact.email}')''')
        con.commit()
        print('contact added')

    def get_all(self):
        con = db_operations.connect_to_db(self)
        cur = con.cursor()
        rows = cur.execute('''SELECT * FROM Contacts''')
        for row in rows:
            print(row)

    def get_contact(self, id):
        con = db_operations.connect_to_db(self)
        cur = con.cursor()
        row = cur.execute(f'''SELECT * FROM Contacts WHERE id = {id}''')
        return row

    def update_contact(self, contact, id):
        con = db_operations.connect_to_db(self)
        cur = con.cursor()
        cur.execute(
            f'''UPDATE Contacts SET name='{contact.name}', address='{contact.address}', phoneNo='{contact.phone_no}', email='{contact.email}' WHERE id={id}''')
        con.commit()
        print('contact updated')

    def delete_contact(self, id):
        con = db_operations.connect_to_db(self)
        cur = con.cursor()
        cur.execute(f'''DELETE FROM Contacts WHERE id={id}''')
        con.commit()
        print('contact deleted')

    def close_db_connection(self, con):
        con.close()
        print('Database disconnected')
