#Thomas E. Moore-Pizon, Jr.

#Needed for graphically widows
from PyQt5 import QtWidgets, QtCore, QtGui

#Global database name variable set to the Test database
dbname = 'Test.db'
tablename = 'TestTable'

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

		#Create Table Menu
		table_menu = menu_bar.addMenu('Tables')

		#View Tables
		viewtables_action = QtWidgets.QAction('View Tables', self)
		viewtables_action.triggered.connect(self.viewtablesCall)
		table_menu.addAction(viewtables_action)

		#Create Table
		createtable_action = QtWidgets.QAction('Create Table', self)
		createtable_action.triggered.connect(self.createtableCall)
		table_menu.addAction(createtable_action)

		#Open Table
		opentable_action = QtWidgets.QAction('Open Table', self)
		opentable_action.triggered.connect(self.opentableCall)
		table_menu.addAction(opentable_action)

		#Create Products Menu
		table_menu = menu_bar.addMenu('Products')

		#View Products in Table
		viewprod_action = QtWidgets.QAction('View Products in Table', self)
		viewprod_action.triggered.connect(self.viewprodCall)
		table_menu.addAction(viewprod_action)

		#Add Products to a Table
		addprod_action = QtWidgets.QAction('Add Products to Table', self)
		addprod_action.triggered.connect(self.addprodCall)
		table_menu.addAction(addprod_action)

		#Show the Window
		self.show()


	def newdbCall(self):

		#Make use of the global database name variable		
		global dbname

		#Create Input Dialog for Name of Database
		dbname, okPressed= QtWidgets.QInputDialog.getText(self, "Database Name Form", "Databasename.db", QtWidgets.QLineEdit.Normal,"")
		if okPressed and dbname !='':
			#Calls our Database Function to Creates a new database named dbname
			sql_connection(dbname)


	def opendbCall(self):
		
		#Make use of the global database name variable
		global dbname

		#Create Input Dialog for Name of Database
		dbname, okPressed= QtWidgets.QInputDialog.getText(self, "Database Name Form", "Databasename.db", QtWidgets.QLineEdit.Normal,"")
		if okPressed and dbname !='':
			#Calls our Database Function to Creates a new database named dbname
			sql_connection(dbname)

	def viewtablesCall(self):

		#Make use of the global database name variable
		global dbname

		#Calls our Database Function which displays the table list to the command window
		sql_viewtables(dbname)

	def createtableCall(self):

		#Make use of the global database name variable
		global dbname
		
		#Make use of the global table name variable
		global tablename		

		#Create Input Dialog for Name of Table
		tablename, okPressed= QtWidgets.QInputDialog.getText(self, dbname, "Input the name of the table that you want to create", QtWidgets.QLineEdit.Normal,"")
		if okPressed and tablename !='':
			#Calls our Database Function to create a new table in the currently open database
			sql_createtable(dbname, tablename)

	def opentableCall(self):

		#Make use of the global database name variable
		global dbname

		#Make use of the global table name variable
		global tablename

		#Create Input Dialog for Name of Table
		tablename, okPressed= QtWidgets.QInputDialog.getText(self, dbname, "Input the name of the table that you want to open", QtWidgets.QLineEdit.Normal,"")
		if okPressed and tablename !='':
			#Calls our Database Function to create a new table in the currently open database
			sql_opentable(dbname, tablename)	

	def addprodCall(self):

		#Make use of the global database name variable
		global dbname
		
		#Make use of the global table name variable
		global tablename

		#Create Input Dialog for Name of the Product
		prodname, okPressed= QtWidgets.QInputDialog.getText(self, dbname + tablename, "productname", QtWidgets.QLineEdit.Normal,"")
		if okPressed and prodname !='':
			#Calls our Database Function to create a new table in the currently open database
			sql_createprod(dbname, tablename, prodname)

	def viewprodCall(self):

		#Make use of the global database name variable
		global dbname
		
		#Make use of the global table name variable
		global tablename

		sql_viewall(dbname, tablename)
