#!/usr/bin/env python
# coding: utf-8



from datetime import datetime

class Time:
    
    def __init__(self, *args):
        '''Examples:
               Format: 24 h only
               t1 = Time(21, 15)  # 21:15
               t2 = Time('21:15') # 21:15
               t_now = Time()     # Current OS time
           Exceptions:
                TypeError('Arguments must be in the next format:\
                             hour - int and minute - int or "HH:MM"'
        '''
        self.h, self.m = self.__validate_time(*args)
        
    def add_hour(self, hour):
        '''Examples:
               t = Time(21, 15)  # 21:15
               t.add_hour(2)     # 23:15
               t.add_hour(1)     # 00:15
               t.add_hour(12)    # 12:15
               t.add_hour(24)    # 12:15
               t.add_hour(49)    # 13:15
           Exceptions:
                hour must be positive or zero int
        '''
        if not isinstance(hour, int):
            raise TypeError('Argument hour must be int')
        if hour < 0:
            raise ValueError('Argument hour must be positive or zero')
        self.h = (self.h + hour) % 24
    
    def add_minute(self, minute):        
        '''Examples:
               t = Time(21, 15)  # 21:15
               t.add_minute(2)   # 21:17
               t.add_minute(60)  # 22:17
               t.add_hour(120)   # 00:17
               t.add_hour(65)    # 01:22
           Exceptions:
                minute must be positive or zero int
        '''
        if not isinstance(minute, int):
            raise TypeError('Argument minute must be int')
        if minute < 0:
            raise ValueError('Argument minute must be positive or zero')
        self.add_hour(minute//60)
        minute = minute % 60
        if self.m + minute > 59:
            self.add_hour(1)
            minute -= 60
        self.m += minute      
    
    
    def delta_time(self, *args, new_day=True):
        """
        Calculate delta time
        param: new_day - True - new_day, False - day now
        Examples:
            Format: 24 h only: (21, 15) or ('21:15')
            t = Time('21:15')
            t.delta_time(21, 15)                 # d:1, h:0, m:0
            t.delta_time(11, 45, new_day=False)  # h:9, m:30
            t.delta_time(11, 45)                 # d:0, h:14, m:30
            t.delta_time(21, 15, new_day=False)  # h:0, m:0
            
        Exceptions:
            TypeError('Arguments must be in the next format:\
                         hour - int and minute - int or "HH:MM"'
        """
        self.h_new, self.m_new = self.__validate_time(*args)
        self.t_in_m_new = self.h_new * 60 + self.m_new
        if new_day:
            self.delta_old_day = 1440 - (self.h * 60 + self.m)
            self.delta = self.delta_old_day + self.t_in_m_new
            self.day = self.delta % (24 * 60)
            return f"d:{self.delta//(24*60)}, h:{self.day//60}, m:{self.day%60}"   
        else:
            self.t_in_m_old = self.h * 60 + self.m
            self.delta = abs(self.t_in_m_new - self.t_in_m_old)
            return f"h:{self.delta//60}, m:{self.delta%60}"

    
    @property
    def time(self):
        return self.__str__()

    @time.setter
    def time(self, value):
        self.__init__(value)
        
    def __str__(self):
        h = str(self.h) if self.h > 9 else f'0{self.h}'
        m = str(self.m) if self.m > 9 else f'0{self.m}'
        return f'{h!s}:{m!s}'
    
    def __repr__(self):
        return f"Time('{self.__str__()}')"
    
    @staticmethod
    def __validate_time(*args):
        
        if len(args) == 0:
            t = datetime.now()
            return t.hour, t.minute
        try:
            if len(args) == 1 and isinstance(args[0], str):
                s = args[0].split(':')
                if len(s) != 2:
                    raise Exception()
                h = int(s[0])
                m = int(s[1])
                if not 0 <= h <= 23:
                    raise Exception()
                if not 0 <= m <= 59:
                    raise Exception()
                return h, m
            if len(args) == 2:
                h = args[0]
                m = args[1]
                if not isinstance(h, int):
                    raise Exception()
                if not isinstance(m, int):
                    raise Exception()
                    
                if not 0 <= h <= 23:
                    raise Exception()
                if not 0 <= m <= 59:
                    raise Exception()
                    
                return args[0], args[1]
        except:
            raise TypeError('Arguments must be in the next format:                             hour - int and minute - int or "HH:MM"')
            
        

