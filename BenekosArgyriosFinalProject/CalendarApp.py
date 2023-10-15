'''
Argyrios Benekos
10-15-2023
A Schedule Application that helps organizing your life
'''
from tkinter import messagebox
from tkinter import Tk, Button, Label, PhotoImage, Toplevel
from tkcalendar import Calendar
from ScheduleApp import ScheduleApp
import Images

class CalendarApp:
    def __init__(self, root):
        self.root = root
        root.title("My Schedule")
        root.iconbitmap("d.ico")
        root.geometry("800x600")
        root.configure(background='blue')
        Images.CalendarImages()
        
        # Creating background for the Calendar window
        calendarLabel = Label(root, image = Images.Images["CalendarImages"])
        calendarLabel.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Set the Calendar
        self.cal = Calendar(root, selectmode="day", year=2023, month=10, day=14)
        self.cal.pack(pady=100)
        
        # Create buttons
        my_button = Button(root, text="Get Date", command=self.grab_date)
        my_button.pack(pady=20)
        
        # Create labels
        self.my_label = Label(root, text="")
        self.my_label.pack(pady=20)

        # Create functions
    def grab_date(self):
        selected_date = self.cal.get_date()
        self.my_label.config(text=selected_date)

        # Create ScheduleApp window and pass the selected date
        schedule_window = Toplevel()
        schedule_app = ScheduleApp(schedule_window, selected_date)

if __name__ == "__main__":
    root = Tk()
    app = CalendarApp(root)
    root.mainloop()