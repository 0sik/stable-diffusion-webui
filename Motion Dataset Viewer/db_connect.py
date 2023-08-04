import pymysql
import os

class ConnectDB:


    def __init__(self, sql):
        self.sql = sql  
        self.data = None

        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='motionai', charset='utf8',
                                    autocommit=True) 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor) 

    
    def execute(self, *args):
        self.curs.execute(self.sql, args)
        self.conn.commit()

        
    def fetch(self):
        self.curs.execute(self.sql)
        self.data = self.curs.fetchall()
        return self.data


    def __del__(self):
        self.curs.close() 
        self.conn.close()  

    def connect():
            return pymysql.connect(host='localhost', user='root', password='1234', db='motionai', charset='utf8',
                                autocommit=True) 
