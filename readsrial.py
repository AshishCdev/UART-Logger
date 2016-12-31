#!/usr/bin/python

import serial	# import the python serial module 
import time	# import the python time module  

serial_ob = serial.Serial(port="/dev/ttyUSB0",baudrate=115200,timeout=2) # create the serial object with desired 
									 # settings use right value of baudrate
while 1:						# run forever
    serial_log = open('ttyUSB_out.csv','a')		# open the file named ttyUSB_out.csv 
    serial_log.write(str(time.strftime("%d/%m/%Y,%H:%M:%S,"))
			+str(serial_ob.readline())) # write the serial information into the file
    serial_log.close() # close the file



