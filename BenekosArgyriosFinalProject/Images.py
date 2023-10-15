from PIL import Image, ImageTk
import random

Images = {}

def CalendarImages():
    global Images
# Lists for background Images
    background = ['Images/agenda.png']    
    Images = {
# Randomly imports the CalendarApp background picture       
        "CalendarImages": ImageTk.PhotoImage(Image.open(random.choice(background)))}

def ScheduleImages():
    global Images
# Lists for background Images
    background = ['Images/schedule.png']    
    Images = {
#  Randomly imports the ScheduleApp background picture     
        "ScheduleImages": ImageTk.PhotoImage(Image.open(random.choice(background)))}
