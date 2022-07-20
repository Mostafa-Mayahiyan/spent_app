#import sqlite3  framework for making database and give it to db value for calling easier 
import sqlite3 as db
#import datetime framework and import datetime function for showing date and time
from datetime import datetime as dt
# create a database file with the name of spent and give it to conn value
conn = db.connect('spent.db')
#create cursor and give it to cur value 
cur = conn.cursor()

#create a function for making a table for database 
def init():
    cur.execute('''CREATE TABLE IF NOT EXISTS socket (
         
         name TEXT  COLLATE NOCASE,
         price REAL,
         date TEXT NULL,
         massage TEXT 
    )''')
    #save table 
    conn.commit()
    #close function after calling 
    cur.close()
    



#create a value and calling datetime function and calling now function for showing Present time then calling strftime function for what showing.
dt1 = dt.now().strftime("%Y-%m-%d | %H:%M:%S")
#create insert function for giving data to the table of database and it should take some data from user expcet massage and time as massage is  equal to empty and dt i gave dt1 
# for showing present time in any data who user gives. 
def insert(name,price,massage='',dt=dt1):
    with conn:
       cur.execute('INSERT INTO socke VALUES (:Name,:price,:massage,:Date)',{'Name':name,'price':price,'massage':massage,'Date':dt})
       conn.commit()


#create delete function for removing data from data base and it takes name for removing
def delete(name):
  with conn:
    cur.execute('DELETE FROM socket WHERE name =:name',{'name':name})
    conn.commit()

#create a fuction for introduce myself xD
def aboutme():
  return """hello i'm Mostafa Mayahiyan And a bigganer programmer ,
  my hometown is Iran,Abadan City and it is my first project
   i hope it was helpful for you..(: """

#create show function for showing result and take name value from user but if user didn't give it to function it be none 
# and it shows all of data base to user 
def show(name=None):
    with conn:
      if name:
        cur.execute('SELECT * FROM socket WHERE name = (:name)',{'name':name})
        write = cur.fetchall()
        cur.execute('SELECT sum(price) FROM socket WHERE name=(:name)',{'name':name})
        trsult = cur.fetchall() [0]

      else:
        cur.execute('SELECT * FROM socket')
        write = cur.fetchall()
        cur.execute('SELECT sum(price) FROM socket ')
        trsult = cur.fetchall() [0]
      return trsult,write

        





