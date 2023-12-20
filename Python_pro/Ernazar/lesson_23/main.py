from sqlite3 import * 



def create_table(name):
    with connect('contacts.db') as db:
        cursor = db.cursor()
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {name} (
                first_name,
                last_name,
                phone_number
                )
            """
        )

def add_data(table, data):
    with connect('contacts.db')as db:
        cursor =db.cursor()
        cursor.execute(
            f"""
            INSERT INTO {table} (first_name,last_name,phone_number)
            VALUES {data}
            """
        ) 

def get_datas(table):
    with connect('contacts.db') as db :
        cursor=db.cursor()
        cursor.execute(
            f"""
            SELECT *
            FROM {table}
            """
        )
        rows = cursor.fetchall()
        return rows
    
def get_one_data(table, name):
    with connect('contacts.db') as db :
        cursor=db.cursor()
        cursor.execute(
            f"""
            SELECT *
            FROM {table}
            WHERE first_name ='{name}'
            """
        )
        rows = cursor.fetchone()
        return rows

#create_table('users')
#add_data('users', ("Ernazar", "Jumaniyazov","+998907144507"))
#print(get_datas('users'))
#print(get_one_data('users', 'Yusup'))
