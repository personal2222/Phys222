#Jan 15, 2015 
import numpy
import scipy
from pylab import *

def droppedBall():
    while True:
        # Defining constants
        g = 9.81

        # Ask for user input
        h = float(input("Please input tower's height (in meters) "))
        t = float(input("How long does the ball fall? (in seconds) "))

        # Calculate the height above the ground
        s = 1/2*g*t**2
        ballHeight = h-s

        # Print the result
        if ballHeight > 0:
            print("\nThe ball's height from the ground is " + str(ballHeight) + "m\n")
        else:
            print("\nThe ball had already hit the ground\n")

        # Ask the user to play it again or not   
        EXIT = input("Hit Enter to play it again\nOtherwise hit any key and then hit enter to quit ") != ""
        if EXIT:
            break



def satelliteAltitude():
    while True:
        # Defining constants
        G = 6.67e-11
        M = 5.97e24
        R = 6371e3

        # Ask for user input
        T = float(input("Please enter the period of the satellite (in minutes) "))
        T_sec = T * 60

        # Calculate the altitude
        altitude = ((G*M*(T_sec)**2/(4*pi**2)) ** (1/3)) -R
        altitude_km = altitude/1000

        # Print the result
        if altitude_km > 0:
            print("\nThe altitude of the satellite is: " + str(altitude_km) + "km\n")
        else:
            print("\nIt is impossible for a satellite to have such period\n")
        

        # Ask the user to play it again or not
        EXIT = input("Hit Enter to play it again\nOtherwise hit any key and then hit enter to quit ") != ""
        if EXIT:
            break


satelliteAltitude()
# It is not possible for a satellite to orbit in a period of 45min
# The altitude for T = 90min is: 279.3216253728606km
