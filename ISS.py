#Importing dependancies 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as img 
import requests

#Sets map variable to be global 
global wmap

fig = plt.figure()
#Background World Map Image Import
wmap = img.imread('map.jpg')

#Requests the ISS position from the Open Notify API 
def getcords():
    #Error handling; In case of internet outage or other connection faults will print failure and set graph to null island
    try:
        responce = requests.get('http://api.open-notify.org/iss-now.json')
        responcejson = responce.json()
        responcepos = responcejson.get('iss_position')
        responcex = responcepos.get('longitude')
        responcey = responcepos.get('latitude')
        return(responcex,responcey)
    except:
        print("An error has occured. Please try again later")
        return(0, 0)

#Function for creating the graph
def graph(i):
    #Resets variables for run
    BBox = [-180, 180, -90, 90]
    xcord = []
    ycord = []
    #Get cords from function and append to lists 
    cords = getcords()
    xcord.append(float(cords[0]))
    ycord.append(float(cords[1]))
    #Clear current graph points
    plt.cla()
    #Display map
    plt.imshow(wmap, zorder=0, extent = BBox, aspect= 'equal')
    #Create graph (alpha changes opacity; c changes colour (currently hex value); s changes dot size)
    plt.scatter(xcord, ycord, zorder=1, alpha= 1, c='#ff2d00', s=20)
    #Debugging / Finding ISS cords; Has been commented out
    #print(xcord, ycord)
    #Set graph axies and titles
    plt.title('ISS Postition')
    plt.xlim(-180,180)
    plt.ylim(-90,90)
    
#Change graph every 5 seconds; Do not set to change more frequently to avoid overloading API;
#5 seconds is enough to display upto date data on graph of this size
ani = animation.FuncAnimation(fig, graph, interval=5000)
plt.show()
