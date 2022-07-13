import datetime

from database import Database


class Events:
    def __init__(self):
        self.__db = Database()

    def get(self, id):
        query = '''select 
                   ev.id,
                   st.first_name || ' ' || st.last_name as full_name,
                   ev.time,
                   ev.text
            from Events as ev
            JOIN Students st ON ev.user_id == st.id
            where ev.id > ?
            order by ev.time'''
        return self.__db.get_results(query, id)

    def add(self, user, text):
        time = datetime.datetime.now()
        query = '''insert into Events (text, time, user_id) VALUES (?, ? , (select id from Students where login = ?))'''
        self.__db.execute(query, text, time, user)

    def drop(self):
        query = '''delete from Events where id >0'''
        self.__db.execute(query)


if __name__ == '__main__':
    Events().add(1, 'Ну здравствуй')
