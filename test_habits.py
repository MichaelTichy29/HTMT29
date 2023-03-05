# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 22:28:31 2023

@author: Michael
"""

from habits import*
import unittest

class Testhabits(unittest.TestCase):
    def test_newhabit(self):
        
        #data for unit test
        sport = clhabit("day")   
        fruit = clhabit("week")
        cheese = clhabit(8)
        
        cheese.checkoff.append(datetime.date(2023,1,10))
        sport.checkoff.append(datetime.date(2023,1,10))
        fruit.checkoff.append(datetime.date(2023,1,10))
        cheese.checkoff.append(datetime.date(2023,1,11))
        sport.checkoff.append(datetime.date(2023,1,11))
        fruit.checkoff.append(datetime.date(2023,1,11))
        cheese.checkoff.append(datetime.date(2023,1,12))
        sport.checkoff.append(datetime.date(2023,1,12))
        fruit.checkoff.append(datetime.date(2023,1,12))
        cheese.checkoff.append(datetime.date(2023,1,13))
        sport.checkoff.append(datetime.date(2023,1,13))
        fruit.checkoff.append(datetime.date(2023,1,13))
        
        cheese.checkoff.append(datetime.date(2023,1,30))
        sport.checkoff.append(datetime.date(2023,1,30))
        fruit.checkoff.append(datetime.date(2023,1,30))
        cheese.checkoff.append(datetime.date(2023,1,31))
        sport.checkoff.append(datetime.date(2023,1,31))
        fruit.checkoff.append(datetime.date(2023,1,31))
        cheese.checkoff.append(datetime.date(2023,2,9))
        sport.checkoff.append(datetime.date(2023,2,9))
        fruit.checkoff.append(datetime.date(2023,2,9))
        cheese.checkoff.append(datetime.date(2023,2,10))
        sport.checkoff.append(datetime.date(2023,2,10))
        fruit.checkoff.append(datetime.date(2023,2,10))
        
        
        #test
        
        self.assertEqual(sport.struggleakt(),"yes")
        self.assertEqual(fruit.struggleakt(),"yes")
        self.assertEqual(cheese.struggleakt(),"yes")
        self.assertEqual(sport.streakcurrent(),0)
        self.assertEqual(fruit.streakcurrent(),0)
        self.assertEqual(cheese.streakcurrent(),0)
        
        
        cheese.checkoff.append(datetime.date.today())
        sport.checkoff.append(datetime.date.today())
        fruit.checkoff.append(datetime.date.today())
        
        self.assertEqual(sport.struggleakt(),"no")
        self.assertEqual(cheese.struggleakt(),"no")
        self.assertEqual(fruit.struggleakt(),"no")
        self.assertEqual(sport.streakcurrent(),1)
        self.assertEqual(fruit.streakcurrent(),1)
        self.assertEqual(cheese.streakcurrent(),1)
        
        #"""
        #test struggle
        #print(sport.checkoff(6))
        self.assertEqual(sport.struggle(datetime.date(2023,1,31),6),"no")
        self.assertEqual(cheese.struggle(datetime.date(2023,1,31),6),"no")
        self.assertEqual(fruit.struggle(datetime.date(2023,1,31),6),"no")
    
        self.assertEqual(sport.struggle(datetime.date(2023,1,29),4),"yes")
        self.assertEqual(cheese.struggle(datetime.date(2023,1,29),4),"yes")
        self.assertEqual(fruit.struggle(datetime.date(2023,1,29),4),"yes")
        #"""
        
        #test streaksingle
        self.assertEqual(sport.streaksingle(datetime.date(2023,1,13),4),[4,-1])
        self.assertEqual(cheese.streaksingle(datetime.date(2023,2,10),8),[2,5])
        self.assertEqual(fruit.streaksingle(datetime.date(2023,2,11),8),[2,3])
    
        self.assertEqual(sport.streaksingle(datetime.date(2023,1,25),4),[0,3])
        self.assertEqual(cheese.streaksingle(datetime.date(2023,1,13),4),[4,-1])
        self.assertEqual(fruit.streaksingle(datetime.date(2023,2,10),8),[2,3])
        
        
        
        #test streaklong
        self.assertEqual(sport.streaklong(),4)
        self.assertEqual(cheese.streaklong(),4)
        self.assertEqual(fruit.streaklong(),2)
               
        
        
     
if __name__ == '__main__':
    unittest.main()