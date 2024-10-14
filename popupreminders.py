import tkinter as tk
from tkinter import messagebox
import schedule
import time
from datetime import datetime

def create_welcome_popup():
    def on_submit():
        if var1.get() and var2.get() and var3.get() and var4.get() and messagebox.askyesno("Yes", "will you make victoria happy?"):
            root.destroy()
        else:
            messagebox.showwarning("Incomplete", "Please check all boxes before closing.")

    root = tk.Tk()
    root.title('Scheduled Notification')
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable the close button

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    var4 = tk.IntVar()

    tk.Label(root, text="HEY SHIFTER! YEAH YOU!", fg="red", wraplength=400, font=("Helvetica", 34)).pack()
    tk.Checkbutton(root, text="Check #nts-ops and #nts-team (and the annoucements). Keep #nts-ops OPEN YOUR WHOLE SHIFT!", variable=var1, fg="red", wraplength=400, font=("Helvetica", 12)).pack()
    tk.Checkbutton(root, text="Look at previous shifter's notes for you and start a new shifter log!", variable=var2, fg="red", wraplength=400, font=("Helvetica", 12)).pack()
    tk.Checkbutton(root, text="Before using NTS-1, fieldhub01, or fieldhub02 inform #nts-ops", variable=var3, fg="red", wraplength=400, font=("Helvetica", 12)).pack()
    tk.Checkbutton(root, text="Check for ESD safety (anything touching the mainboards?)", variable=var4, fg="red", wraplength=400, font=("Helvetica", 12)).pack()
    tk.Button(root, text="Yes I'm sure I did these things (or else victoria will be very sad)", command=on_submit, fg="red", wraplength=400, font=("Helvetica", 12)).pack()

    # Make the window modal
    root.grab_set()
    root.focus_force()
    root.mainloop()

def create_end_popup():
    def on_submit():
        if var1.get() and var2.get() and var3.get() and messagebox.askyesno("Yes", "will you make victoria happy?"):
            root.destroy()
        else:
            messagebox.showwarning("Incomplete", "Please check all boxes before closing.")

    root = tk.Tk()
    root.title('Scheduled Notification')
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable the close button

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    var3 = tk.IntVar()

    tk.Label(root, text="HEY SHIFTER! YEAH YOU!", fg="red", wraplength=400, font=("Helvetica", 34)).pack()
    tk.Checkbutton(root, text="Fill out your shifter log NOW!", variable=var1, fg="red", wraplength=400, font=("Helvetica", 12)).pack()
    tk.Checkbutton(root, text="Triple check to make sure EVERYTHING is connected appropriately before ticking this box", variable=var2, fg="red", wraplength=400, font=("Helvetica", 12)).pack()
    tk.Checkbutton(root, text="Inform #nts-ops you are done with your server and shift", variable=var3, fg="red", wraplength=400, font=("Helvetica", 12)).pack()
    tk.Button(root, text="I am ready to leave my shift!", command=on_submit, fg="red", wraplength=400, font=("Helvetica", 12)).pack()

    # Make the window modal
    root.grab_set()
    root.focus_force()
    root.mainloop()

def schedule_popup(welcome_times, end_times, days, end_date):
    def welcome_job():
        if datetime.now() < end_date:
            create_welcome_popup()
        else:
            schedule.clear()

    def end_job():
        if datetime.now() < end_date:
            create_end_popup()
        else:
            schedule.clear()

    for time_str in welcome_times:
        for day in days:
            schedule.every().day.at(time_str).do(welcome_job).tag(day)

    for time_str in end_times:
        for day in days:
            schedule.every().day.at(time_str).do(end_job).tag(day)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Example usage
# test times
# end_times = ["14:36"]
# days = ["monday"]
welcome_times = ["09:00", "16:00"]  # Times of the day to show the popup
end_times = ["11:50", "14:50"]  # Times of the day to show the popup
days = ["monday, tuesday, wednesday, thursday, friday"]  # Days of the week to show the popup
end_date = datetime(2024, 12, 31)  # End date for the schedule

schedule_popup(welcome_times, end_times, days, end_date)