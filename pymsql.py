import pymysql


db = pymysql.connect(host='localhost',user = 'root',\
							 password='1337',\
							 db='phonebook',\
							 autocommit = True
							 )


db_str = "INSERT INTO users(login,password,bd) values('hell','wrote','06.06.2006')"
sel_str = "SELECT * FROM users"
print(db_str)
a = []

try:
	with db.cursor() as cur:
		cur.execute(db_str)
		cur.execute(sel_str)
		for row in cur:
			a.append(row[1])

		for i in a:
			print(i)
		print(a,"prev")
		cur.execute(sel_str)
		print(a)

		cur.close()
except pymysql.error as e:
	print(e)
finally:
	db.close