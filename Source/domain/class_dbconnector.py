import sqlite3
from class_user import User


class DBConnector:
    _instance = None

    def __new__(cls, test_option=None):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, test_option=None):
        self.conn = None
        self.test_option = test_option

    def start_conn(self):
        if self.test_option is True:
            self.conn = sqlite3.connect('db_test.db')
        else:
            self.conn = sqlite3.connect('main_db.db')
        return self.conn.cursor()

    def end_conn(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def commit_db(self):
        if self.conn is not None:
            self.conn.commit()
        else:
            raise f"cannot commit database! {self.__name__}"

    def create_tables(self):
        c = self.start_conn()
        c.executescript("""
            DROP TABLE IF EXISTS user;
            CREATE TABLE "user" (
                "id"	INTEGER,
                "user_id"	VARCHAR(10),
                "user_pw"	VARCHAR(10),
                "nickname"	TEXT NOT NULL,
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            DROP TABLE IF EXISTS song;
            CREATE TABLE "song" (
                "song_id"	INTEGER,
                "title" varchar(30),
                "singer" varchar(30),
                "lyrics" TEXT,
                PRIMARY KEY("song_id" AUTOINCREMENT)
            );
            DROP TABLE IF EXISTS battle;
            CREATE TABLE "battle" (
                "battle_id"	INTEGER,
                "winner_id" INTEGER,
                "loser_id"	INTEGER,
                PRIMARY KEY("battle_id" AUTOINCREMENT)
            );
            DROP TABLE IF EXISTS battle_song;
            CREATE TABLE "battle_song" (
                "battle_song_id" INTEGER, 
                "battle_id" INTEGER, 
                "song_id" INTEGER,
                "answer_id" INTEGER, 
                PRIMARY KEY("battle_song_id" AUTOINCREMENT)
            );
        """)


    def insert_user(self, user_obj:User):
        c = self.start_conn()
        user_id = user_obj.user_id
        user_pw = user_obj.user_pw