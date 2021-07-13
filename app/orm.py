import sqlite3

from django.http import HttpRequest


# Создание пользователя в бд для таблицв ContactUs
class ContactUs:

    # Создаем инициализатор с тремя полями нашей модели
    def __index__(self, email, subj, mess):
        self.email = email
        self.subj = subj
        self.mess = mess

    # Создание вручную CRUD - операция
    # Функция  чтение пользователя
    def select_contact(self):
        con = sqlite3.connect('db.sqlite3')
        cur = con.cursor()
        sql_quary = '''
            SELECT * FROM ContactUs
        '''
        cur.execute(sql_quary)
        con.commit()
        con.close()
        return 'print contact info'

    #   Функция создание пользователя
    def create_contact(self):
        con = sqlite3.connect('db.sqlite3')
        cur = con.cursor()
        sql_query = f'''
            INSERT INTO ContactUs (email_form, subject, message)
            VALUES ({self.email}, {self.subj}, {self.mess});
        '''
        cur.execute(sql_query)
        con.commit()
        con.close()
        return 'Create new contact'

    # Функция обновление пользователя
    def update_contact(self):
        con = sqlite3.connect('db.sqlite3')
        cur = con.cursor()
        sql_quary = '''    '''
        cur.execute(sql_quary)
        con.commit()
        con.close()
        return 'print contact info'

    # Функция удаление пользователя
    def delete_contact(self):
        con = sqlite3.connect('db.sqlite3')
        cur = con.cursor()
        sql_quary = '''   '''
        cur.execute(sql_quary)
        con.commit()
        con.close()
