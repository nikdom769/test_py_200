# Лабораторная работа № 1.2
# Слушатель (ФИО): Домичев Н.Н.

class Date:
class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # usual year
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))  # intercalary year

    def __init__(self, *args):
        """
        Example:
            d1 = Date(2010, 11, 15)  # 15.11.2010
        Exceptions:
            TypeError("Date  must be in the next format:2000, 2, 13 or '2000.2.13' and\
                    year, month, day - integer")
            ValueError("Wrong date")
        """
        self.__year, self.__month, self.__day = self.__is_valid_date(*args)

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    def __repr__(self):
        return f"Date({self.__year}, {self.__month}, {self.__day})"

    @staticmethod
    def is_leap_year(year):
        """
        Testing year for intercalary
        :param year: Format 2012, 1978
        :return: True - usual year, False - intercalary year
        Високосные года делятся нацело на 4.
        Однако из этого правила есть исключение: 
             столетия, которые не делятся нацело на 400, високосными не являются.
        """
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            return False
        else:
            return True

    @classmethod
    def get_max_day(cls, year, month):
        """
        Return max value day in month of year
        :param year: Format 2012, 1978
        :param month: Format 1, 2 ...
        :return: Max value day in month of year
        """
        new_year = 1 if cls.is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[new_year][month - 1]
    
    @classmethod
    def __is_valid_date(cls, *args):
        if len(args) < 3:
            raise ValueError("Wrong format date. Must be (2020, 12, 23)")
        for i in args:
            if not isinstance(i, int):
                raise TypeError("Value's year, month and day must be int")
        if not (0 < args[1] < 13 or 0 < args[2] < 32):
            raise ValueError("Wrong date: month must be 1 ... 12, day must be 1 ... 31")
        if args[2] > cls.get_max_day(args[0], args[1]):
            raise ValueError("Wrong date: value day > max value day in month")
        else:
            return args     

    @property
    def date(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    @date.setter
    def date(self, *value):
        self.__year, self.__month, self.__day = self.__is_valid_date(1*value)
        #self.__init__(*value)

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    def __max_day(self):
        """
        Пересчет даты, если при изменении года или месяца текущий день больше
        максимального дня нового месяца
        """
        new_day = self.__day - self.get_max_day(self.__year, self.__month)
        self.__year += 1 if self.__month + 1 > 12 else 0
        self.__month += 1
        self.__day = new_day
        
    @staticmethod
    # вычисление разности дат
    def __sub_date(date1, date2):
        """
        date1 > date2
        format date1 (date2): 2020, 3, 10
        """
        year = date1[0] - date2[0]
        if date1[1] - date2[1] < 0:
            month = 12 + (date1[1] - date2[1]) % 12
            year -= 1
        else:
            month = date1[1] - date2[1]
        if date1[2] - date2[2] < 0:
            day = (Date.get_max_day(date2[0], date2[1]) - date2[2]) + date1[2]
            if month - 1 < 0:
                year -= 1
                month = 11
            else:
                month -= 1
        else:
            day = date1[2] - date2[2]
        return f"{year} year, {month} month, {day} day"

    def add_day(self, day):
        """
        Example:
            d1 = Date(2020, 2, 15)  # 15.2.2020
            d1.add_day(14)          # 29.2.2020
            d1.add_day(35)          # 4.4.2020
        Exceptions:
            Value day must be positive or zero int
        """
        if not isinstance(day, int):
            raise TypeError('Day must be int')
        if day < 0:
            raise ValueError('Value day must be positive or 0')
        while day:
            if self.__day + day > self.get_max_day(self.__year, self.__month):
                day -= (self.get_max_day(self.__year, self.__month) - self.__day)
                self.__day = 0
                self.add_month(1)
            else:
                self.__day += day
                day = 0

    def add_month(self, month):
        """
        Example:
            d1 = Date(2020, 2, 15)  # 15.2.2020
            d1.add_month(5)         # 15.7.2020
            d1.add_month(13)        # 15.8.2021
        Exceptions:
            Value month must be positive or zero int
        """
        if not isinstance(month, int):
            raise TypeError("Value month must be int")
        if month < 0:
            raise ValueError('Value month  must be positive or 0')
        if month // 12:
            self.add_year(month // 12) #  если прибавляем более 12 месяцев
        if self.__month + month % 12 > 12:
        # проверка если после прибавления месяца переходим в новый год
            self.__month = (self.__month + month % 12) % 12
            self.__year += 1 # без проверки дня, т.к. проветка дня ниже 
        else:
            self.__month += month % 12
        if self.__day > self.get_max_day(self.__year, self.__month):
            self.__max_day() # изменение дня

    def add_year(self, year):
        """
        Example:
            d1 = Date(2020, 2, 29)  # 29.2.2020
            d1.add_year(1)          #  1.3.2021
            d1.add_year(2)          #  1.3.2023
        Exceptions:
            Value year must be positive or zero int
        """
        if not isinstance(year, int):
            raise TypeError("Value year must be int")
        if year < 0:
            raise ValueError('Value year must be positive or 0')
        self.__year += year
        if self.__day > self.get_max_day(self.__year, self.__month):
            self.__max_day() # изменение дня

    @staticmethod
    def date2_date1(date2, date1):
        """
        Example:
            a = (2020, 2, 2)
	    b = [2021, 3, 3]
            Date.date2_date1(a, b)         #  1 year, 1 month, 1 day
        Exceptions:
            Value year must be positive or zero int
        """

        if not isinstance(date2, (list, tuple)):
            raise TypeError("Date2 must be list or tuple")
        if not isinstance(date1, (list, tuple)):
            raise TypeError("Date1 must be list or tuple")
        if len(date2) != 3:
            raise ValueError("Date2 must be (2020, 2, 3)")
        if len(date1) != 3:
            raise ValueError("Date1 must be (2020, 2, 3)")
        
        if Date(date2[0], date2[1], date2[2]) == Date(date1[0], date1[1], date1[2]):
            return 0
        elif Date(date2[0], date2[1], date2[2]) > Date(date1[0], date1[1], date1[2]):
            return Date.__sub_date(date2, date1)
        else:
            return Date.__sub_date(date1, date2)


    def __eq__(self, other):
        """self == other"""
        return True if self.__day == other.__day\
                       and self.__month == other.__month\
                       and self.__year == other.__year else False
    
    def __gt__(self, other):
        """self > other"""
        if self.__year > other.__year:
            return True
        elif self.__year == other.__year\
              and self.__month > other.__month:
            return True
        elif self.__year == other.__year\
              and self.__month == other.__month\
              and self.__day > other.__day:
            return True
        else:
            return False

