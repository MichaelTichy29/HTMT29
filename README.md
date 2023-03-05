# Habit Tracker HTMT29
## What is HTMT29

The habit tracker HTMT29, is build to control your habits. So you can easyly define your habits and set the freuquenz you would like to do this as "day," "week" or an arbitrary integer. 
To use this App you should check out the habit each time you have done this. It is only allowed one time per habit and day. So its not built for shorter frequenzes or to count the number of done in a period.
It is only possible to check out a habit for the current day. So you can't add data for the past (or the future.

Additional it is possible to remove the data for the current day. So you can correct your database if you just have choosen the wron habit or something like this.

By the definition of a habit the frequenz "week" means one time in the calendary week (from monday to sunday). Of course "day" means that this should be done each day at least one time. 
If you set an arbitrary integer then this means the time (in day) between two definitions of done for this habit. So 7 is something else as "week." (But of course "day" and 1 is the same.)

At least ou can analyse your habits if you hve actual a streak of certain successfull periods (Think of the difference between "week" and 7), how long is this streak or if you struggle currently. Beyond this you can also analyse the past. How long was the longest streak in one habit or over all habits.

## Installation

The packackes 
- Questionary
- unittest
- pytest

are needed. So you can install them each for its own by pip install -r xyz.py
or all the packages by using the **requirements.txt** with
pip install -r requirements.txt


## How to handel HTMT29

To use the habit tracker just run  **questionhabits.py**
Now you can follow the instructions on the desktop. You have to use the command line to choose the option what you want to do in the currente menue. In the main menue you have the choice to
- Check out a habit
- Delete a check out of today
- analyse your habits
- Add a new habit
- exit the program

Depending on your choice on this level you have further options respectively have to input a name or a period.


## How to test HTMT29

The test of the program is splitted into two parts

1. Test the analysing class: This is implemented by unittest. So you have to run **unittest.main.py**
2. The test of the database connection and the controlling part ist done by pytest. So you have to run **test\_pymainhabits.py** with pytest. 


