#Thomas E. Moore-Pizon, Jr.

#sqlite3 provides the link to the database
import sqlite3
from sqlite3 import Error

def sql_connection(dbname):

	try:

		#Open a connection to the database and creates one if there is none
		con = sqlite3.connect(dbname)
		cursor = con.cursor()
		
		#Table Debug Code
		#sql_tabledebug(cursor)
		
		con.close()

	except Error:
		print(Error)

def sql_tabledebug(cursor):

	#Debug Code Creates a Table and List all of The Current Tables
	cursor.execute("CREATE TABLE IF NOT EXISTS `product`(product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT)")
	cursor.execute("select * from SQLite_master where type=\"table\"")
	print("Tables available in the in-memory database(main):")
	tables = cursor.fetchall()
 
	print("Listing tables from SQLite_master:")
	for table in tables:
		print("------------------------------------------------------")
		print("DB Object Name: %s"%(table[0]))
		print("Name of the database object: %s"%(table[1]))
		print("Table Name: %s"%(table[2]))
		print("Root page: %s"%(table[3]))
		print("SQL statement: %s"%(table[4]))
		print("------------------------------------------------------")


