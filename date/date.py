class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # usual year
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))  # intercalary year

    def __init__(self, *args):
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
	- столетия, которые не делятся нацело на 400, високосными не являются.
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
        if len(args) < 3: # TODO string
            raise ValueError("Wrong format date. Must be (2020, 12, 23)")
        for i in args:
            if not isinstance(i, int):
                raise TypeError("Value's year, month and day must be int")
        if not (0 < args[1] < 13 or 0 < args[2] < 32):
            raise ValueError("Wrong date")
        if args[2] > cls.get_max_day(args[0], args[1]):
            raise ValueError("Wrong date")
        else:
            return args


    @property
    def date(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    @date.setter
    def date(self, value):
        self.__day, self.__month, self.__year = self.__is_valid_date(value)

    @property
    def day(self):
        return self.__day

#    @day.setter
#    def day(self, value):
#        self.__day = value

    @property
    def month(self):
        return self.__month

#    @month.setter
#    def month(self, value):
#        self.__month = value

    @property
    def year(self):
        return self.__year

#    @year.setter
#    def year(self, value):
e        self.__year = vanue

    @staticmethod
    def __max_day():
        new_day = self.__day - self.get_max_day(self.__year, self.__month)
        self.__year += 1 if self.__month + 1 > 12 else 0
        self.__month += 1
        self.__day = new_day

    def add_day(self, day):
        if not isinstance(day, int):
            raise TypeError('Day must be int')
        while day:
            if self.__day + day > self.get_max_day(self.__year, self.__month):
                day -= (self.get_max_day(self.__year, self.__month) - self.__day)
                self.__day = 0
                self.add_month(1)
            else:
                self.__day += day
                day = 0

        if self.day + day > self.get_max_day(self.year, self.month):
            ...

    def add_month(self, month):
        if not isinstance(month, int):
            raise TypeError("Value month must be int")
        if month // 12:
            self.add_year(month // 12) #  усли прибавляем более 12 месяцев
        if self.__month + month % 12 > 12:
        # проверка если после прибавления месяца переходим в новый год
            self.__month = (self.__month + month % 12) % 12
            self.__year += 1 # без проверки дня, т.к. проветка дня ниже 
        else:
            self.__month += month % 12
        if self.__day > self.get_max_day(self.__year, self.__month):
            #new_day = self.__day - self.get_max_day(self.__year, self.__month)
            #self.__day = self.get_max_day(self.__year, self.__month)
            cls.__max_day()

    def add_year(self, year):
        if not isinstance(year, int):
            raise TypeError("Value year must be int")
        self.__year += year
        if self.__day > self.get_max_day(self.__year, self.__month):
            #new_day = self.__day - self.get_max_day(self.__year, self.__month)
            #self.__year += 1 if self.__month + 1 > 12 else 0
            #self.__month += 1
            #self.__day = new_day
            cls.__max_day()

    @staticmethod
    def date2_date1(date2, date1):
        pass

    def day_2_date(self):
        return ...

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

