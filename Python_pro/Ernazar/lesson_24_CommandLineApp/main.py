import sys
from sqlite3 import *

class Contact:
    def __init__(self,db):
        self.db=db
        cursor= self.db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS contacts (name,surname,number)""")


    def add(self,name,surname,number):
        cursor= self.db.cursor()
        cursor.execute(f"""INSERT INTO contacts(name,surname,number) VALUES('{name}', '{surname}', '{number}')""")

    def list(self):
        cursor = self.db.cursor()
        cursor.execute("""SELECT * FROM contacts""")
        return cursor.fetchall()
    def search(self,name):
        cursor=self.db.cursor()
        cursor.execute(f"""SELECT * FROM contacts WHERE name='{name}' """)
        return cursor.fetchall()
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Only 1 argument required')
    
    commands=('add', 'list', 'search')
    command= sys.argv[1]
    if command not in commands:
        sys.exit(f'Unknown command: {command}, Commands: {commands}')
    
    with connect('contact.db') as db:
        contact = Contact(db)
    
        if command == 'add':
            name= input('Name:')
            surname= input('Surname:')
            number= input('Number:')
            contact.add(name,surname,number)
            print('Contact added')
        elif command == 'list':
            contacts = contact.list()
            for contact in contacts:
                print(contact)
        elif command == 'search':
            name= input('Name:')
            contacts= contact.search(name)
            for contact in contacts:
                print(contact)
