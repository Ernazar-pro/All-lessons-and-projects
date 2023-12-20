"""
Taza argument qosasiz. search_num
>>> python main.py search_num
>>> Number:4507
>>> ('Ernazar','Jumaniyazov')
"""

import sys
from sqlite3 import *
from prettytable import from_db_cursor
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
        table= from_db_cursor(cursor)
        return table
    def search(self,name):
        cursor=self.db.cursor()
        cursor.execute(f"""SELECT * FROM contacts WHERE name='{name}' """)
        table=from_db_cursor(cursor)
        return table
    def search_num(self,num):
        cursor=self.db.cursor()
        cursor.execute(f"""
        SELECT* 
        FROM contacts
        """)

        contacts=cursor.fetchall()
        new_list=[]
        for contact in contacts:
            number=contact[2]
            if number[-4:] == num:
                new_list.append(contact)
        
        return new_list    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Only 1 argument required')
    
    commands=('add', 'list', 'search','search_num')
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
            print(contacts)
        elif command == 'search':
            name= input('Name:')
            contacts= contact.search(name)
            print(contacts)
        elif command =='search_num':
            num=input('Number: ')
            number=contact.search_num(num)
            print(number)