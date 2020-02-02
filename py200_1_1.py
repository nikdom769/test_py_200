# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Домичев Н.Н.

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class Glass:

    def __init__(self, capacity_volume, occupied_volume):
        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume
            else:
                raise ValueError ("Must be (0, inf)")
        else:
            raise TypeError ("Must be integer or float")

        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0 and occupied_volume <= self.capacity_volume:
                self.occupied_volume = occupied_volume
            else:
                raise ValueError ("Must be [0, capacity_volume]")
        else:
            raise TypeError ("Must be integer or float")


# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.

def make_glass():
    g2_1 = Glass(100, 10)
    print(g2_1.capacity_volume, g2_1.occupied_volume)
    
    g2_2 = Glass(100, 10)
    print(g2_2.capacity_volume, g2_2.occupied_volume)

    g2_1.occupied_volume = 20
    print(g2_1.occupied_volume, g2_2.occupied_volume)

    #g2_3 = Glass(-1, 0)
    #g2_4 = Glass(0, 1)
    #g2_5 = Glass()
    #g2_6 = Glass("sadahl", 0)

# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class GlassDefaultArg:

    def __init__(self, capacity_volume, occupied_volume=0):
        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume
            else:
                raise ValueError ("Must be (0, inf)")
        else:
            raise TypeError ("Must be integer or float")
  
        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0 and occupied_volume <= self.capacity_volume:
                self.occupied_volume = occupied_volume
            else:
                raise ValueError ("Must be [0, capacity_volume]")
        else:
            raise TypeError ("Must be integer or float")
            

def make_glass_default():
    g3_1 = GlassDefaultArg(200)
    print(g3_1.capacity_volume, g3_1.occupied_volume)
    
    g3_2 = GlassDefaultArg(200, 200)
    print(g3_2.capacity_volume, g3_2.occupied_volume)


# 4. Создайте класс GlassDefaultListArg (нужен только __init__) 
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?


class GlassDefaultListArg:

    def __init__ (self, capacity_volume, occupied_volume=[]):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        self.occupied_volume.append(2)

def make_glass_list():
    """
    Пояснение:
    occupied_volume существует для всех экземляров класса
    ссылка на пустой список создана по умолчанию является для всех экземпляров единой
    изменяемые типв это набор ссылок на объекты
    
    occupied_volume -> [2], [2, 2], [2, 2, 2] 
    """
    g4_1 = GlassDefaultListArg(200)
    print(g4_1.capacity_volume, g4_1.occupied_volume)

    g4_2 = GlassDefaultListArg(300)
    print(g4_2.capacity_volume, g4_2.occupied_volume)

    g4_3 = GlassDefaultListArg(400)
    print(g4_3.capacity_volume, g4_3.occupied_volume)



# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.

class GlassAddRemove:

    def __init__(self, capacity_volume, occupied_volume=0):
        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume
            else:
                raise ValueError ("Must be (0, inf)")
        else:
            raise TypeError ("Must be integer or float")

        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0 and occupied_volume <= self.capacity_volume:
                self.occupied_volume = occupied_volume
            else:
               raise ValueError ("Must be [0, capacity_volume]")
        else:
            raise TypeError ("Must be integer or float")

    def add_water(self, volume):
        """
        Example:
            Glass(100, 0)
            Glass.add_water(10)  # Glass(100, 10)
            GLass.add_water(100) # Glass(100, 100), return Остаток: 10
        """
        if isinstance(volume, (int, float)):
            if volume > 0:
                self.volume = volume
            else:
                raise ValueError ("Must be > 0")
        else:
            raise TypeError ("Must be integer of float")
        if self.volume > self.capacity_volume - self.occupied_volume:
            self.occupied_volume = self.capacity_volume
            return f"Остаток: {volume - (self.capacity_volume - self.occupied_volume)}"
        else:
            self.occupied_volume += volume

    def remove_water(self, volume):
        """
        Example:
            Glass(100, 50)
            Glass.remove_water(10)  # Glass(100, 40)
            Glass.remove_water(50)  # VallueError
        """
        if isinstance(volume, (int, float)):
            if volume >= 0:
                self.volume = volume
            else:
                raise ValueError ("Must be positive")
        else:
            raise TypeError ("Must be integer of float")
        if self.volume > self.occupied_volume:
            raise ValueError ("Value volume water > occupiefd volum")
        else:
            self.occupied_volume -= self.volume


