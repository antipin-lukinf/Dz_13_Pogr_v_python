#Задание №3
#📌 Создайте класс с базовым исключением и дочерние классы-
#исключения:
#○ ошибка уровня,
#○ ошибка доступа.

class ErrorDefault(Exception):
    def __init__(self, *args:object) -> None:
        super().__init__(self)


    def __str__(self, string:str='') -> str:
        return 'Родитель'
    
class ErrorLevel(ErrorDefault):
    def __init__(self):
        super().__init__(self)

    def __str__(self) -> str:
        return 'Error level'
    
class ErrorAcces(ErrorDefault):
    def __str__(self) -> str:
        return 'Error Acces'
    
lev = 1
if lev != 1:
    raise ErrorAcces(f'Уровень доступа недостаточен, уровень доступа {lev}')