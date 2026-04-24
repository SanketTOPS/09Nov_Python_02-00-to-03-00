import sqlite3

try:
    db=sqlite3.connect("testdb.db")
    print("Database connected!")
except Exception as e:
    print(e)
    
#Table Create
create_tbl="create table studinfo(id integer primary key autoincrement, name text, city text)"

try:
    db.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)
    
#Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('nirav','baroda'),('ashok','ahmedabad'),('bhavin','bhavnagar'),('jatin','jamnagar')"

try:
    db.execute(insert_data)
    db.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)"""
    
#Insert_Input
n=int(input("Enter number of students:"))
for i in range(n):
    name=input("Enter your name:")
    city=input("Enter your city:")
    insert_data=f"insert into studinfo(name,city)values('{name}','{city}')"
    
    try:
        db.execute(insert_data)
        db.commit()
        print("Resord Inserted!")
    except Exception as e:
        print(e)
    

#Update Data
"""update_data="update studinfo set name='prasiddh',city='surat' where id=5"

try:
    db.execute(update_data)
    db.commit()
    print("Record Updated!")
except Exception as e:
    print(e)"""
    
#Delete Data
"""delete_data="delete from studinfo where id=4"

try:
    db.execute(delete_data)
    db.commit()
    print("Record Deleted!")
except Exception as e:
    print(e)"""
    
#Show Data
cr=db.cursor()
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(2)
    #data=cr.fetchone()
    #print(data)
    for i in data:
        print(i)
except Exception as e:
    print(e)