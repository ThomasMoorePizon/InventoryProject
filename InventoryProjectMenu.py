#Thomas E. Moore-Pizon, Jr.

#Needed for graphically widows
from PyQt5 import QtWidgets, QtCore, QtGui

#Database Functions
from InventoryProjectDataBaseFunctions import *

class InventoryWindow(QtWidgets.QMainWindow):
	def __init__(self):

		#Create the Widget
		QtWidgets.QMainWindow.__init__(self)

		#Call setup to create window
		self.setup()


	def setup(self):

		#Add Window Title Inventory
		self.setWindowTitle('Inventory')

		#Adjust the location and size of the Window
		self.setGeometry(100, 100, 800, 400)

		#Create the Menu Bar and use the local Menu
		menu_bar = self.menuBar()
		menu_bar.setNativeMenuBar(False)

		#Add File to the Menu Bar
		file_menu = menu_bar.addMenu('File')

		#Create the New DataBase Action and Add to File Menu
		newdb_action = QtWidgets.QAction('Create New Database', self)
		newdb_action.triggered.connect(self.newdbCall)
		file_menu.addAction(newdb_action)

		#Create the Open DataBase Action and Add to File Menu
		opendb_action = QtWidgets.QAction('Open Database', self)
		opendb_action.triggered.connect(self.opendbCall)
		file_menu.addAction(opendb_action)

		#Create the Exit Action and Add to File Menu
		exit_action = QtWidgets.QAction('Exit', self)
		exit_action.triggered.connect(QtWidgets.qApp.quit)
		file_menu.addAction(exit_action)

		#Show the Window
		self.show()

	def newdbCall(self):
		
		#Create Input Dialog for Name of Database
		dbname, okPressed= QtWidgets.QInputDialog.getText(self, "Database Name", "Databasename.db", QtWidgets.QLineEdit.Normal,"")
		if okPressed and dbname !='':
			#Calls our Database Function to Creates a new database named dbname
			sql_connection(dbname)

	def opendbCall(self):
		
		#Create Input Dialog for Name of Database
		dbname, okPressed= QtWidgets.QInputDialog.getText(self, "Database Name", "Databasename.db", QtWidgets.QLineEdit.Normal,"")
		if okPressed and dbname !='':
			#Calls our Database Function to Creates a new database named dbname
			sql_connection(dbname)




