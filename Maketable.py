# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 21:01:38 2023

@author: Michael
"""

import sqlite3

class DatabaseConnection:
    """ construkt the database connection as a class. (Ok, I got this as a hint to disconnet an remove this more easily)
    """
    def __init__(self, name = "habitdaten.sqlite"):
        self.db = sqlite3.connect(name)
    
    def __delete__(self):
        self.db.close()
    
    
    def maketable(self):
        """ create the database, if it does not exist.
        
        habits: name of the habit (PRIMARY KEY)
                period the habit shoul be done
        dates: name (FOREIGN KEY)
               checkofflen as list of checkoffs
               condition relikt of an old idea - removable
        
        """
        point = self.db.cursor()
    
        point.execute("CREATE TABLE IF NOT EXISTS habits(name VARCHAR(20), period INTEGER)")
        point.execute("CREATE TABLE IF NOT EXISTS dates(name VARCHAR(20), checkoff DATE, condition INTEGER)")
        self.db.commit()
        
        
    def new_habit(self, name, period):
        """
        insert a new habit in the table habit
        """
        point = self.db.cursor()
        point.execute("INSERT INTO habits VALUES (?,?)", (name, period))
        self.db.commit()
    
    def add_data(self, name, date):
        """
        insert a new date in the table dates
        """
        point = self.db.cursor()
        point.execute("INSERT INTO dates VALUES (?,?,?)", (name, date, 2))
        self.db.commit()
        
        
    def del_data(self, name, date):
        """
        removes a date in the table dates
        !!! in the code only allowed for the current date.
        """
        point = self.db.cursor()
        point.execute("DELETE FROM dates WHERE name ='" + name + "' and checkoff ='" + date + "'") 
        self.db.commit()