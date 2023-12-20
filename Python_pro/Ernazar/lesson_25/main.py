import sys
from sqlite3 import *
import time
from prettytable import from_db_cursor

class MoneyController:
    def __init__(self,db) :
        self.db=db
        cursor= self.db.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS spends (date,money)
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS earns (date,money)
        """)
    
    def spend_money(self,money):
        date=time.strftime('%Y-%n-%d %H:%N:%5')
        cursor=self.db.cursor()
        cursor.execite(f"""
        INSERT INTO earns (date,money)
        VALUES ('{date}','{money}')
        """)
    def earn_money(self,money):
        date=time.strftime('%Y-%n-%d %H:%N:%5')
        cursor=self.db.cursor()
        cursor.execute(f"""
        INSERT INTO earns (date,money)
        VALUES ('{date}','{money}')
        """)
    def get_history_spends(self):
        cursor=self.db.cursor()
        cursor.execute("""
        SELECT *
        FROM spends
        """)
        return from_db_cursor(cursor)
    def get_history_earns(self):
        cursor = self.db.cursor()
        cursor.execute("""
        SELECT *
        FROM earns
        """)
    def balance(self):
        cursor=self.db.cursor()
        cursor.execute("""
        SELECT *
        FROM spends
        """)
        spends = cursor.fetchall()
        spends_sun = 0
        for spend in spends:
            spends_sun+=int(spend[1])
        
        cursor.execute("""
        SELECT *
        FROM earns
        """)
        earns = cursor.fetchall()
        earns_sun=0
        for earn in earns:
            earns_sum += int(earn[1])
        
        return f'Balance: {earns_sun - spends_sun}'
if __name__  == '__main__':
    command = sys.argv[1:]

    with connect('controlmoney.db') as db:
        controller = MoneyController(db)

        if command[0] == 'spend':
            controller.spend_money(command[1])
            print(f'{command[1]}  sum aqsha sawdiniz')
        
        elif command[0] == 'earn':
            controller.earn_money(command[1])
            print(f'{command[1]} sum aqsha tawdiniz')
        
        elif command[0] == 'balance':
            print(controller.balance())
        
        elif command[0] == 'spends':
            print(controller.get_history_spends())
        
        elif command[0] == 'earns':
            print(controller.get_history_earns())

