#Задание №1
#📌 Создайте функцию, которая запрашивает числовые данные от
#пользователя до тех пор, пока он не введёт целое или
#вещественное число.
#  📌 Обрабатывайте не числовые данные как исключения.

def number_input():
    while True:
        
        try:
            numb = input('Введите число : ')
            if '.' in numb:
                return float(numb)
            
            return int(numb)
               
        except ValueError as e:
            print('Ошибочное значение')
    
    
    

number_input()
    
