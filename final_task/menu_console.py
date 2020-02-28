"""
Console menu
"""

import logging

my_log_console = logging.getLogger("menu_console")



def point_menu(numb):
    """
    Проверка правильности введенного пункта меню.
    param: cnt - Счетчик количества неправильно выбраных пунктов меню
    param: num_menu - Номер пункта меню
    param: numb - количество пунктов меню
    """
    def valid_input_menu(fn):
        def wrp_p_menu():
            cnt = 1
            while cnt <= 3:
                try:
                    num_menu = int(fn())
                    if (num_menu < 1 or num_menu > numb) and cnt < 3:
                        print(f"Введите пункт меню от 1 до {numb}")
                        cnt += 1
                    else:
                        return num_menu
                except ValueError:
                    print("Введите пункт меню с использование цифр")
                    cnt += 1
            my_log_console.info(f"Попытка правильного ввода пункта меню {cnt}")
        return wrp_p_menu
    return valid_input_menu


@point_menu(3)
def menu_search():
    """Меню выбора поля для поиска записи в библиотеке"""
    print("Выбирите поле поиска.\n\
          1. Код книги\n\
          2. Фамилия автора\n\
          3. Наименование книги")
    p_menu = input()
    return p_menu


@point_menu(5)
def menu_library():
    """Пункты консольного меню."""
    print("Выберете пункт меню:\n\
           1. Поиск книги в библиотеке\n\
           2. Добавить книгу\n\
           3. Удалить книгу\n\
           4. Редактировать запись о книге\n\
           5. Выход") # TODO: Добавить книгу из файла
    p_menu = input()
    return p_menu


@point_menu(4)
def main_menu():
    """Пункты основного консольного меню."""
    print("Выберете пункт меню:\n\
           1. Создать новую библиотеку\n\
           2. Удалить библиотеку\n\
           3. Просмотреть библиотеку\n\
           4. Выход")
    p_menu = input()
    return p_menu
