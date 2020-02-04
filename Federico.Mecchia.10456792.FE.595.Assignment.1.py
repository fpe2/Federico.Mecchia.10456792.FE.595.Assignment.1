# Federico Mecchia - CWID: 10456792

# FE 595

# Assignment 1



# Student: Federico Mecchia

# CWID: 104567592



# Course: FE 595 - Financial Technology

# Professor: Kenneth Blaney

# Spring 2020



# Assignment 1



# Academic Integrity

# The following pledge shall be written in full and signed by every student
# on all submitted work (including, but not limited to, homework, projects,
# lab reports, code, quizzes and exams) that is assigned by the course
# instructor.
# No work shall be graded unless the pledge is written in full and signed.

# I pledge my honor that I have abided by the Stevens Honor System.

# Signature: Federico Mecchia
# CWID: 10456792
# Date: 02/03/2020



# For "Assignment 1" I have come up with two possible
# solutions, identified by "Option 1" and "Option 2".



# Option 1



import numpy as np

import matplotlib.pyplot as plt

xop1 = np.linspace(0, 2*np.pi, num=500)

y1op1 = np.sin(xop1)

y2op1 = np.cos(xop1)

plt.plot(xop1, y1op1, 'green', label='Sine Function')

plt.plot(xop1, y2op1, 'orange', label='Cosine Function')

plt.grid('True')

plt.title('Graph of One Period of Sine and Cosine functions', fontsize=15)

plt.xlabel('x')

plt.ylabel('sin(x) and cos(x)')

plt.legend()

plt.show()



# Option 2



import numpy as np

import matplotlib.pyplot as plt

xop2 = np.arange(0, 2*np.pi, step=0.001)

y1op2 = np.sin(xop2)

y2op2 = np.cos(xop2)

plt.plot(xop2, y1op2, 'red', label='Sine Function')

plt.plot(xop2, y2op2, 'blue', label='Cosine Function')

plt.grid('True')

plt.title('Graph of One Period of Sine and Cosine functions', fontsize=15)

plt.xlabel('x')

plt.ylabel('sin(x) and cos(x)')

plt.legend()

plt.show()



# Comment

# First I import "numpy" and "matplotlib.pyplot".
# I then generate the values of "x", identified by "xop1" in "Option 1"
# and by "xop2" in "Option 2". I created "xop1" in "Option 1" and by "xop2"
# in "Option 2" by using different methods. To this regard, in fact, I created
# "xop1" by using "np.linspace()" and by including in the brackets "0", which
# is the starting point, "2*np.pi", since I am interested in representing just
# one period of the Sine and Cosine functions, and "num=500", which represents
# the number of samples that have to be generated. For "Option 2", instead, I
# used "np.arange()" to create "xop2" and I included "0", which is the
# starting point, "2*np.pi", since I am interested in representing just one
# period of the Sine and Cosine functions, and "step=0.001".
# Furthermore, for both "Option 1" and "Option 2" I used "np.sin()" to take
# into consideration the Sine function (I thus created "y1op1" and "y1op2")
# and also "np.cos()" to take into consideration the Cosine function (I thus
# created "y2op1" and "y2op2").
# Moreover, I used "plt.plot()" to plot "xop1" and "y1op1" in "Option 1" and
# "xop2" and "y1op2" in "Option 2" and then I used again "plt.plot()" to plot
# "xop1" and "y2op1" in "Option 1" and "xop2" and "y2op2" in "Option 2"; I
# also selected the colors for "y1op1", "y2op1", "y1op2" and "y2op2" and I
# also added the corresponding labels.
# In addition to this, I also used "plt.grid()" and included "True" in the
# brackets to display the grid in the brackets, "plt.title()" to add the
# title (I also selected the "fontsize"), "plt.xlabel()" to give a name to
# the "x-axis", "plt.ylabel()" to give a name to the "y-axis" and
# "plt.legend()" to display the legend.
# Lastly I used "plt.show()" to display the graphs.


