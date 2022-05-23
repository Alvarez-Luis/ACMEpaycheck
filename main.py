import tkinter

from methods import calc_methods


root = tkinter.Tk()

def open_browser():
    file = open('data.txt', "r")
    return file


def calcs():
    calc_methods_instance = calc_methods()

    file = open_browser()
    file_lines = file.readlines()
    for lines in file_lines:
        paycheck = 0
        name = lines.split('=')[0]
        line = lines.split('=')[1]
        line = line.split(',')
        for day in line:
            paycheck += calc_methods_instance.payment_calc(day, not calc_methods.is_weekend(day[0:2]))
        text = f'The amount to pay {name} is: {paycheck} USD'
        label = tkinter.Label(frame, text=text)
        label.pack()

canvas = tkinter.Canvas(root, height=300, width=500, bg='#263D42')
canvas.pack()

frame = tkinter.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

openFile = tkinter.Button(root, text='Calculate', padx=10, pady=5, fg='white', bg='#263D42', command=calcs)
openFile.pack()

root.mainloop()