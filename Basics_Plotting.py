# Name: Sareen Mohammad
# 
# Student-ID: 203651
#
# Rename the file to <sareen>06.py
#

# useful imports
import math
import matplotlib.pyplot as plt
import numpy as np

#
def exercise1():
    """
    My first plot. 
    """
    # close all figures
    plt.close('all')

    # set fontsize to 16
    plt.rc('font', size=16)

    # create a new figure with a single subplot
    fig, ax = plt.subplots()

    # Task 1A: plot x against y1 = sin(10*x) * exp(-x/2) as blue line
    x = np.arange(0, 3*np.pi, 0.02)
    y = np.sin(10*x) * np.exp(-x/2)

    ax.plot(x, y, 'b')


    # Task 1B: plot envelope functions in red and green
    y2 = np.exp(-x/2) 
    y3 = -np.exp(-x/2)
    ax.plot(x, y2, 'r')
    ax.plot(x, y3, 'g')   
   


    # Task 1C: set axis limits
    ax.set_xlim(0, 3*np.pi)
    ax.set_ylim(-1.2, 1.2)
    
    
    # Task 1D: show grid
    ax.grid()


    # Task 1E: set xticks
    ax.set_xticks([0, np.pi, 2*np.pi, 3*np.pi])
    

    # Task 1F: change tick labels
    ax.set_xticklabels([r'$0$', r'$\pi$', r'$2\pi$', r'$3\pi$'])
   
   # Task 1G: set title
    ax.set_title('My first plot')

    # Task 1H: x and y labels
    ax.set_xlabel('x-axis [x-unit]')
    ax.set_ylabel('y-axis [y-unit]')

    # Task 1I: add a legend
    ax.legend([
    r'$\sin(10x)e^{-x/2}$',
    r'$+e^{-x/2}$',
    r'$-e^{-x/2}$'  ])

    # Task 1J: save figure as PNG file
    filename = 'MyFirstPlot.png'

    fig.tight_layout()
    fig.savefig(filename)
    plt.show()
    return fig, ax



### Exercise 2: 2D plot with two different y-axes

def exercise2():
    
    # close all figures
    plt.close('all')
    
    # set fontsize to 16
    plt.rc('font', size=16)

    # Task 2A: Plot height and velocity as a function of time in a single subplot
    # using different y-axes
    
    h0 = 100 
    g = 9.81 
     
    t = np.linspace(0,np.sqrt(2 * h0 / g), 50)
    
    h = h0 - 0.5 * g * t**2
    v = g * t
    
    fig, ax = plt.subplots()
    ax2 = ax.twinx()

    ax.plot(t,h,'r')
    ax2.plot(t,v,'b')
    
    
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax2.set_yticks([0,10, 20, 30, 40])

    # Task 2B: Set x-axis and y-axis labels as well as the title 

    ax.set_xlabel('time [s] ')
    ax.set_ylabel('height [m]', color='red')
    ax2.set_ylabel('velocity [m/s]', color='blue')
    
    # Task 2C: Set the axis limits and save the figure in a file

    ax.set_title('Freely falling object')
    
    filename = 'Freelyfallingobject.png'

    fig.tight_layout()
    fig.savefig(filename)
    plt.show()
    return fig, ax


#
def exercise3():

    # keyword figsize determines height and width of figure
    # setting figsize here to ensure that plot has square shape
    fig, ax = plt.subplots(figsize=(5, 5))

    # Task 3A: plot a full circle

    r =10
    thetha = np.linspace(0, 2*np.pi)
    
    x = r * np.cos(thetha)
    y = r * np.sin(thetha)
    
    ax.plot(x,y)
    
    
    
    # Task 3B: plot full circles at different centers

    r = 1

    ax.plot(4 + r*np.cos(thetha),  3.5 + r*np.sin(thetha))
     
    ax.plot(-4 + r*np.cos(thetha),  3.5 + r*np.sin(thetha))
   
    ax.plot(0 + r*np.cos(thetha), -1.5 + r*np.sin(thetha))
    
    # Task 3C: circle segment

    segment = np.linspace(5/4*np.pi, 7/4*np.pi, 300)
    r = 8

   # x = 0.0 + r * np.cos(pi)
   # y = 1.5 + r * np.sin(pi)
    
    
    ax.plot(0.0 + r * np.cos(segment), 1.5 + r * np.sin(segment), lw=10)
   
    #plt.plot(x, y)
    
    plt.show()
    return fig, ax


# Exercise 4: NumPy warmup

#
def exercise4():

    a = np.array([[ 7,  4,  1, 11],
                  [ 3, 10,  2, -8],
                  [ 6,  9,  0,  5]])
    
    # Task 4A: Find and print the minimum value of 'a' by using a NumPy function

    print('Task 4A:', np.min(a))


    # Task 4B: Print the row and column index of the smallest entry in 'a' by using
    # NumPy functions

    row, col = np.where(a == a.min())
    print('Task 4B:', row[0], col[0])

    # Task 4C: Create and print the matrix \cos(2\pi m n/N) for N=6 and
    # n, m in {0, 1, ..., 5}
    

    N = 6

    n = np.arange(N).reshape(N, 1)[[0,2,3,4,5]]
    m = np.arange(N)                


    C = np.cos(2 * np.pi * n * m / N)


    print('Task 4C:', C)

    
    # Task 4D: Evaluate and print the given polynomial at x=0, 1, 2, 3, 4, 5


    x = np.array([0, 1, 2, 3, 4, 5])

    f = -1 + 2*x - 3*x**2 + 4*x**3

    print('Task 4D:',f)
 
