import psycopg2

conn = psycopg2.connect('host=192.168.1.4 user=pi password=inz178 dbname=sounder')

cur = conn.cursor()

cur.execute('select * from userdata')

results = cur.fetchall()

for result in results:
    print(result)

data=('admin')

""""
SELECT
CASE when exists
(
SELECT * from userdata where nick='admin')
THEN 'TRUE'
ELSE 'FALSE'
END
;
"""

user = 'admins'
password = '000000'
#SELECT COALESCE((select column from table where condition1 and condition2), FALSE);

#sql = "select TRUE from userdata where nick='admin'ELSE FALSE"
#sql = "SELECT COUNT(*) FROM userdata WHERE nick=(%s) and password=(%s)"
#sql ="SELECT TRUE IF COUNT(*) <= 1 FROM userdata WHERE nick='admin'"

#sql='SELECT * from userdata WHERE %s IN nick'
data = [user,password]
#To dziala
cur.execute("""SELECT COUNT(*) FROM userdata WHERE nick=(%s) and password=(%s)""",(user,password))

wartosc = cur.fetchall()
print(int(wartosc[0][0]))

cur.execute("""SELECT COUNT(*) FROM userdata WHERE nick=(%s) and hash=(%s)""",(user,password))

#ten dziala
#cur.execute("""SELECT COUNT(*) FROM userdata WHERE nick='admins' and password='admins'""")
wartosc = cur.fetchall()
print(int(wartosc[0][0]))
