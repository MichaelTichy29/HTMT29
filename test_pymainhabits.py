# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 21:03:19 2023

@author: Michael
"""

from Maketable import*
from mainhabits import*
from datetime import date

class Testpymainhabits:
    
    
    def setup_method(self):
        self.dbztest = DatabaseConnection("test.sqlite")

        #self.db = get_db("test.sqlite")
        
        self.dbztest.maketable()
        
        self.dbztest.new_habit("Tennis", 0)
        newhabit(self.dbztest, "Hockey", 10)
        newhabit(self.dbztest, "Badminton", "week")
        newhabit(self.dbztest, "Push up", "day")
        self.dbztest.new_habit("Fruit", 1)
        
        # Tennis - week
        self.dbztest.add_data("Tennis", "2022-12-01")
        self.dbztest.add_data("Tennis", "2022-12-08")
        self.dbztest.add_data("Tennis", "2022-12-14")
        self.dbztest.add_data("Tennis", "2022-12-15")
        self.dbztest.add_data("Tennis", "2022-12-29")
        self.dbztest.add_data("Tennis", "2023-01-06")
        self.dbztest.add_data("Tennis", "2023-01-08")
        self.dbztest.add_data("Tennis", "2023-01-17")
        self.dbztest.add_data("Tennis", "2023-01-30")
        self.dbztest.add_data("Tennis", "2023-01-31")
        
                
        # Badminton - week
        self.dbztest.add_data("Badminton", "2022-12-01")
        self.dbztest.add_data("Badminton", "2022-12-13")
        self.dbztest.add_data("Badminton", "2022-12-27")
        self.dbztest.add_data("Badminton", "2022-12-28")
        self.dbztest.add_data("Badminton", "2023-01-04")
        self.dbztest.add_data("Badminton", "2023-01-05")
        self.dbztest.add_data("Badminton", "2023-01-06")
        self.dbztest.add_data("Badminton", "2023-01-18")
        self.dbztest.add_data("Badminton", "2023-01-27")
        self.dbztest.add_data("Badminton", "2023-02-01")
        self.dbztest.add_data("Badminton", "2023-02-04")
        
        
        # Hockey - 10
        self.dbztest.add_data("Hockey", "2022-11-30")
        self.dbztest.add_data("Hockey", "2022-12-01")
        self.dbztest.add_data("Hockey", "2022-12-04")
        self.dbztest.add_data("Hockey", "2022-12-18")
        self.dbztest.add_data("Hockey", "2023-01-03")
        self.dbztest.add_data("Hockey", "2023-01-04")
        self.dbztest.add_data("Hockey", "2023-01-18")
        self.dbztest.add_data("Hockey", "2023-01-20")
        self.dbztest.add_data("Hockey", "2023-01-25")
        self.dbztest.add_data("Hockey", "2023-01-30")
        self.dbztest.add_data("Hockey", "2023-02-04")
        
        
        # Push up - day
        self.dbztest.add_data("Push up", "2023-01-3")
        self.dbztest.add_data("Push up", "2023-01-06")
        self.dbztest.add_data("Push up", "2023-01-08")
        self.dbztest.add_data("Push up", "2023-01-09")
        self.dbztest.add_data("Push up", "2023-01-10")
        self.dbztest.add_data("Push up", "2023-01-11")
        self.dbztest.add_data("Push up", "2023-01-13")
        self.dbztest.add_data("Push up", "2023-01-14")
        self.dbztest.add_data("Push up", "2023-01-15")
        self.dbztest.add_data("Push up", "2023-01-16")
        self.dbztest.add_data("Push up", "2023-01-20")
        self.dbztest.add_data("Push up", "2023-01-21")
        self.dbztest.add_data("Push up", "2023-01-22")
        self.dbztest.add_data("Push up", "2023-01-23")
        self.dbztest.add_data("Push up", "2023-01-24")
        self.dbztest.add_data("Push up", "2023-01-25")
        self.dbztest.add_data("Push up", "2023-01-26")
        self.dbztest.add_data("Push up", "2023-01-27")
        self.dbztest.add_data("Push up", "2023-01-29")
        self.dbztest.add_data("Push up", "2023-01-30")
        self.dbztest.add_data("Push up", "2023-02-04")
        
        # fruit - day
        self.dbztest.add_data("Fruit", "2022-01-04")
        self.dbztest.add_data("Fruit", "2022-01-05")
        self.dbztest.add_data("Fruit", "2022-01-10")
        self.dbztest.add_data("Fruit", "2022-01-11")
        self.dbztest.add_data("Fruit", "2022-01-12")
        self.dbztest.add_data("Fruit", "2022-01-14")
        self.dbztest.add_data("Fruit", "2022-01-15")
        self.dbztest.add_data("Fruit", "2022-01-20")
        self.dbztest.add_data("Fruit", "2022-01-21")
        self.dbztest.add_data("Fruit", "2022-01-23")
        self.dbztest.add_data("Fruit", "2022-01-24")
        self.dbztest.add_data("Fruit", "2022-01-25")
        self.dbztest.add_data("Fruit", "2023-01-28")
        self.dbztest.add_data("Fruit", "2023-01-29")
        self.dbztest.add_data("Fruit", "2023-01-30")
        self.dbztest.add_data("Fruit", "2023-01-31")
        self.dbztest.add_data("Fruit", "2023-02-01")
        self.dbztest.add_data("Fruit", "2023-02-02")
        self.dbztest.add_data("Fruit", "2023-02-04")

         
        
        
        
    def test_period(self):
        
        #Transformation of period
        assert perioddbtopython(2) == 2
        assert perioddbtopython(0) == "week"
        assert perioddbtopython(1) == "day"
        
        assert periodpythontodb("day") == 1
        assert periodpythontodb("week") == 0
        assert periodpythontodb(9) == 9
        
        assert checkperiod("day") == [1, "day"]
        assert checkperiod("week") == [1, "week"]
        assert checkperiod("5") == [1, 5]
        assert checkperiod("2.3") == [2, 2]
        assert checkperiod("-1") == [0,"-1"]
        assert checkperiod("0") == [0,"0"]
        assert checkperiod("bla") == [0, "bla"]
        
        
        
        
        
        
        # list of habits
        assert allhabits(self.dbztest) == [("Tennis",0), ("Hockey",10), ("Badminton", 0), ("Push up", 1), ("Fruit", 1)]
        assert allhabitsper(self.dbztest, 10) == [("Hockey",10)]
        assert allhabitsper(self.dbztest, "week") == [("Tennis",0),("Badminton", 0)]
        assert allhabitsper(self.dbztest, "day") == [("Push up", 1), ("Fruit", 1)]
        assert daten(self.dbztest, "Tennis") == [("2022-12-01", "Tennis"), ("2022-12-08", "Tennis"), ("2022-12-14", "Tennis"),("2022-12-15", "Tennis"),("2022-12-29", "Tennis"),("2023-01-06", "Tennis"),("2023-01-08", "Tennis"),("2023-01-17", "Tennis"), ("2023-01-30", "Tennis"), ("2023-01-31", "Tennis")]
      
        
        #  check ex
        assert funccheckex(self.dbztest, "Tennis") == 1
        assert funccheckex(self.dbztest, "Push up") == 1
        assert funccheckex(self.dbztest, "bla") == 0
        assert funccheckex(self.dbztest, "Nein") == 0
                           
        
        
        #funcstruggleakt, checkouthabit and delcheckouthabit
        assert funcstruggleakt(self.dbztest, "Tennis") == "yes"
        checkouthabit(self.dbztest, "Tennis")
        assert funcstruggleakt(self.dbztest, "Tennis") == "no"
        delcheckouthabit(self.dbztest, "Tennis")
        assert funcstruggleakt(self.dbztest, "Tennis") == "yes"
        
        assert funcstruggleakt(self.dbztest, "Hockey") == "yes"
        checkouthabit(self.dbztest, "Hockey")
        assert funcstruggleakt(self.dbztest, "Hockey") == "no"
        delcheckouthabit(self.dbztest, "Hockey")
        assert funcstruggleakt(self.dbztest, "Hockey") == "yes"
        
        assert funcstruggleakt(self.dbztest, "Push up") == "yes"
        checkouthabit(self.dbztest, "Push up")
        assert funcstruggleakt(self.dbztest, "Push up") == "no"
        delcheckouthabit(self.dbztest, "Push up")
        assert funcstruggleakt(self.dbztest, "Push up") == "yes"
        
        
        #funcstreaklong
        assert funcstreaklong(self.dbztest, "Tennis") == 3
        assert funcstreaklong(self.dbztest, "Hockey") == 5
        assert funcstreaklong(self.dbztest, "Badminton") == 3
        assert funcstreaklong(self.dbztest, "Push up") == 8
        assert funcstreaklong(self.dbztest, "Fruit") == 6
        
        
        #funcstreaklongall
        assert funcstreaklongall(self.dbztest) == [8, ["Push up"]]
        self.dbztest.add_data("Hockey", "2023-02-05")
        self.dbztest.add_data("Hockey", "2023-02-06")
        self.dbztest.add_data("Hockey", "2023-02-07")
        assert funcstreaklong(self.dbztest, "Hockey") == 8
        assert funcstreaklongall(self.dbztest) == [8, ["Hockey", "Push up"]]
        
        
        # functstruggelall- list of habits that struggel currently
        assert funcstruggleaktall(self.dbztest) == ["Tennis", "Hockey", "Badminton", "Push up", "Fruit"]
        checkouthabit(self.dbztest, "Fruit")
        checkouthabit(self.dbztest, "Badminton")
        assert funcstruggleaktall(self.dbztest) == ["Tennis", "Hockey", "Push up"]
        delcheckouthabit(self.dbztest, "Fruit")
        assert funcstruggleaktall(self.dbztest) == ["Tennis", "Hockey", "Push up", "Fruit"]
        
        
        
        
        
    def teardown_method(self):
        self.dbztest.db.close()
        import os
        os.remove("test.sqlite")
        pass
    
    

    