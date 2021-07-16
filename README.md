# Problem solving

Write a program that solves the most suitable (with most power) link station for a device at given point [x,y].
Please make this project as complete as you think it should be to be maintainable in the long term by more than one maintainer.
​Provide instructions how to run the solution or if applicable how to access a deployed running version.
This problem can be solved in 2-dimensional space. Link stations have reach and power.

### A link station’s power can be calculated:

    power = (reach - device's distance from linkstation)^2

if distance > reach, power = 0

### Program should output following line:

_Best link station for point x,y is x,y with power z_

or:

_No link station within reach for point x,y_

Link stations​ are located at points ​(x, y)​ and have reach ​(r) ([x, y, r])​:

    [[0, 0, 10],
    [20, 20, 5],
    [10, 0, 12]]

Print out function output from ​points​ ​(x, y):

    (0,0),
    (100, 100),
    (15,10)​,
    (18, 18)​

# Running locally

Requires Python 3.8+

    $ make install

Will setup virtual environment and install requirements to it

    $ make run

Will run program with default values and print out results

# Running tests locally

    $ py.test -vv tests
