#!/usr/bin/python 
import mariadb
import sys
from time import sleep as sl

mail = []
users = []
mails_q = "SELECT email FROM users"
users_q = "SELECT login FROM users"
data_q = "SELECT * FROM phonebook WHERE user_id = ?"

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="1337",
        host="localhost",
        port=3306,
        database="phonebook",
        autocommit = True

    )
    #conn.autocommit = False
    
    def sql(q,arr):
        print(q)
        
        with conn.cursor() as cur:
#            conn.commit() 
            cur.execute(q)
            print(cur)
            for row in cur:
                arr.append(row[0])
            
#        conn.close()
        print(arr)
        return arr
    def add_sql(login,email,password,date):
#        conn.commit()

            if email in mail:
                print("try other email")
            elif login in users:
                print("try other name")
            else:
                with conn.cursor() as cur:
                    try:
                        cur.execute("INSERT INTO users(login,email,password,bd) VALUES(?,?,?,?)",(login,email,password,date))
                    except mariadb.Error as e:
                            print(f"Error connecting to MariaDB Platform: {e}")
    def table_data(q,db_id):
        with conn.cursor() as cursor:
            print(q,db_id)
            conn.commit()
            cursor.execute(q,(db_id,))
            table_data = cursor.fetchall()
            print(table_data[1][2])
        
    table_data(data_q,1)

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor

A = []


test_q = "SELECT * FROM users;"
test_arr = []
test_select = "SELECT login from users Where id = 1"
try:
    sql(test_q,test_arr)
    sql(test_select, test_arr)
    mails = sql("SELECT email FROM users",mail)
    users = sql("SELECT login FROM users",users)
    print(test_arr)
    print("prev:",users,mails)
    add_sql("vaslystry:ha","vasiligi@10emin.eu","1234","05.05.2000")

    print("post",mails,users)
    #conn.commit()
except mariadb.Error as e:
    print(f"Error: {e}")
#finally:
#    conn.close()





#test_q2 = "SELECT login FROM users Where id = "+str(test_arr[0])
#print(test_q2)
#sql(test_q,test_arr)
#print(test_arr)

