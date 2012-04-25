#-------------------------------------------------------------------------------
# Created on 14.12.2011
# 
# @author: Van Der Korn
# @file: filelogger.py
#-------------------------------------------------------------------------------
# -*- coding=utf-8 -*-

from  logger import Logger

class FileLogger(Logger):
    '''Журналирование'''
    
    def __init__(self,filename):
        '''Инициализация журнала'''
        self.filename=filename
        FileLogger.open(self)
          
    def open(self):
        '''Открыть журнал'''
        self.f_log = open(self.filename,'w+')

    def close(self):
        '''Закрыть журнал'''
        self.f_log.close()

    def writelog(self, text):
        '''Записать в журнал'''
        self.f_log.write("%s\n" % text)
        self.f_log.flush()

    def __del__(self):
        '''Уничтожить журнал'''
        FileLogger.close(self)

