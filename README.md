# ACMEpaycheck

<h4>Requirements:</h4>
- Python 3.x
<br>
<h4>How to run the project:</h4>
- Clone the repository from github with the follow link: https://github.com/Alvarez-Luis/ACMEpaycheck.git <br>
- go to the file where you downloaded the code <br>
- Execute the command python main.py <br>
- Click in the button calculate to read the output.

<br>

<h4>Overview:</h4>
The program reads a file, which is in the same folder of the project, with the data of the employees and their respective working hours; when the user clicks on the calculate button, the program takes those hours and calculates the total pay for each one.
Each employee's pay is displayed in a table in the program.

<h4>Approach to solution:</h4>
The python program uses tkinter to create a simple GUI to interact with the user, it displays a window with a frame where the processed information is displayed, and a button to call the methods to perform the calculations.
The solution has two files that contain the methods to read, process and print the information; main.py file contains two methods:<br>
open_browser: that reads a file named data.txt and returns that file.<br>
calcs: which does some initial calculations, and creates an instance of calc_methods which is a class of the methods.py file,
at the end of the method it prints the respective employee's name and salary. <br>

methods.py contains a class called calc_methods, this class contains three methods:<br>
constructor: contains an initialization from some values of schedules and day_time to store the working time of each employee.<br>
is_weekend: static method, which receives a day, returns true if the day is in the list, otherwise it returns false.<br>
payment_calc: method that receives a day and a bool, this method evaluates the range of hours and places the hour of work depends on the range, multiplies the total hours of work with the price of the horn in that range.
It returns the payment in each iteration.
