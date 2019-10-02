#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  capture.py
#  

import time
import sqlite3
import os # for getting temp

dbname='sensorsData.db'
sampleFreq = 2 # time in seconds


# Get temp
def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        temp = (temp.replace("'C\n",""))
        logData (temp.replace("temp=",""))
        #return (temp.replace("temp=",""))


# log sensor data on database
def logData (temp):
	
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	
	curs.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (temp, temp))
	conn.commit()
	conn.close()

# display database data
def displayData():
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	print ("\nEntire database contents:\n")
	for row in curs.execute("SELECT * FROM DHT_data"):
		print (row)
	conn.close()

# main function
def main():
	for i in range (0,3):
		measure_temp()
		time.sleep(sampleFreq)
	displayData()

# Execute program 
main()