import time
import logging

from structure_driver import IStructureDriver
from observer import Observer, Subject

my_log_lib = logging.getLogger("library") # привязка методов к модулю




class Book(Subject):
    
    """
    Format Book: {"id": '', # в качестве id используется ISBN, УДК, ББК и др. индентификационные обозначения
                  "last_name": '',
                  "first_name":'',
                  "title": '',
                  "series": '',
                  "volume": '',
                  "year": '',
                  "note": ''}
    field: id, title and year must be always
    """
    
    def __init__(self, kwargs):
        super().__init__()
        kwargs = self.__valid_field_record(kwargs)
        self.__id = kwargs['id']
        self.__last_name = kwargs['last_name']
        self.__first_name = kwargs['first_name']
        self.__title = kwargs['title']
        self.__series = kwargs['series']
        self.__volume = kwargs['volume']
        self.__year = kwargs['year']
        self.__note = kwargs['note']
        self.notify()

    
    @staticmethod
    def __valid_field_record(kwargs):
        """
        Проверка заполнения полей id и title, корректности данных поля year
        Дозаполнение отсутвующих полей
        """
        NAME_COLUMN = ("id", # в качестве id используется ISBN, УДК, ББК и др. индентификационные обозначения
                       "last_name",
                       "first_name",
                       "title",
                       "series",
                       "volume",
                       "year",
                       "note")
        while True:
            try:
                if kwargs["id"] and int(kwargs["year"]) <= int((time.ctime()).split()[4]):
                    break
                elif not kwargs["id"]:
                    kwargs["id"] = input("Укажите ISBN (УДК, ББК, и т.д.): ")
                elif not kwargs["title"]:
                    kwargs["title"] = input("Укажите название книги: ")
                elif int(kwargs["year"]) > int((time.ctime()).split()[4]):
                    kwargs["year"] = input(f"Введеный год больше текущего: ")
            except ValueError:
                kwargs["year"] = input(f"Неверный формат года: ")
        # заполнение полей пустыми строками, не все поля переданы
        for name in NAME_COLUMN:
            if not name in kwargs.keys():
                kwargs[name] = ''
        return kwargs


    @property
    def id_(self):
        return self.__id
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def title(self):
        return self.__title
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def series(self):
        return self.__series
    
    @property
    def volume(self):
        return self.__volume
    
    @property
    def year(self):
        return self.__year
    
    @property
    def note(self):
        return self.__note

    
    def __str__(self):
        return f"\
        id:{'':12} -> {self.__id}\n\
        first_name:{'':4} -> {self.__first_name}\n\
        last_name:{'':5} -> {self.__last_name}\n\
        title:{'':9} -> {self.__title}\n\
        series:{'':8} -> {self.__series}\n\
        volume:{'':8} -> {self.__volume}\n\
        year:{'':10} -> {self.__year}\n\
        note:{'':10} -> {self.__note}"


class Library(IStructureDriver, Observer):
        
    def __init__(self, structure_driver=None):
        self.__libr = set()
        self.__records = 0
        self.__structure_driver = structure_driver
    
    @property
    def num_records(self):
        return self.__records
    
    def __to_dict(self):
        res = []
        for rec in self.__libr:
            res.append({'id': rec.id_,
                        'last_name': rec.last_name,
                        'first_name': rec.first_name,
                        'title': rec.title,
                        'series': rec.series,
                        'volume': rec.volume,
                        'year': rec.year,
                        'note': rec.note})
        return res
    
    def __to_library(self, list_):
        if not list_:
            for val in list_:
                self.add_book(val)
        return self

    @staticmethod
    def input_data() -> dict:
        """Ввод данных пользователем"""
        base = {}
        base["id"] = (input("Введите индентификационный код (ISBN, УДК, ББК) книги: ")).strip()
        base["last_name"] = (input("Введите фамилию автора книги: ")).strip()
        base["first_name"] = (input("Введите имя автора книги: ")).strip()
        base["title"] = (input("Введите название книги: ")).strip()
        base["series"] = (input("Введите серию книг: ")).strip()
        base["volume"] = (input("Введите том: ")).strip()
        base["year"] = (input("Введите год издания: ")).strip()
        base["note"] = (input("Введите примечание: ")).strip()
        return base if base["id"] and base["title"] else input_data()

    def add_book(self, book):
        """
        Add new book
        Exception:
            Record about book must be dict 
        """
        if not isinstance(book, dict):
            raise TypeError("Book must be dict")
        new_book = Book(book)
        # проверка отсутсвия книги по id
        if not self.find_book(['id', new_book.id_]):
            self.__libr.add(new_book)
            self.__records += 1
            new_book.add_observer(self)
            my_log_lib.info(f"Добавлена запись {str(new_book)}")
            self.update()
        else:
            return f"Такая запись уже существует"
    
    def find_book(self, field: list) -> dict:
        """
        Search books for field: id, title, last_name
        param: field: list - name field and value ['id', '123']
        """
        if not isinstance(field, list):
            raise TypeError("Field must be list")
        if len(field) != 2 and (field[0] not in ['id', 'title', 'last_name']):
            raise ValueError("field must be 2 value, or field[0] must be id, title, last_name")
        ind: int = 1 # индекс записи в результатах поиска
        result: dict = {} # результаты поиска
        for rec in self.__libr:
            var_find = {'id': rec.id_,
                        'last_name': rec.last_name,
                        'title': rec.title} # соответсвие полей поиска
            if var_find[field[0]] == field[1]:
                result[ind] = rec
                ind += 1
        return result if result else None

    def del_book(self, field_id: str) -> None:
        """
        Delete record about book 
        param: field_id - value id
        """
        if not isinstance(field_id, str):
            raise TypeError("field_id must be string")
        del_book = self.find_book(['id', field_id])
        del_book[1].remove_observer(self)
        self.__libr.remove(del_book[1])
        self.__records -= 1
        
        print(f"Запись о книге {del_book[1].title} - удалена")
        my_log_lib.info(f"Запись о книге {del_book[1].title} удалена")
        self.update()
    
    def edit_book(self, field_id: str) -> None:
        """
        Edit field of book
        param: field_id - value id
        """
        edit_book = self.find_book(['id', field_id])
        print(edit_book[1])
        new_book = self.input_data()
        y_n = input("Введите 'y/n' для применения изменений: ")
        if y_n == 'y':
            self.del_book(field_id)
            self.add_book(new_book)
            print(f"Запись о книге {edit_book[1].title} - изменена")
            my_log_lib.info(f"Запись о книге {edit_book[1].title} - изменена")
        self.update()
    
    @staticmethod
    def print_result_search(data: dict) -> None:
        """
        Вывод найденых записей на экран
        param: data - данные о книге
        """
        for ind, val in data.items():
            print(f"Запись номер {ind}")
            print(val)
            print("-"*50)
    
    def set_structure_driver(self, structure_driver):
        self.__structure_driver = structure_driver
    
    def save(self):
        self.__structure_driver.write(self.__to_dict())
    
    def load(self):
        self.__to_library(self.__structure_driver.read())
        
    def update(self):
        print("Данные обнавлены")
        self.save()
        my_log_lib.info(f"Данные в библиотеке обнавлены")
