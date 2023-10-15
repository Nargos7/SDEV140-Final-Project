from CalendarApp import CalendarApp
from ScheduleApp import ScheduleApp
from Images import Images
from PIL import Image, ImageTk
import random
from tkinter import Tk
import time

# Simulate user interactions for CalendarApp
def simulate_calendar_app():
    root_calendar = Tk()
    app_calendar = CalendarApp(root_calendar)

    # Simulate clicking the "Get Date" button
    app_calendar.grab_date()

    # Wait for a moment to observe the changes (you can adjust the time)
    time.sleep(2)

    # Close the Tkinter window
    root_calendar.destroy()

# Simulate user interactions for ScheduleApp
def simulate_schedule_app():
    root_schedule = Tk()
    app_schedule = ScheduleApp(root_schedule, "2023-10-15")  # Replace "2023-10-15" with the date you want to test

    # Simulate entering an activity and saving it
    app_schedule.activity_var.set("Workout")
    app_schedule.save_activity()

    # Simulate showing activities
    app_schedule.show_activities()

    # Wait for a moment to observe the changes (you can adjust the time)
    time.sleep(2)

    # Simulate exiting the app
    app_schedule.exit_app()

# Simulate user interactions for Images module
def simulate_image_module():
    # Simulate generating CalendarImages
    Images.CalendarImages()
    print("Generated Calendar Image:", Images["CalendarImages"])

    # Simulate generating ScheduleImages
    Images.ScheduleImages()
    print("Generated Schedule Image:", Images["ScheduleImages"])

# Run the simulations
simulate_calendar_app()
simulate_schedule_app()
simulate_image_module()