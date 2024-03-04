# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: October 28, 2023

# Description:
# This program contains the Calculator_GUI class. This class provides a GUI,
# which prompts the user to enter a month, day, and year (after 1582).
# Once this information is input, the user can click the Calculate button
# and the GUI will display the day of the week that this date falls on.
# The user can also click the Exit button to close the GUI and end the program.

# Logic:
# import tkinter, tkinter.messagebox
# class Calculator_GUI:
#   init:
#       main window = tkinter.tk
#       title = 'Day of the Week Calculator'
#       initialize top, middle, and bottom frames
#       create top frame widgets:
#           month prompt = Label('Month: ')
#           month field = Entry
#           day prompt = Label('Day: ')
#           day field = Entry
#           year prompt = Label('Year: ')
#           year field = Entry
#       pack top frame widgets(side='left')
#       create middle frame widgets:
#           outText = StringVar
#           outLabel = Label(outText)
#       pack middle frame widget
#       create bottom frame widgets:
#           calculate button = Button('Calculate', command=calc_day)
#           exit button = Button('Exit', command=destroy)
#       pack bottom frame widgets(side='left')
#       pack each frame
#       tkinter.mainloop()
#   calc_day:
#       get month, day, year
#       if not month, day, and year: display error messagebox, return
#       try: int(month, day, and year)
#       except: display error messagebox, return
#       if year < 1583: display error messagebox, return
#       if month not between 1 and 12: display error messagebox, return
#       call day_valid
#       if False: display error messagebox, return
#       if month is 1 or 2: month += 12, year -= 1
#       w = self.day + 2 * (self.month) + int(0.6 * (self.month + 1)) \
#           + self.year + int(self.year / 4) - int(self.year / 100) \
#           + int(self.year / 400) + 2
#       outText = w % 7
#   day_valid:
#       if month in [1, 3, 5, 7, 8, 10, 12]:
#           max days = 31
#       if month in [4, 6, 9, 11]:
#           max days = 30
#       if month == 2:
#           if year multiple of 4:
#               if year multiple of 100:
#                   if year multuple of 400:
#                       max days = 29
#                   else:
#                       max days = 28
#               else:
#                   max days = 29
#           else:
#               max days = 28
#       if day > max days: return False
#       else: return True
# gui = Calculator_GUI()
     

# import tkinter module to create GUI
# import tkinter.messagebox to use for displaying messageboxes
import tkinter, tkinter.messagebox

