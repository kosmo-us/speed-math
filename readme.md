## Speed math challenge

A simple speed math python program to improve your speed math.
Currently in alpha phase, more features to be added. Please raise issues if you find bugs or want new features/tasks.



### Known issues:
- Reciprocal test: minor float handling issue.     <code>fixed</code> 
- Final input prompt in a task keeps running after time out until an input is given.

### How to run:

#### Windows:

Since windows users usually aren't familiar with the command line. I decided to release builds especially for windows.<br>
Follow the steps below to download the exe file.
- Go to [releases](https://github.com/kosmo-us/speed-math/releases)
- Find the latest release 
- Download the zip -> extract -> run the exe.

<br>*Windows defender may flag the executable as "unrecognised" but it is completely safe to run the file. If you still have doubts, you can just follow the next method below which has the source visible*

#### General (for every OS including windows):

- Download this repo directly or run <code>git clone https://github.com/kosmo-us/speed-math.git</code> in your terminal.
- Change to "app" directory
- Excute <code>python main.py</code> in your terminal

This needs to have python3 installed on your machine, recommended python version: python 3.6+

### Implementations to come:

- Custom full challenge mode to choose which tasks to include in the full challenge mode with custom time limit.
- Store the custom challenge profiles to disk.
- Rapid mode, a short challenge mode with random tasks to complete.    <code>Added, renamed to challenge mode</code>
- GUI version of the program

### How to use this program

You may go through the complete challenge which is a compilation of all the tasks available, each task has a set period of time to complete
or practice specific tasks as well. Scores are available immediately after a task is completed or, in case of complete challenge, after the complete challenege has been completed. Date wise scores can saved to a csv file within the program directory.
<br>
<br>
**Tips to improve speed math**

- Memorize all the squares upto 30 and cubes upto 15.
- While adding, add two digits at a time instead of 1. E.g. 4843+8663, here start with 63+43 then 48+86 and so on...rest the usual addition method.
- Memorize multipliction tables upto at least 30
- Memorize exponents of 2 and 3 upto 15 and 10 respectively
- Memorize reciprocals upto 11/x for all x at least upto 12
- You can use learn some vedic math to learn short ways to do certain calculations
