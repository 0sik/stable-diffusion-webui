import pymysql
import os

class ConnectDB:

    # 인스턴스 초기화
    def __init__(self, sql):
        self.sql = sql  
        self.data = None

        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='motionai', charset='utf8',
                                    autocommit=True)  # DB와 연결합니다.
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)  # sql문 수행을 위해 cursor 객체를 생성합니다.

    
    def execute(self, *args):
        self.curs.execute(self.sql, args)
        self.conn.commit()

        
    def fetch(self):
        self.curs.execute(self.sql)
        self.data = self.curs.fetchall()
        return self.data

    # 인스턴스 삭제
    def __del__(self):
        self.curs.close()  # cursor 객체를 닫습니다.
        self.conn.close()  # DB연결을 해제합니다.

    def connect():
            return pymysql.connect(host='localhost', user='root', password='1234', db='motionai', charset='utf8',
                                autocommit=True)  # Connect to the MySQL database.