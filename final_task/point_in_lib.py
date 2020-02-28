"""
Основной файл, запускающий программу
"""

import sys
import os
import logging
import argparse

# собственные модули
sys.path.append("./Modules/")  # добавлена папка с подключаемыми модулями
from menu_choice import MenuChoice
import menu_console as mn


# задание режима DEBUG или REALES 
pars_arg = argparse.ArgumentParser(description="")
pars_arg.add_argument('-order',
                      action='store',
                      type=str,
                      required=False,
                      help="Enter DEBUG if you want DEBUG order")
argum = pars_arg.parse_args(sys.argv[1:])
arg_d = 0 if argum.order == 'DEBUG' else 1
    

# Инициализация log-файла
FORMAT = "%(asctime)s --> %(name)s -> %(levelname)s -> %(message)s"
type_level = [logging.INFO, logging.DEBUG]
logging.basicConfig(filename="./application.log",
                    filemode="at",
                    format=FORMAT,
                    level=type_level[arg_d])
my_log_point = logging.getLogger("point_in_lib")


# создание папки db
if not os.path.isdir('./db'):
    os.mkdir('./db')


def main_progr():
    """Обработка основного меню"""
    my_log_point.info("App start")
    
    while True:
        first = mn.main_menu()
        if first == 4:
            my_log_point.info("App end")
            print("Досвидания")
            break
        menu = MenuChoice()
        dict_menu = {1: menu.create_lib,
                     2: menu.delete_lib,
                     3: menu.view_lib,
                     }
        dict_menu[first]()


if __name__ == "__main__":
    try:
        main_progr()
    except Exception as exc:
        if arg_d:
            my_log_point.info(exc)
        else:
            my_log_point.debug(exc)

