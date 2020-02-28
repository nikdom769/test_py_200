"""
Классы меню и подменю
"""
import os
import logging

from library import Library
#from structure_driver import *
from builders import SDFabric #, CSVBuilder, JSONFileBuilder
import menu_console as mn


my_log_menu = logging.getLogger("menu") # привязка методов к модулю


class SubMenuChoice:
    """
    Menu Library
    """
    def __init__(self, library):
        if not isinstance(library, Library):
            raise TypeError("Var Library must be Library")
        self.__lib = library
    
    def add_record(self):
        book = Library.input_data()
        self.__lib.add_book(book)
        
    def search_record(self):
        n = mn.menu_search()
        # Соответсвие пунктов меню и обозначениям в словаре
        field_search = {1: "id",
                        2: "last_name",
                        3: "title",
                        }
        text = input("Введите значение поля: ")
        res = self.__lib.find_book([field_search[n], text])
        if res:
            self.__lib.print_result_search(res)
            return res
        else:
            print("Записей о книге не найдено")

    def delete_record(self):
        results = self.search_record()
        field_id = results[1].id_
        if len(results) > 1:
            field_id = input("Уточните id книги: ")
        self.__lib.del_book(field_id)
        
    def edit_record(self):
        results = self.search_record()
        if len(results) > 1:
            field_id = input("Уточните id книги: ")
            self.__lib.edit_book(field_id)
        elif len(results) == 1:
            field_id = results[1].id_
            self.__lib.edit_book(field_id)


class MenuChoice:
    """
    Main menu
    """    

    def create_lib(self):
        self.__lib = Library()
        driver_name = input("Введите тип библиотеки\
                            (формат: .csv или .json) >")
        builder = SDFabric.get_sd_driver(driver_name)
        self.__lib.set_structure_driver(builder.build())
        self.__lib.save()
        print("Создана библиотека")
        my_log_menu.info("Создана библиотека")
        self.addit_menu(self.__lib)
        
    def delete_lib(self):
        filename = input("Введите имя файла > ")
        if os.path.isfile(f"./db/{filename}"):
            os.remove(f"./db/{filename}") # удаление файла с библиотекой
            print("Удалена библиотека")
            my_log_menu.info("Удалена библиотека")
        else:
            my_log_menu.info(f"Файла {filename} нет")
            print("Файла с таким именем нет")
   
    def view_lib(self):
        f_name = ['test_01.csv']
        #f_name for _, _, name in os.walk("./db/")] # список файлов
                                                            # папки db
        self.__lib = Library()
        if len(f_name) > 1:
            # если в архиве больше одной библиотеки
            for name in f_name:
                print(name)
            #self.__lib = Library()
            driver_name = input("Введите тип библиотеки\
                                (формат: .csv или .json) >")
            builder = SDFabric.get_sd_driver(driver_name)
            self.__lib.set_structure_driver(builder.build())
            #self.__lib.load()
            #if not self.__lib.num_records:
            #    print("Библиотека пуста")
        else:
            print(f_name[0].split('.')[1])
            builder = SDFabric.get_sd_driver(f_name[0].split('.')[1])
            print(f_name[0])
            self.__lib.set_structure_driver(builder.build(f_name[0]))
        self.__lib.load()
        if not self.__lib.num_records:
            print("Библиотека пуста")
        self.addit_menu(self.__lib)
    
    
    def addit_menu(self, libr: Library):
        """Method make submenu"""
        while True:
            n = mn.menu_library()
            if n == 5:
                break
            sub_menu = SubMenuChoice(self.__lib)
            dict_sub_menu = {1: sub_menu.search_record,
                             2: sub_menu.add_record,
                             3: sub_menu.delete_record,
                             4: sub_menu.edit_record,
                             }
            dict_sub_menu[n]()
