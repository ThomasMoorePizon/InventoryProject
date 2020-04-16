#Thomas E. Moore-Pizon, Jr.

#Path to storage location for databases
dbfolder = "\\Databases\\"

#sqlite3 provides the link to the database
import sqlite3
from sqlite3 import Error

#Needed for graphically widows
from PyQt5 import QtWidgets, QtCore, QtGui

def sql_connection(dbname):

	path = dbfolder + dbname

	try:

		#Open a connection to the database and creates one if there is none
		con = sqlite3.connect(path)
		cursor = con.cursor()
				
		con.close()

	except Error:
		print(Error)

def sql_viewtables(dbname):

	path = dbfolder + dbname

	try:

		#Open a connection to the database and creates one if there is none
		con = sqlite3.connect(path)
		cursor = con.cursor()

		#Select all of the tables
		cursor.execute("select * from SQLite_master where type=\"table\"")

		#Grab all of the tables
		tables = cursor.fetchall()
 
		#Print the tables information to the command window
		print("Listing tables from SQLite_master:")
		for table in tables:
			#print("------------------------------------------------------")
			#print("DB Object Name: %s"%(table[0]))
			#print("Name of the database object: %s"%(table[1]))
			print("Table Name: %s"%(table[2]))
			#print("Root page: %s"%(table[3]))
			#print("SQL statement: %s"%(table[4]))
			#print("------------------------------------------------------")				
		con.close()

	except Error:
		print(Error)


def sql_createtable(dbname, tablename):

	path = dbfolder + dbname

	try:

		#Open a connection to the database and creates one if there is none
		con = sqlite3.connect(path)
		cursor = con.cursor()
		
		#Creates a Table
		dbcommand = '''CREATE TABLE IF NOT EXISTS ''' + tablename  + '''(product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty INTEGER);'''
		cursor.execute(dbcommand)
		
		con.close()

	except Error:
		print(Error)

def sql_opentable(dbname, tablename):
	
	path = dbfolder + dbname

	try:

		#Open a connection to the database and creates one if there is none
		con = sqlite3.connect(path)
		cursor = con.cursor()
		
		#See if the table exists
		tableselect ="SELECT count(name) FROM sqlite_master WHERE type='table' AND name=\'" + tablename + "\'"
		cursor.execute(tableselect)

		#If the count is 1, then the table exists
		if cursor.fetchone()[0]==1 :
			print()
		else :
			print('Error - Table does not exist')
	except Error:
		print(Error)
	
	con.commit()
	con.close()

def sql_deltable(dbname, deltablename):
	
	path = dbfolder + dbname

	try:

		#Open a connection to the database and creates one if there is none
		con = sqlite3.connect(path)
		cursor = con.cursor()
		
		#See if the table exists
		tableselect ="SELECT count(name) FROM sqlite_master WHERE type='table' AND name=\'" + deltablename + "\'"
		cursor.execute(tableselect)

		#If the count is 1, then the table exists
		if cursor.fetchone()[0]==1 :
			droptablecommand = "DROP TABLE " + deltablename
			cursor.execute(droptablecommand)
		else :
			print('Error - Table does not exist')
	except Error:
		print(Error)
	
	con.commit()
	con.close()

def sql_createprod(dbname, tablename, prodname):

	path = dbfolder + dbname

	try:

		#Open a connection to the database and creates one if there is none
		con = sqlite3.connect(path)
		cursor = con.cursor()
		
		#See if the table exists
		tableselect ="SELECT count(name) FROM sqlite_master WHERE type='table' AND name=\'" + tablename + "\'"
		cursor.execute(tableselect)

		#If the count is 1, then the table exists
		if cursor.fetchone()[0]==1 :
			insertcommand ="INSERT INTO " + tablename + "(product_name) VALUES(\"" + prodname + "\")"
			cursor.execute(insertcommand)
		else :
			print('Error - Table does not exist')

	except Error:
		print(Error)
	
	con.commit()
	con.close()
	
def sql_viewall(dbname, tablename):

	path = dbfolder + dbname

	try:

		#Open a connection to the database and creates one if there is none
		con = sqlite3.connect(path)
		cursor = con.cursor()
		
		#See if the table exists
		tableselect ="SELECT count(name) FROM sqlite_master WHERE type='table' AND name=\'" + tablename + "\'"
		cursor.execute(tableselect)

		#If the count is 1, then the table exists
		if cursor.fetchone()[0]==1 :
			rowselect ="SELECT * FROM " + tablename
			cursor.execute(rowselect)
			rows = cursor.fetchall()
			for row in rows:
				print(row)

		else :
			print('Error - Table does not exist')

	except Error:
		print(Error)
	
	con.commit()
	con.close()

def sql_delprod(dbname, tablename, prodname):

	path = dbfolder + dbname

	try:

		#Open a connection to the database and creates one if there is none
		con = sqlite3.connect(path)
		cursor = con.cursor()
		
		#See if the table exists
		tableselect ="SELECT count(name) FROM sqlite_master WHERE type='table' AND name=\'" + tablename + "\'"
		cursor.execute(tableselect)

		#If the count is 1, then the table exists
		if cursor.fetchone()[0]==1 :
			deletecommand ="DELETE from " + tablename + " where product_name =\"" + prodname + "\""
			cursor.execute(deletecommand)
		else :
			print('Error - Table does not exist')

	except Error:
		print(Error)
	
	con.commit()
	con.close()

def sql_upinv(dbname, tablename, prodname, qty):

	path = dbfolder + dbname

	try:

		#Open a connection to the database and creates one if there is none
		con = sqlite3.connect(path)
		cursor = con.cursor()
		
		#See if the table exists
		tableselect ="SELECT count(name) FROM sqlite_master WHERE type='table' AND name=\'" + tablename + "\'"
		cursor.execute(tableselect)

		#If the count is 1, then the table exists
		if cursor.fetchone()[0]==1 :
			updatecommand ="UPDATE " + tablename + " SET product_qty = " + qty + " where product_name = \""  + prodname + "\""
			cursor.execute(updatecommand)
		else :
			print('Error - Table does not exist')

	except Error:
		print(Error)
	
	con.commit()
	con.close()
