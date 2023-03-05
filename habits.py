# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 06:00:59 2023

@author: Michael
"""

import datetime

class clhabit:
        
    def __init__(self,period):
        """ Constuction of the class which is used-
        
        period: frequenz in which the habit should be done (day, week, integer: week means one time in a calendary week, interger means the time between two events)
        checkoff: list of dates at which the habit is checked out
        """
        self.period = period
        self.checkoff = []

        
    """----------------------------------------------------------------------"""
    def struggle(self, dateakt, beginakt):
        """ Calculate if we struggel or not.
        differ between the period day, week and integer (in particular 7 != week)
    
        dateakt: Beginndate at which we should look back one period and decide
        beginakt: Index of the checkoff list at which we beginn to look back
        
        return: yes or no
        """
        checkofflen = beginakt
        if checkofflen == 0:
            struggle_current = "yes"
        else:
            """ calculation for the period dayly"""
            if self.period == "day":
                if dateakt == self.checkoff[checkofflen-1]:
                    struggle_current = "no"
                else:
                    struggle_current = "yes"
                        
            elif self.period == "week":
                """calculation for the period week, means each calendary week"""
                day_nr = dateakt.weekday()
                """Gives the number of the day mon = 0, tue = 1, ..."""
                if  dateakt - datetime.timedelta(days = day_nr+1) >= self.checkoff[beginakt-1]:
                    """check if the habbit was done in the current week"""
                    struggle_current = "yes"
                else: 
                    struggle_current = "no"
            
            else:
                """ calculation for an arbitrary period - given by a number of days"""
                if datetime.timedelta(days = self.period) >= dateakt - self.checkoff[beginakt-1]:
                    struggle_current = "no"
                else:
                    struggle_current = "yes"
        return struggle_current
        
    """----------------------------------------------------------------------"""


    def struggleakt(self):
        """ use method self.struggel with the current date
        
            return: yes or no
        """
        dateakt = datetime.date.today()
        beginakt = len(self.checkoff)
        struggleakt = self.struggle(dateakt, beginakt)
        return struggleakt
        """ ------------------------------------------------------------------------"""
        
    def streaksingle(self, begindate, beginindex):
        """ use self.struggel to calculate the streak which begins at a certain time and point in the list of checkoffs
            differ between the period day, week and integer (in particular 7 != week)
        
        dateakt: Beginndate at which we should look back one period and decide
        beginakt: Index of the checkoff list at which we beginn to look back
        
        return:  the lenght (in periods) of a single streak. (as integer)
        """
        checkofflen = beginindex
        count = 0        
        if self.period == "day":
            """calculation for period = day: count up as long as the dayly dates are in the checkoff array"""
            current = "no"
            while (current == "no" and count < checkofflen):
                if begindate - datetime.timedelta(days = count) == self.checkoff[checkofflen-1-count]:
                    current = "no"
                    count = count+1
                else:
                    current = "yes"
            newindex = beginindex - count-1
  
                                  
        elif self.period == "week":
            """calculation for period = week: check for the current week. If the habbit is found check from sun to sun if the 
            habbit is found at least once"""
            """Current week as initial:"""
            current = self.struggle(begindate, beginindex)
            if current == "yes":
                """streak does not exist has time 0- this case should not exist."""
                count = 0
                newindex = beginindex-1
            else:
                count = 1
                day_nr = begindate.weekday()+1
                sun2 = begindate - datetime.timedelta(days = day_nr)
                sun1 = sun2 - datetime.timedelta(days = 7)
                index = checkofflen-1
                indexcount = 0
                """ Count up for each week the habbit is found"""
                while (current == "no" and sun2 > self.checkoff[0]):
                    """indexcount searchs in the array of checkoffs"""
                    indexcount = 0
                    findhabbit = 0
                    """condition if the index of checkoff exists (>=0)"""
                    if index-1 >=  0:
                        exit = 0
                    else:
                        exit = 1
                    
                        
                    while (findhabbit == 0 and exit == 0 and sun1 < self.checkoff[index - indexcount-1]):
                        """check if we find the habbit in the given week"""
                        if sun2 >= self.checkoff[index-indexcount-1]:
                            findhabbit = 1
                            index = index - indexcount-1
                        else:
                            indexcount = indexcount +1
                            if index - indexcount == 0:
                                exit = 0
                                
                    """ count up or leave"""           
                    if findhabbit == 1:
                        current = "no"
                        count = count +1
                        sun2 = sun1
                        sun1 = sun2 - datetime.timedelta(days = 7)
                    else: 
                        current = "yes"
                if index == indexcount:
                    newindex = -1
                else:
                    newindex = index - indexcount -1
                    while (sun1 < self.checkoff[newindex] and newindex >= 0):
                        newindex = newindex -1
                                                   
        else:
            """check for an arbirary period"""
            current = self.struggle(begindate, beginindex)
            if current == "yes":
                """streak does not exist has time 0"""
                count = 0
            else:
                count = 1
                while (current == "no" and count < beginindex):
                    if datetime.timedelta(days = self.period) >= self.checkoff[checkofflen-count] - self.checkoff[checkofflen-count-1]:
                        current = "no"
                        count = count+1
                    else:
                        current = "yes"
            newindex = beginindex - count -1
            
        return [count, newindex]             
    
    """----------------------------------------------------------------------"""
        
    def streakcurrent(self):
        """ use method self.streaksingle with the current date
        
            return: lenght of the current streak (as integer)
        """
        
        begindate = datetime.date.today()
        beginindex = len(self.checkoff)
        [aktcount, aktindex] = self.streaksingle(begindate, beginindex)
        currentlen = aktcount
        return currentlen

    
    """----------------------------------------------------------------------"""
    
    def streaklong(self):
        """ use method self.streaksingle backwards in the list of checkoffs to calculate for one habit the longest streak.
        
           in the list streak we have lenght of the streaks. But we do not see if the habit is broken for one period or one year 
           so we do not list a number of zeros.
           
            return: streak -  lenght of the longest streak (as integer)
        """
        streak = []
        beginindex = len(self.checkoff)-1
        begindate = self.checkoff[beginindex]
        while (beginindex >=0):
             [count, newindex] = self.streaksingle(begindate, beginindex+1)
             streak.append(count)
             beginindex = newindex
             if newindex >= 0:
                 begindate = self.checkoff[newindex]
                                      
        """ the return ist the maximum of the different streaks"""
        #return streak
        return max(streak)
           
"""----------------------------------------------------------------------"""
"""----------------------------------------------------------------------"""

""" some simple test during the ddevelopment. sure I could remove them. 
But I decided another way"""

  
if __name__ == "__main__":     
    
    
   
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
 
    fruit.checkoff.append(datetime.date(2023,2,20))
    fruit.checkoff.append(datetime.date(2023,2,21))
    
    print(fruit.streaklong())

    
    