"""
Project to help with time distracted
Published Ross Hanson
Febuary 2016
"""


from Tkinter import *
import time


"""
An applet that will measure how much time I waste when I am working
"""
class DistractionStopper:

    time_distracted = 0.0
    start_of_time = 0.0
    end_of_time = 0.0

    """
    Takes time as a long, and returns a string printing out the days, hours, and minutes
    """
    def convert_time(self, temp_time):
        temp_time = int(temp_time)
        seconds = temp_time%60
        minutes = temp_time/60
        hours = minutes/60
        days = hours/24
        string_time = "time wasted = "
        if days > 0:
            string_time = string_time + "days: " + str(days) + " "
        if hours > 0 or days > 0:
            string_time = string_time + "hours: " + str(hours) + " "
        if minutes > 0 or hours > 0 or days >0:
            string_time = string_time + "minutes: " + str(minutes) + " "
        string_time = string_time + "seconds: " +str(seconds)
        return string_time
    
    def __init__(self, parent):
        #sets minimum size of window
        parent.minsize(width=20, height=5)

        #Creates the label which will show the time wasted
        self.time = Label(parent, text = self.convert_time(self.time_distracted))
        self.time.grid(column = 0, row = 0)

        #creates the start timer button
        self.start_timer = Button(parent, text = "Start", command = self.start_time)
        self.start_timer.grid(column = 1, row = 0)

        #creates the stop timer button
        self.stop_timer = Button(parent, text = "Stop", command = self.stop_time)
        self.stop_timer.grid(column = 2, row = 0)
        self.stop_timer['state'] = 'disabled'

        #creates the reset button
        self.reset_timer = Button(parent, text = "reset", command = self.reset_time)
        self.reset_timer.grid(column = 3, row = 0)
        self.reset_timer['state'] = 'disabled'

    """
    Sets the start point for for time distracted with start_of_time with time.time(), disables
    the start timer button, enables stop timer button
    """
    def start_time(self):
        self.start_of_time = time.time()
        self.start_timer['state'] = 'disabled'
        self.stop_timer['state'] = 'normal'

    """
    Calculates time diracted button from end _of time and start time by time.time. Disables
    stop time button, enables start timer button and reset button timer. Updates label
    """
    def stop_time(self):
        self.end_of_time = time.time()
        self.time_distracted = self.time_distracted + (self.end_of_time - self.start_of_time)
        self.start_timer['state'] = 'normal'
        self.stop_timer['state'] = 'disabled'
        self.reset_timer['stat'] = 'normal'
        self.time.configure(text = self.convert_time(self.time_distracted))
        
    """
    Resets the time distraced button. Diabels reset button. resets label
    """
    def reset_time(self):
        self.time_distracted = 0.0
        self.reset_timer['state'] = 'disabled'
        self.time.configure(text = self.convert_time(self.time_distracted))

# create root window
root = Tk();
root.title("DistractionStopper")
app = DistractionStopper(root)
root.mainloop()
