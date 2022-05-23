import tkinter
from tkinter import filedialog
from datetime import datetime
import os

root = tkinter.Tk()

def openBrowser():
    filename = filedialog.askopenfilename(initialdir='/Desktop', title='Select a file', filetypes=(('all files', '*.*'),('executables', '*.exe')))
    return filename


def calcs():
    day_of_week = ['MO','TU','WE','TH','FR']
    days_of_weekend = ['SA','SU']
    week_schedule1_start = datetime.strptime('00:01', '%H:%M').time()
    week_schedule1_end = datetime.strptime('09:00', '%H:%M').time()
    week_schedule2_start = datetime.strptime('09:01', '%H:%M').time()
    week_schedule2_end = datetime.strptime('18:00', '%H:%M').time()

    filename = openBrowser()
    file = open(filename, "r")
    file_lines = file.readlines()
    for lines in file_lines:
        paycheck = 0
        name = lines.split('=')[0]
        line = lines.split('=')[1]
        line = line.split(',')
        for day in line:
            if day[0:2] in day_of_week:
                day_time1 = datetime.strptime(day[2:7], '%H:%M')
                day_time2 = datetime.strptime(day[8:13], '%H:%M')
                if day_time1.time() >= week_schedule1_start and day_time2.time() <= week_schedule1_end:
                    time = (day_time2-day_time1)
                    time = str(time)[:1]
                    paycheck += int(time)*25
                elif day_time1.time() >= week_schedule2_start and day_time2.time() <= week_schedule2_end:
                    time = (day_time2-day_time1)
                    time = str(time)[:1]
                    paycheck += int(time)*15
                else:
                    time = (day_time2-day_time1)
                    time = str(time)[:1]
                    paycheck += int(time)*20
            elif day[0:2] in days_of_weekend:
                day_time1 = datetime.strptime(day[2:7], '%H:%M')
                day_time2 = datetime.strptime(day[8:13], '%H:%M')
                if day_time1.time() >= week_schedule1_start and day_time2.time() <= week_schedule1_end:
                    time = (day_time2-day_time1)
                    time = str(time)[:1]
                    paycheck += int(time)*30
                elif day_time1.time() >= week_schedule2_start and day_time2.time() <= week_schedule2_end:
                    time = (day_time2-day_time1)
                    time = str(time)[:1]
                    paycheck += int(time)*20
                else:
                    time = (day_time2-day_time1)
                    time = str(time)[:1]
                    paycheck += int(time)*25
        text = f'The amount to pay {name} is: {paycheck} USD'
        label = tkinter.Label(frame, text=text)
        label.pack()

canvas = tkinter.Canvas(root, height=300, width=500, bg='#263D42')
canvas.pack()

frame = tkinter.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

openFile = tkinter.Button(root, text='Open file', padx=10, pady=5, fg='white', bg='#263D42', command=calcs)
openFile.pack()

root.mainloop()