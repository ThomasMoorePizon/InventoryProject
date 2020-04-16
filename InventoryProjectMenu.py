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
		self.setGeometry(100, 100, 400, 100)

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

		#Delete Table
		deltable_action = QtWidgets.QAction('Delete Table', self)
		deltable_action.triggered.connect(self.deltableCall)
		table_menu.addAction(deltable_action)

		#Create Products Menu
		table_menu = menu_bar.addMenu('Products')

		#View Products in Table
		viewprod_action = QtWidgets.QAction('View Products in Table', self)
		viewprod_action.triggered.connect(self.viewprodCall)
		table_menu.addAction(viewprod_action)

		#Add Product to a Table
		addprod_action = QtWidgets.QAction('Add Product to Table', self)
		addprod_action.triggered.connect(self.addprodCall)
		table_menu.addAction(addprod_action)

		#Delete Product from a Table
		delprod_action = QtWidgets.QAction('Delete Products from a Table', self)
		delprod_action.triggered.connect(self.delprodCall)
		table_menu.addAction(delprod_action)

		#Create Inventory Menu
		table_menu = menu_bar.addMenu('Inventory')

		#View Products in Table
		viewinv_action = QtWidgets.QAction('View Inventory in Table', self)
		viewinv_action.triggered.connect(self.viewinvCall)
		table_menu.addAction(viewinv_action)

		#Update Inventory of a Product
		upinv_action = QtWidgets.QAction('Update Inventory of a Product', self)
		upinv_action.triggered.connect(self.upinvCall)
		table_menu.addAction(upinv_action)

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
			#Calls our Database Function to open a table in the currently open database
			sql_opentable(dbname, tablename)	

	def deltableCall(self):

		#Make use of the global database name variable
		global dbname

		#Create Input Dialog for Name of Table
		deltablename, okPressed= QtWidgets.QInputDialog.getText(self, dbname, "Input the name of the table that you want to delete", QtWidgets.QLineEdit.Normal,"")
		if okPressed and deltablename !='':
			#Calls our Database Function to open a table in the currently open database
			sql_deltable(dbname, deltablename)	


	def addprodCall(self):

		#Make use of the global database name variable
		global dbname
		
		#Make use of the global table name variable
		global tablename

		#Create Input Dialog for Name of the Product
		prodname, okPressed= QtWidgets.QInputDialog.getText(self, dbname + tablename, "productname", QtWidgets.QLineEdit.Normal,"")
		if okPressed and prodname !='':
			#Calls our Database Function to add a product in the currently open table
			sql_createprod(dbname, tablename, prodname)

	def viewprodCall(self):

		#Make use of the global database name variable
		global dbname
		
		#Make use of the global table name variable
		global tablename

		sql_viewall(dbname, tablename)

	def delprodCall(self):

		#Make use of the global database name variable
		global dbname
		
		#Make use of the global table name variable
		global tablename

		#Create Input Dialog for Name of the Product
		prodname, okPressed= QtWidgets.QInputDialog.getText(self, dbname + tablename, "productname", QtWidgets.QLineEdit.Normal,"")
		if okPressed and prodname !='':
			#Calls our Database Function to delete a product in the currently open table
			sql_delprod(dbname, tablename, prodname)

	def viewinvCall(self):

		#Make use of the global database name variable
		global dbname
		
		#Make use of the global table name variable
		global tablename

		sql_viewall(dbname, tablename)

	def upinvCall(self):

		#Make use of the global database name variable
		global dbname
		
		#Make use of the global table name variable
		global tablename

		#Create Input Dialog for Name of the Product
		prodname, okPressed= QtWidgets.QInputDialog.getText(self, dbname + tablename, "productname", QtWidgets.QLineEdit.Normal,"")
		if okPressed and prodname !='':

			#Create Input Dialog for the Inventory Count
			qty, okPressed= QtWidgets.QInputDialog.getText(self, dbname + tablename, "inventory count", QtWidgets.QLineEdit.Normal,"")
			if okPressed and prodname !='':

				#Calls our Database Function to delete a product in the currently open table
				sql_upinv(dbname, tablename, prodname, qty)



