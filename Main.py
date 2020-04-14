#Thomas E. Moore-Pizon, Jr.

#Needed for system interface
import sys

#Class that defines the Window and Menu System
from InventoryProjectMenu import *

if __name__ == "__main__":

	#Create the application - always just one application
	app = QtWidgets.QApplication(sys.argv)

	#Calls the object to create the window
	main_window = InventoryWindow()

	#Run the application
	app.exec_()

