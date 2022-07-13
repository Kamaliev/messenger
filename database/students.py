import datetime

from database import Database


class Students:
    def __init__(self):
        self.__db = Database()

    def add(self, first_name, last_name, login, password):
        print(first_name, last_name, login, password)
        query = '''insert into Students (first_name, last_name, login, password, time, online) VALUES (?, ?, ?, ?, ?, ?)'''
        time = datetime.datetime.now()
        self.__db.execute(query, first_name, last_name, login, password, time, time)

    def check(self, login, password):
        query = '''select * from Students where login = ? and password = ?'''
        result = self.__db.get_results(query, login, password)
        return len(result) > 0

    def check_login(self, login):
        query = '''select * from Students where login = ?'''
        result = self.__db.get_results(query, login)
        return len(result) > 0

    def get_username(self, login):
        query = '''select first_name || ' ' || last_name from Students where login = ?'''
        result = self.__db.get_result(query, login)
        if result is not None:
            return result[0]

    def get_online(self):
        query = '''select count(*) from Students where online>= ?'''
        result = self.__db.get_result(query, datetime.datetime.now()-datetime.timedelta(seconds=5))
        if result:
            return result[0]
        return 0

    def update_online(self, login):
        query = '''update Students set online = ? where login = ?'''
        self.__db.execute(query, datetime.datetime.now(), login)

if __name__ == '__main__':
    students = Students()
    students.add('Asf', 'ASdf')
