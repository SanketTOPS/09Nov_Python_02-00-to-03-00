import pymysql

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='hellodb')
    print("Database connected!")
except Exception as e:
    print(e)
   
cr=db.cursor() 
    
#Table Create
create_tbl="create table studinfo(id integer primary key auto_increment, name text, city text)"

try:
    cr.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)
    
#Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('nirav','baroda'),('ashok','ahmedabad'),('bhavin','bhavnagar'),('jatin','jamnagar')"

try:
    cr.execute(insert_data)
    db.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)"""
    

#Update Data
update_data="update studinfo set name='prasiddh',city='surat' where id=5"

try:
    cr.execute(update_data)
    db.commit()
    print("Record Updated!")
except Exception as e:
    print(e)