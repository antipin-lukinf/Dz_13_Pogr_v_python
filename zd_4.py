"""
Задание №4
📌 Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
📌 Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
📌 Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
"""

import json
import random


class User():
    

    def __init__(self, name=' ', id=0, acces_level=0):
        self.name = name
        self.id = id
        self.acces_level = acces_level
        self.users_list = []
    
    def user_input(self):
        user_list = []
        users_list = []
        while True:
            try:
                name = input('Name: ')
                if not str.istitle(name):
                    raise ValueError
            
            except Exception as e:
                print(e)

            if not name:
                for i in user_list:
                    users_list.append(User(*i))
                self.users_list = users_list
                break
            while True:
                user_id = random.randint(10_000, 100_000)
                if user_id not in [uid[2] for uid in user_list]:
                    break

            while True:
                lvl = input('Lvl: ')
                if lvl.isdigit() and 0 < int(lvl) < 8:
                    user_list.append((name, user_id, lvl))
                    break
    
    def __str__(self) -> str:
        return f'{self.name}  {self.acces_level}    {self.id}'
    
    def get_info(self):
        return [(user.name, user.id, user.acces_level) for user in self.users_list]
    
    

     
    def json_write(self, file_name):
        
        result_dict = {}

        for user in self.users_list:

            result_dict[user.id] = [user.name, user.acces_level]

        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(result_dict, f, indent=4, ensure_ascii=False)

    def json_read(self, file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                new_dict = json.load(f)
        except EOFError as e:
            print(e)

        for key in new_dict:
            self.users_list.append(User(new_dict[key][0], key, new_dict[key][1]))
    
    def log_id(self, name, input_id):
        work_list = self.get_info()
        for value in work_list:
            if name in value:
                self.name = value[0]
                self.id = value[1]
                self.acces_level = value[2]
                return self.acces_level
                
        raise Exception('В доступе отказано')
    
    def create_new_user(self, name, lvl):
        if int(self.acces_level) < lvl:
            raise Exception('Уровень доступа не достаточен')
        while True:
            user_id = random.randint(10_000, 100_000)
            if user_id not in [uid.id for uid in self.users_list]:
                self.users_list.append(User(name, user_id, lvl))
                break






new_user = User('', '', '')
"""new_user.user_input()
new_user.json_write() """

new_user.json_read('result_users.json')
for i in new_user.users_list:
    print(i)

print(new_user.get_info())
print(new_user.log_id('w', 44918))
new_user.create_new_user('ERTYY', 2)
print(new_user.get_info())

