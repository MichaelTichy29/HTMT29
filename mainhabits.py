# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 17:09:14 2023

@author: Michael
"""

import sqlite3
from habits import*
from Maketable import*
import questionary
import datetime
     


def perioddbtopython(perin):
    """ Transform the period form database structure the the structure of python
    
    perin: inputperiod (as integer, 0 = week)
    
    return: perout - period for the output (day, week or integer) 
    """
    if perin == 1:
        perout = "day"
    elif perin == 0:
        perout = "week"
    else:
        perout = perin    
    return perout
    
def periodpythontodb(perin):
    """ Transform the period form python structure the the structure of the database
    
    perin: inputperiod (day, week or integer) 
    
    return: perout - period for the output (as integer, 0 = week)
    """
    if perin == "day":
        perout = 1
    elif perin == "week":
        perout = 0    
    else:
        perout = perin    
    return perout

    
def checkperiod(period):
    """ Check if the given input is a valid value for a period. For a real input suggest an integer
    
    period: input period of the user (day, week or integer is valid) 
    
    return: perout - period for the output in python strukture
            res - weather the input is a valid period, we suggest a period or the input is sensless.
    """
    
    if (period == "day" or period == "week"):
        res = 1
        perout = period
    else:
        try:
            per_fl = float(period)
            
            if (int(per_fl) == per_fl and int(per_fl) > 0):
                res = 1
                perout = int(per_fl)
            elif per_fl > 0:
                res = 2
                perout = int(float(period))
            else:
                res = 0
                perout = period
        except ValueError:
            res = 0
            perout = period
 
    return [res, perout]
    
    
def printhabits(inhalt):
    # prints the habits of a list (an add the period)
    t = 0
    for x in inhalt:
        t = t+1
        per = perioddbtopython(x[1])
        print(t, ": ",  x[0], "(period = ", per, ")")
        
def printhabitslist(inhalt):
    # print the habits of a list (without the period)
    t = 0
    for x in inhalt:
        t = t+1
        print(t, ": ",  x[0],)


def allhabits(dbz):
    """ gives all habits of a database
    
    dbz: the used database connection
    
    return: Inhalt - list of the habits
    """
    point = dbz.db.cursor()
    point.execute("Select DISTINCT name, period FROM habits")
    inhalt = point.fetchall()
    #printhabits(inhalt)    
    return inhalt
      


def allhabitsper(dbz,per):
    """ gives all habits with a certain period of a database
    
    dbz: the used database connection
    per: period of intrest
    
    return: Inhalt - list of the habits with the period = per
    """
    perdb = periodpythontodb(per)
    point = dbz.db.cursor()
    point.execute("Select DISTINCT name, period FROM habits WHERE period=?", (perdb,))
    inhalt = point.fetchall()
    return(inhalt)
    

def printdata(inhalt):
    # print check out dates
    t = 0
    for x in inhalt:
        t = t+1
        print(t, ": ",  x[0], "(habit: ", x[1], ")")
        
        

def daten(dbz, habit):
    """ gives all ckeck out dates for a habit in a database 
    
    dbz: the used database connection
    habit: habit of intrest
    
    return: Inhalt - list of check out dates for the habit
    """
    point = dbz.db.cursor()
    point.execute("Select checkoff, name FROM dates WHERE name ='" + habit + "'")
    inhalt = point.fetchall()
    return inhalt
    




def checkouthabit(dbz, habit):
    """ check if the habit exists in the database and weather it isn't checkt out for today
    checkt out (wirte in database by add_data) if this is fullfilled
    
    dbz: the used database connection
    habit: habit of intrest
    
    return: testout - if the writing is successfull (0= not ex, 1 = success, 2 = already checked out)
    """

    test = allhabits(dbz)
    #condition if the habit exists
    test1 = 0
    for x in test:
        if x[0] == habit:
            pastdates = daten(dbz, habit)
            test1 = 1
            #condition if the habit is checked out today already
            test2 = 0
            for y in pastdates:
                dateobj = datetime.datetime.strptime(y[0], '%Y-%m-%d').date()
                today = datetime.date.today()
                if today == dateobj:
                    test2 = 1
                    testout = 2
                    print("Attention! You have already checked out the habit", habit, "for today")
            if test2 == 0:
                dbz.add_data(habit, datetime.date.today())
                print("Yes! Now you have checked out the habit", habit, "for today")
                testout = 1
    if test1 == 0: 
        print("Some user bug! The habit", habit, "doesn't exist")
        testout = 0
    return testout
        


def delcheckouthabit(dbz, habit):
    """ check if the habit exists in the database and is checked out for today
    if this is fullfilled remove this chekc out
    
    dbz: the used database connection
    habit: habit of intrest
    
    return: testout - if the removing is successfull (1 = success, 2 = not exist or not checked out)
    """

    test = allhabits(dbz)
    #condition if the habit exists
    test1 = 0
    for x in test:
        if x[0] == habit:
            pastdates = daten(dbz, habit)
            test1 = 1
            #condition if the habit is checked out today already
            test2 = 0
            for y in pastdates:
                dateobj = datetime.datetime.strptime(y[0], '%Y-%m-%d').date()
                today = datetime.date.today()
                if today == dateobj:
                    test2 = 1
                    # remove the check out
                    dbz.del_data(habit, y[0])
                    testout = 1
                    print("Now you have removed the checked out of the habit", habit, "for today")
            if test2 == 0:
                print("You havn't checkt out the habit", habit, "for today")
                testout = 2
    if test1 == 0: 
        print("The habit", habit, "doesn't exist")
        testout = 2
    return testout
   

def funccheckex(dbz, habit):
    """ check if the habit exists in the database. 
    
    dbz: the used database connection
    habit: suggested name of intrest
    
    return: exists (0 = not exists, 1 = exists)
    """
    test = allhabits(dbz)
    exists = 0
    for x in test:
        if x[0] == habit:
            exists = 1
    return exists    


     
def newhabit(dbz, habit, period):
    """ check if the habit exists in the database. if not then add this habit
    
    dbz: the used database connection
    habit: habit of intrest
    period: frequenz of the new habit (day, week or integer)
    
    return: ---
    """
    test1 = funccheckex(dbz, habit)
    """test = allhabits(dbz)
    test1 = 0
    for x in test:
        if x[0] == habit:
            test1 = 1
            """
    if test1 == 0:
        perout = periodpythontodb(period)
        dbz.new_habit(habit, perout)
        




def askforhabit(dbz, question):
    """Ask for the name of a habit, until the user enters a valid name
    dbz: the used database connection
    question: string of the question which is asked
    
    return: answer1 - name of the habit, if valid
    """

    res = 0
    test = allhabits(dbz)
    while res == 0:
        print("Your current habits are:")
        printdata(test)
        print(question)
        answer1 = questionary.text("Name of the habit").ask()
        res = funccheckex(dbz, answer1)
    return answer1

        
            
def funciniobjanddata(dbz, habit):
    """For the analyse of a habit get the data out of the database and cunstruct the class
    
    dbz: the used database connection
    habit: name of the habit ! must be valid. chek before
    
    return: chabit - the class of the habit to analyse
    """
    test = allhabits(dbz)
    for x in test:
       if x[0] == habit:
           pastdates = daten(dbz, habit)
           if x[1] == 1:
               periodout = "day"
           elif x[1] == 0:
               periodout = "week"
           else:
               periodout = x[1]        
           chabit = clhabit(periodout)
           #condition if the habit is checked out today already
           for y in pastdates:
               dateobj = datetime.datetime.strptime(y[0], '%Y-%m-%d').date()
               chabit.checkoff.append(dateobj)
    return chabit

def funcstruggleakt(dbz, habit):
    """Check if the habit exixts in the database.
    If this is fullfilled use struggleakt to check weather we struggle currently
    
    dbz: the used database connection
    habit: name of the habit ! must be valid. chek before
    
    return: strugglenow (yes or no)
    """
   
    exists = funccheckex(dbz, habit)
    if exists == 1:
        chabit = funciniobjanddata(dbz, habit)
        strugglenow = chabit.struggleakt()
    else:
        strugglenow = "not defined"
    return strugglenow




def funcstreakcurrent(dbz, habit):
    """Check if the habit exixts in the database.
    If this is fullfilled use streakcurrent to calculate the current streak
    
    dbz: the used database connection
    habit: name of the habit ! must be valid. chek before
    
    return: streaknow  length of the current streak (integer, 0 = struggle akt)
    """
    exists = funccheckex(dbz, habit)
    if exists == 1:
        chabit = funciniobjanddata(dbz, habit)
        streaknow = chabit.streakcurrent()
    else:
        streaknow = "not defined"
    return(streaknow)



def funcstreaklong(dbz, habit):
    """Check if the habit exixts in the database.
    If this is fullfilled use streaklong to search for the longest streak
    
    dbz: the used database connection
    habit: name of the habit ! must be valid. chek before
    
    return: streaklong length of the longest streak of a habit (integer)
    (it's not defined if there was no streak at any time')
    """
    exists = funccheckex(dbz, habit)
    if exists == 1:
        chabit = funciniobjanddata(dbz, habit)
        if len(chabit.checkoff) > 0:
            streaklong = chabit.streaklong()
        else:
            streaklong = 0
    else:
        streaklong = "not defined"
    return(streaklong)


def funcstreaklongall(dbz):
    """Runs the function funcstreaklong(dbz, habit) for all habits of the database.
    calculate the longest streak. 
    
    dbz: the used database connection
    
    return: maxstreak - length of the longest streak (as integer)
            streaklongnames - list the names of the habits with the longest streak 
    """
    
    allhab = allhabits(dbz)
    streaklonglist = []
    streaklongnames = []
    maxstreak = 0
    for x in allhab:
        chabit = funciniobjanddata(dbz, x[0])
        if len(chabit.checkoff) > 0:
            streaklong = chabit.streaklong()
        else:
            streaklong = 0
        streaklonglist.append(streaklong)
        #if the longest streak of the new habit is the longest over all, then set a new max and write the name in the list.
        # if the longest streak of the new habit as long as the current max add the name to the list of the max streaks
        if streaklong > maxstreak:
            streaklongnames.clear()
            maxstreak = streaklong
            streaklongnames.append(x[0])
        elif streaklong == maxstreak:
            streaklongnames.append(x[0])
    return [maxstreak, streaklongnames]
    

def funcstruggleaktall(dbz):
    """Runs the function funcstruggleakt for all habits of the database.
    list the names of the habits which struggle currently 
    
    dbz: the used database connection
    
    return: strugglelist (list of strings) 
    """
    allhab = allhabits(dbz)
    strugglelist = []
    for x in allhab:
        akt = funcstruggleakt(dbz, x[0])
        if akt == "yes":
            strugglelist.append(x[0])
    return strugglelist
