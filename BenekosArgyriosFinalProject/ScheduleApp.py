from tkinter import messagebox, StringVar, Entry
from tkinter import Tk, Button, Label, PhotoImage
import Images

class ScheduleApp:
    def __init__(self, root, selected_date):
        self.root = root
        self.root.title("Schedule Maker")
        root.iconbitmap("d.ico")
        self.root.geometry("800x600")
        root.configure(background='yellow')
        Images.ScheduleImages()
        
        # Creating background for the Calendar window
        scheduleLabel = Label(root, image = Images.Images["ScheduleImages"])
        scheduleLabel.place(x=0, y=0, relwidth=1, relheight=1)

        # Display the selected date
        label_date = Label(root, text=f"Selected Date: {selected_date}")
        label_date.pack(pady=20)

        # Set up variables
        self.activity_var = StringVar()
        
         # Create a list to store activities associated with dates
        self.activities = []

        # Create labels
        label1 = Label(root, text="Enter your daily activity:")
        label1.pack()

        # Create entry box
        entry = Entry(root, textvariable=self.activity_var)
        entry.pack()

        # Create buttons
        button_save = Button(root, text="Save Activity", command=self.save_activity)
        button_save.pack()

        button_show = Button(root, text="Show Activities", command=self.show_activities)
        button_show.pack()

        button_exit = Button(root, text="Exit", command=self.exit_app)
        button_exit.pack()

    def save_activity(self):
        activity = self.activity_var.get()
        # Check if the activity is not empty and contains at least one non-space character
        if activity and any(char.isalnum() for char in activity):
            # Save the activity along with the selected date
            self.activities.append((self.root.title(), activity))
            messagebox.showinfo("Success", f"Activity saved: {activity}")
        else:
            messagebox.showwarning("Warning", "Please enter a valid activity.")

    def show_activities(self):
        # Display activities for the selected date
        activities_for_date = [activity for date, activity in self.activities if date == self.root.title()]

        if activities_for_date:
            activity_text = "\n".join(activities_for_date)
            messagebox.showinfo("Activities", f"Activities for {self.root.title()}:\n{activity_text}")
        else:
            messagebox.showinfo("No Activities", f"No activities recorded for {self.root.title()}.")


    def exit_app(self):
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = ScheduleApp(root, "default_date")
    root.mainloop()