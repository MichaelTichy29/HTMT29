# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 23:32:48 2023

@author: Michael
"""

import questionary
from mainhabits import*
from Maketable import*


def mainmenue():
   stop = False
   
   while not stop:
        print("\n")    
        choice = questionary.select("What do you want to do?", 
                                    choices=["Check out", "Delete a check out", "Analyse a habit", "Add a habit", "Exit"]).ask()
        if choice == "Check out":
            test = allhabits(dbz)
            if len(test) == 0:
                print("Currently you haven't defined any habit.")
            else: # There is a defined habit, to check out
                res = 0
                while res == 0:
                    print("\n")
                    print("Your current habits are:")
                    printhabits(test)
                    print("Which do you want to check out? Write the name.")
                    print("\n")
                    answer1 = questionary.text("Name of the habit").ask()
                    res = checkouthabit(dbz, answer1)
                    
        elif choice == "Delete a check out":
            test = allhabits(dbz)
            if len(test) == 0:
                print("Currently you haven't defined any habit.")
            else: # There is a habit to delte the check out
                res = 0
                while res == 0:
                    print("\n")
                    print("Your current habits are:")
                    printhabits(test)
                    print("For which one do you want to delete the check out for today? Write the name.")
                    print("\n")
                    answer1 = questionary.text("Name of the habit").ask()
                    res = delcheckouthabit(dbz, answer1)
                
        elif choice == "Analyse a habit":
            test = allhabits(dbz)
            if len(test) == 0:
                print("Sorry, there is currently no habit defined. You can't analyse something")
            else: 
                print("\n")
                choice = questionary.select("What do you want to analyse?", 
                                            choices=["Show a list of habits?", "Analyse which habits currently struggle?", "Analyse the streaks"]).ask()
                if choice == "Show a list of habits?":
                    print("\n")
                    choice1 = questionary.select("What do you want to see", 
                                                choices=["A list of all habits?", "A list of all habits for a certain period"]).ask()
                    
                    if choice1 =="A list of all habits?":
                        print("Your current habits are:")
                        test = allhabits(dbz)
                        printhabits(test)
                    else: # all habits of a given period
                        res = 0 
                        while res == 0:
                            print("\n")
                            answer2 = questionary.text("For which period do you want to have the habits?").ask()
                            [res, per] = checkperiod(answer2)
                            if res == 1:
                                print("Ok, the habits of the period", per, "are:")
                                habitsper = allhabitsper(dbz, per)
                                printhabits(habitsper)
                            elif res == 2:
                                print("Do you mean period = ", per, "?")
                                answer3 = questionary.select("Please confirm", choices=["yes", "no"]).ask()
                                if answer3 == "yes":
                                    print("Ok, the habits of the period", per, "are:")
                                    habitsper = allhabitsper(dbz, per)
                                    printhabits(habitsper)
                                else:
                                    res = 0
                                    print("Try it again. The frequenz must be day, week or an integer.")
                            else:
                                print("No the frequenz must be day, week or an integer")    
                
                elif choice == "Analyse which habits currently struggle?":
                    print("\n")
                    choice1 = questionary.select("What do you want to see", 
                                                choices=["A list of all habits currently struggle?", "For a certain habit whether you struggle aktual?"]).ask()
                    print("\n")
                    if choice1 == "A list of all habits currently struggle?":
                        strugglelist = funcstruggleaktall(dbz)
                        if len(strugglelist)  == 0:
                            print("Yes! You currently do not struggle with any habit!")
                        else:
                            print("Oh No!. You struggle currently with the following habits!")
                            printhabitslist(strugglelist)
                    else: 
                        answer1 = askforhabit(dbz, "For which habit do you want to know, weather you struggle currently?Write the name.")
                        strugglecur = funcstruggleakt(dbz, answer1)
                        if strugglecur == "yes":
                            print("Oh No!. You struggle currently with the habit", answer1)
                        elif strugglecur == "no":
                            print("It's fine! You have done the habit", answer1, "for the moment.")
                        else:
                            print("Something went wrong. This path is not allowed!")
                                
                            
                else: # choice =="Analyse the streaks"
                    print("\n")    
                    [maxstreak, streaklongnames] = funcstreaklongall(dbz)
                    print("The longest streak over all habits is", maxstreak)
                    print("This is for the habits:")
                    printhabitslist(streaklongnames)
                    print("\n")
                    
                    answer = questionary.select("What do you additional want to know?", choices=["Longest streak of a habit?", "Current streak length of a habit?", "Nothing?"]).ask()
                    if answer == "Longest streak of a habit?":
                        answer1 = askforhabit(dbz, "For which one do you want to know the longest streak? Write the name.")
                        streaklen = funcstreaklong(dbz, answer1)
                        if streaklen == 0:
                            print("Oh, you haven't done the habit", answer1, "at any time. The longest streak is", streaklen)
                        else:
                            print("The longest streak for", answer1, "was", streaklen)
                        
                    elif answer == "Current streak length of a habit?":
                        answer1 = askforhabit(dbz, "For which one do you want to know the current streak? Write the name.")
                        streaklen = funcstreakcurrent(dbz, answer1)
                        if streaklen == 0:
                            print("Oh, you haven't done the habit", answer1, "in this period. The current length is", streaklen)
                        else:
                            print("The current streak for", answer1, "is", streaklen)
                    else: 
                        print("Ok. Bye")                    
                
        
        elif choice == "Add a habit":
            res = 0
            while res == 0:
                print("\n")
                answer1 = questionary.text("Name of the habit").ask()
                exists = funccheckex(dbz, answer1)
                if exists == 1:
                    print("A habit with the name", answer1, "already exists. Choose another one.")
                else:
                    res = 1
                
            res = 0 
            while res == 0:
                print("\n")
                answer2 = questionary.text("What is the frequenz of the habit").ask()
                [res, per] = checkperiod(answer2)
                if res == 1:
                    print("Ok, we add the habit", answer1, "with the frequenz", per)
                    newhabit(dbz, answer1, answer2)
                elif res == 2:
                    print("Do you mean period = ", per, "?")
                    answer3 = questionary.select("Please confirm", choices=["yes", "no"]).ask()
                    if answer3 == "yes":
                        newhabit(dbz, answer1, per)
                        print("Ok, we add the habit", answer1, "with the frequenz", per)
                    else:
                        res = 0
                        print("Try it again. The frequenz must be day, week or an integer.")
                else:
                    print("No the frequenz must be day, week or an integer")
        
        elif choice == "Exit":
            stop = True 
            print("See you soon")
    

 
if __name__ == "__main__":    
    dbz = DatabaseConnection()
    dbz.maketable()
     
    mainmenue()