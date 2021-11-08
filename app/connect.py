import psycopg2

class Connect(psycopg2.extensions.connection):
    def __init__(self, host, user, password,dbname):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__dbname = dbname

        self.conn = psycopg2.connect(f'host={self.__host} user={self.__user} password={self.__password} dbname={self.__dbname}')

        self.cursor = self.conn.cursor()

    def execute_get(self, *args):
        self.cursor.execute(*args)
        return self.cursor.fetchall()

    def commited(self):
        self.conn.commit()

    def execute_insert(self, *args):
        #print("SQL : ", sql)
        #print("arg : ", arg)
        self.cursor.execute(*args)
        self.conn.commit()



#C = Connect('192.168.1.4','pi','inz178','sounder')

#C.cur.execute("""SELECT COUNT(*) FROM userdata WHERE nick='admins' and password='admins'""")
# C.cursor.execute("""SELECT * FROM userdata """)
# result = C.cur.fetchall()
# print(result)
# user = 'admins'
# password = '000000'


# print(C.execute("""SELECT COUNT(*) FROM userdata WHERE nick=(%s) and hash=(%s)""",(user,password)))



    #
    #
    # cur.execute('select * from userdata')
    #
    # results = cur.fetchall()
    #
    # for result in results:
    #     print(result)
    #
    # data=('admin')
    #
    #
    # SELECT
    # CASE when exists
    # (
    # SELECT * from userdata where nick='admin')
    # THEN 'TRUE'
    # ELSE 'FALSE'
    # END
    # ;
    #
    #
    # user = 'admins'
    # password = '000000'
    # #SELECT COALESCE((select column from table where condition1 and condition2), FALSE);
    #
    # #sql = "select TRUE from userdata where nick='admin'ELSE FALSE"
    # #sql = "SELECT COUNT(*) FROM userdata WHERE nick=(%s) and password=(%s)"
    # #sql ="SELECT TRUE IF COUNT(*) <= 1 FROM userdata WHERE nick='admin'"
    #
    # #sql='SELECT * from userdata WHERE %s IN nick'
    # data = [user,password]
    # #To dziala
    # cur.execute("""SELECT COUNT(*) FROM userdata WHERE nick=(%s) and password=(%s)""",(user,password))
    #
    # wartosc = cur.fetchall()
    # print(int(wartosc[0][0]))
    #
    # cur.execute("""SELECT COUNT(*) FROM userdata WHERE nick=(%s) and hash=(%s)""",(user,password))
    #
    # #ten dziala
    # #cur.execute("""SELECT COUNT(*) FROM userdata WHERE nick='admins' and password='admins'""")
    # wartosc = cur.fetchall()
    # print(int(wartosc[0][0]))

