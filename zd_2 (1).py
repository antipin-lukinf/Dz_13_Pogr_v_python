#Задание №2
#📌 Создайте функцию аналог get для словаря.
#📌 Помимо самого словаря функция принимает ключ и
#значение по умолчанию.
#📌 При обращении к несуществующему ключу функция должна
#возвращать дефолтное значение.
#📌 Реализуйте работу через обработку исключений.

def get_val_in_dict(dict_work:dict, key, defoult_value):
    try:
        return dict_work[key]
    except Exception:
        return defoult_value
    
dic = {1:2, 3:4}
print(get_val_in_dict(dic, 3, 0))
    