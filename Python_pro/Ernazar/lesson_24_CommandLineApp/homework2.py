from prettytable  import PrettyTable

table=PrettyTable()
table.field_names = ["name","surname","number"]
table.add_row(['Ernazar','Jumaniyazov','+998907144507'])
table.add_row(['Begis','Embergenov','+998918702085'])
table.add_row(['Alisher','Rustamov','+998905927700'])
table.add_row(['Yusup','Salimov','+998906530494'])
table.add_row(['Azizbek','Dawletbaev','+998977777777'])
table.add_row(['Erlan','Sarsenbaev','+998912598683'])
table.add_row(['Nurlan','Sarsenbaev','+998612245546'])
print(table)