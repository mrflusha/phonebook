#!/usr/bin/python 
import mariadb
import sys
from time import sleep as sl

mail = []
users = []
mails_q = "SELECT email FROM users"
users_q = "SELECT login FROM users"
data_q = "select name, phone_num, bd, id from phonebook where user_id = ?"
auth_q = "SELECT id FROM users WHERE login = ? AND password = ?"
add_contact_q = "INSERT INTO phonebook(user_id,name,phone_num,bd) VALUES(?,?,?,?)"
buttons_q = "SELECT name FROM phonebook WHERE name LIKE '?%'"


test_login = "admin"
test_pw = "password"

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
            print("\t",table_data, end = "\t")
            return table_data
        
    td = table_data(data_q,1)
    td_phone,td_name, td_bd = list(),list(),list()
    print(td)
    for i in range(len(td)):
        td_name = td[i][0]
        td_phone = td[i][1]
        td_bd = td[i][2]
        print("\nимя:",td_name,
            "Телефон:",td_phone,
            "Дата рождения:",td_bd,"\n")
    def auth(q, login, pw):
        with conn.cursor() as cur:
            try:
                cur.execute(q,(login,pw))
                user_id = cur.fetchall()

                if len(user_id) != 0:
                    user_id = user_id[0][0]
                else:
                    user_id = False                
                print (user_id)
                return user_id
            except mariadb.Error as e:
                print(f"Error connecting to MariaDB Platform: {e}")
    def add_contact(user_id,name,phone_num,bd):
        with conn.cursor() as  cur:
            
            cur.execute(add_contact_q,(user_id,name,phone_num,bd))
    def get_contacts(q,arr,user_id):
        print(q)
        
        with conn.cursor() as cur:
#            conn.commit() 
            cur.execute(q, (user_id,))
            print(cur)
            for row in cur:
                arr.append(row[0])
            
#        conn.close()
        print(arr)
        return arr

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor

A = []


test_q = "SELECT * FROM users;"
test_arr = []
test_select = "SELECT login from users Where id = 1"
butt_id = list()
butt_name = list()
butt_phone = list()
butt_bd = list()
id_q = "SELECT id from phonebook where user_id = ?"
name_q = "SELECT name from phonebook where user_id = ?"
phone_q = "SELECT phone_num from phonebook where user_id = ?"
bd_q = "SELECT bd from phonebook where user_id = ?"
get_contacts(id_q, butt_id,"1")
get_contacts(name_q, butt_name,"1")
get_contacts(phone_q, butt_phone,"1")
get_contacts(bd_q, butt_bd,"1")
print("ID = ",butt_id,"name = ", butt_name, "phone = ", butt_phone, "birthday = ", butt_bd)


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
    auth(auth_q,test_login,test_pw)
    auth(auth_q,test_login,"0")


except mariadb.Error as e:
    print(f"Error: {e}")
#finally:
#    conn.close()





#test_q2 = "SELECT login FROM users Where id = "+str(test_arr[0])
#print(test_q2)
#sql(test_q,test_arr)
#print(test_arr)