# declare Calculator_GUI class for creating GUI
class Calculator_GUI:
    # initialization method for GUI
    def __init__(self):
        # create main window widget
        self.main_window = tkinter.Tk()
        # create title for main window
        self.main_window.title(f'Day of the Week Calculator')

        # create top frame for prompts and entry widgets
        self.top_frame = tkinter.Frame(self.main_window)
        # create middle frame for displaying output
        self.middle_frame = tkinter.Frame(self.main_window)
        # create bottom frame for button widgets
        self.bottom_frame = tkinter.Frame(self.main_window)

        
        # create label in top frame prompting for month input
        self.month_prompt = tkinter.Label(self.top_frame, 
                                          text=f'Month: ')
        
        # create entry widget for user to input month
        self.month_field = tkinter.Entry(self.top_frame, width=12)

        # create label in top frame prompting for day input
        self.day_prompt = tkinter.Label(self.top_frame,
                                        text=f'Day: ')

        # create entry widget for user to input day
        self.day_field = tkinter.Entry(self.top_frame, width=12)

        # create label in top frame promptingfor year input
        self.year_prompt = tkinter.Label(self.top_frame, 
                                         text=f'Year: ')

        # create entry widget for user to input year
        self.year_field = tkinter.Entry(self.top_frame, width=12)

        # pack month prompt label
        self.month_prompt.pack(side='left')
        # pack month entry field
        self.month_field.pack(side='left')
        # pack day prompt label
        self.day_prompt.pack(side='left')
        # pack day entry field
        self.day_field.pack(side='left')
        # pack year prompt label
        self.year_prompt.pack(side='left')
        # pack year entry field
        self.year_field.pack(side='left')

        # create string variable object for output text
        self.out_text = tkinter.StringVar()
        # create label in middle frame to display output
        self.out_label = tkinter.Label(self.middle_frame,
                                       textvariable=self.out_text)

        # pack output label
        self.out_label.pack()

        # create calculate button in bottom frame, which calls calc_day method
        self.calc_button = tkinter.Button(self.bottom_frame,
                                               text=f'Calculate',
                                               command=self.calc_day)

        # create exit button in bottom frame, which will call destroy method
        self.exit_button = tkinter.Button(self.bottom_frame,
                                          text=f'Exit',
                                          command=self.main_window.destroy)

        # pack calculate button
        self.calc_button.pack(side='left')
        # pack exit button
        self.exit_button.pack(side='left')

        # pack top frame
        self.top_frame.pack()
        # pack middle frame
        self.middle_frame.pack()
        # pack bottom frame
        self.bottom_frame.pack()

        # enter tkinter main loop
        tkinter.mainloop()

    # method to calculate day of the week for input date
    def calc_day(self):
        # read in user month input using get method
        entered_month = self.month_field.get()
        # read in user day input using get method
        entered_day = self.day_field.get()
        # read in user year input using get method
        entered_year = self.year_field.get()
        
        # check if there is month input
        if not entered_month:
            # if not, display messagebox with error message
            tkinter.messagebox.showinfo(f'Invalid Entry',
                                        f'No month entered.')
            # end calc_day
            return

        # check if there is day input
        if not entered_day:
            # if not, display messagebox with error message
            tkinter.messagebox.showinfo(f'Invalid Entry',
                                        f'No day entered.')
            # end calc_day
            return

        # check if there is year input
        if not entered_year:
            # if not, display messagebox with error message
            tkinter.messagebox.showinfo(f'Invalid Entry',
                                        f'No year entered.')
            # end calc_day
            return

        # try suite for input validation
        try:
            # try to convert month input to integer
            self.month = int(entered_month)
            # try to convert day input to integer
            self.day = int(entered_day)
            # try to convert year input to integer
            self.year = int(entered_year)

        # if there is an error with any of these...
        except:
            # display messagebox with error message
            tkinter.messagebox.showinfo(f'Invalid Entry',
                                        f'Please enter only numbers.')
            # end calc_day
            return

        # check if year is before 1583
        if self.year <= 1582:
            # if it is, display messagebox with error message
            tkinter.messagebox.showinfo(f'Invalid Entry',
                                        f'Year must be after 1582.')
            # end calc_day
            return

        # check if month input is between 1-12
        if not 1 <= self.month <= 12:
            # if it is not, display messagebox with error message
            tkinter.messagebox.showinfo(f'Invalid Entry',
                                        f'Month must be between 1 - 12')
            # end calc_day
            return

        # determine if day is valid by calling day_valid method
        if not self.day_valid():
            # if day is not valid, display messagebox with error message
            tkinter.messagebox.showinfo(f'Invalid Entry',
                                        f'{self.month_name} {self.year} only '
                                        f'has {self.max_days} days.')
            # end calc_day
            return

        # check if month is Jan or Feb
        if self.month in [1, 2]:
            # if it is, per the algorithm, make it month 13 or 14...
            self.month += 12
            # of the previous year
            self.year -= 1

        # initialize list with days of the week, where Saturday is day 0
        days_of_week = ['Saturday', 'Sunday', 'Monday', 'Tuesday',
                        'Wednesday', 'Thursday', 'Friday']

        # use provided algorithm to calculate w
        w = self.day + 2 * (self.month) + int(0.6 * (self.month + 1)) \
            + self.year + int(self.year / 4) - int(self.year / 100) \
            + int(self.year / 400) + 2

        # assign day of week to output string variable by calculating
        # remainder when w is divided by 7, then accessing the
        # corresponding index from the days of the week list
        self.out_text.set(f'Day of the Week: {days_of_week[w % 7]}')
        
    # method to check if day input is valid
    def day_valid(self):
        # initialize list with names of months 
        months = ['Janaury', 'Febuary', 'March', 'April', 'May', 'June','July',
                  'August', 'September', 'October', 'November', 'December']

        # initialize month name attribute by referencing month list
        self.month_name = months[self.month - 1]

        # check if month is one with 31 days
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            # if so, initialize max days attribute with 31
            self.max_days = 31

        # check if month is one with 30 days
        elif self.month in [4, 6, 9, 11]:
            # if so, initialize max days attribute with 30
            self.max_days = 30

        # otherwise, month is February
        else:
            # check if year is multiple of 4
            if (self.year % 4) == 0:
                # check if year is also multiple of 100
                if (self.year % 100) == 0:
                    # check if year is also multiple of 400
                    if (self.year % 400) == 0:
                        # if all are true, leap year, max days is 29
                        self.max_days = 29
                    # if multiple of 4 and 100 but not 400...
                    else:
                        # not leap year, max days is 28
                        self.max_days = 28
                # if multiple of 4 but not 100...
                else:
                    # leap year, max days is 29
                    self.max_days = 29
            # if not multiple of 4...
            else:
                # not leap year, max days is 28
                self.max_days = 28

        # check if input day is greater than max days
        if self.day > self.max_days:
            # if it is, day is invalid, return False
            return False
        # if it is not, day is valid, return True
        else:
            return True
                

# call main to execute program
if __name__ == '__main__':
    # create instance of Calculator_GUI
    gui = Calculator_GUI()
        
