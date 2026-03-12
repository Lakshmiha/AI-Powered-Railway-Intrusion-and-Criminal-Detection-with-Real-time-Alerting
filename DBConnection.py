<<<<<<< HEAD

=======
>>>>>>> 3c4cc6b3de07162dc0e1212019925b8bfada673d
import pymysql

class Database:

    def __init__(self):
        self.cnx = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="railwayobject",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.cnx.cursor()

    def select(self, q):
        self.cur.execute(q)
        return self.cur.fetchall()

    def selectOne(self, q):
        self.cur.execute(q)
        return self.cur.fetchone()

    def insert(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.lastrowid

    def update(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.rowcount

    def delete(self, q):
        self.cur.execute(q)
        self.cnx.commit()
<<<<<<< HEAD
        return self.cur.rowcount

# import mysql.connector
#
#
# class Database:
#
#     def __init__(self):
#
#         self.cnx = mysql.connector.connect(host="localhost",user="root",password="root",database="railwayobject")
#         self.cur = self.cnx.cursor(dictionary=True)
#
#
#     def select(self, q):
#         self.cur.execute(q)
#         return self.cur.fetchall()
#
#     def selectOne(self, q):
#         self.cur.execute(q)
#         return self.cur.fetchone()
#
#
#     def insert(self, q):
#         self.cur.execute(q)
#         self.cnx.commit()
#         return self.cur.lastrowid
#
#     def update(self, q):
#         self.cur.execute(q)
#         self.cnx.commit()
#         return self.cur.rowcount
#
#     def delete(self, q):
#         self.cur.execute(q)
#         self.cnx.commit()
#         return self.cur.rowcount
#
=======
        return self.cur.rowcount
>>>>>>> 3c4cc6b3de07162dc0e1212019925b8bfada673d