def glass_method():
    g5_1 = GlassAddRemove(200, 100)
    print(g5_1.capacity_volume, g5_1.occupied_volume)

    g5_1.add_water(50)
    print(g5_1.capacity_volume, g5_1.occupied_volume)
    
    g5_1.remove_water(150)
    print(g5_1.capacity_volume, g5_1.occupied_volume)

    #g5_1.remove_water(50) # должно быть вызвано исключение
    

# 6. Создайте три объекта типа GlassAddRemove, 
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.


def print_dir(obj):
    print("="*20)
    print(type(obj))
    print("+"*20)
    print(dir(obj))

def glass_dir():

    g6_1 = GlassAddRemove(200, 100)
    g6_2 = GlassAddRemove(20, 10)
    g6_3 = GlassAddRemove(200, 1)

    print_dir(g6_1)
    print_dir(g6_2)
    print_dir(g6_3)
    print_dir(GlassAddRemove)


# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__, 
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.

class GlassDefaultList:

    def __init__ (self, capacity_volume=100, occupied_volume=5):
        print(self.__dir__)
        self.capacity_volume = capacity_volume
        print(self.__dir__)
        self.occupied_volume = occupied_volume
        print(self.__dir__)


def glass_attr():
    """
    Результат:
        сначала отображаются атрибуты встроенные (built-in)
        далее последовательно добавляются атрибуты пользовательские
    """
    g7_1 = GlassDefaultList()


# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.

def glass_id():
    g8_1 = Glass(200, 10)
    g8_2 = Glass(200, 100)
    g8_3 = Glass(200, 100)
    
    print(hex(id(g8_1)))
    print(hex(id(g8_2)))
    print(hex(id(g8_3)))

# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python - да, т.к. первый аргумент в функциях(методах) класса указывает на экземпляр
#     - соглашения о стиле кодирования - self
#    Запустите код.

class d:
    def __init__(f, a=2):
        f.a = a

    def print_me(p):
        print(p.a)

def func_d():
    """
    Первый аргумент в функциях (методах) класса указывает на экземпляр
    Для интерпретатора наименование первого аргумента не обязательно, по соглашению о стиле кодирования - self
    """
    d.print_me(d())


# 10. Исправьте
class A:
    def __init__(self, a):
        if 10 < a < 50:
            #return
            raise ValueError ("Value a must be (10, 50)")
        self.a = a

def func_a():
    """
    Объясните так реализовывать __init__ нельзя?
    __init__ должен быть реализован с использованием проверки данных,
    при неправильной инициализации необходимо вызвать исключение
    """
    a10_1 = A(20)
    a10_2 = A(0)
    
    print(a10_1.__dict__)
    print(a10_2.__dict__)

# Объясните так реализовывать __init__ нельзя?
		
        
        
        
# 11. Циклическая зависимость (стр. 39-44)
# 

class Node:
    def __init__(self, prev=None, next_=None):
        self.__prev = prev
        self.__next = next_
    def set_next(self, next_):
        self.__next = next_

    def set_prev(self, prev):
        self.__prev = prev
        
    def __str__(self):
        ...
        
    def __repr__(self):
        ...

class LinkedList:



    def insert(self, node, index=0):
        '''
        Insert Node to any place of LinkedList
        node - Node
        index - position of node
        '''
        ...
        
       
    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        ...

    def clear(self):
        '''
        Clear LinkedList
        '''
        ...

    def find(self, node):
        ...


    def remove(self, node):
        ...
        
    def delete(self, index):
        ...
























