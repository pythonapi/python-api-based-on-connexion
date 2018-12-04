'''
Connects to the MySQL database.

Pypi documentation: https://pypi.org/project/PyMySQL/
PIP PyMySQL documentation: https://pymysql.readthedocs.io/en/latest/
'''
import pymysql.cursors

class Mysql():
    def __init__(self, db_host, db_user, db_password, db_name):
        # Connect to the database
        self.connection = pymysql.connect(host=db_host,
                                         user=db_user,
                                         password=db_password,
                                         db=db_name,
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor,
                                         autocommit=False)

    def execute_select(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def execute_insert(self, sql, parameters = ()):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, parameters)
        self.connection.commit()

    def execute_insert_bulk(self, sql, parameters = ()):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, parameters)

    def execute_delete(self, sql, parameters = ()):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, parameters)
        self.connection.commit()

    def commit(self):
        self.connection.commit()

    def open(self):
        return self.connection.open

    def close(self):
        self.connection.close()
