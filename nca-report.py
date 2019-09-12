#!/usr/bin/python

import os, sys, linecache

# Open a file
path = os.getcwd() + "/"
dirs = os.listdir( path )

def reportonfile( driverpt ):
    # This opens file and extracts start and end date and time
	ncatimestamp = {'START': '0', 'STOP': '0'}
	startstr = "#start".lower()
	stopstr = "#stop".lower()
	linecount = 0
	with open(driverpt) as fo:
		fileline = fo.readline()
		while fileline:
			linecount += 1
			if fileline.lower().find(startstr) != -1:
	   			ncatimestamp['START'] = linecount
				# print "Line With START is :- ", linecount
			if fileline.lower().find(stopstr) != -1:
				ncatimestamp['STOP'] = linecount 	
 				# print "Line With STOP is :- ", linecount
 			fileline = fo.readline()
    # print filecontent
	fo.close()
	# print " - Line With START is :- ", linecache.getline(driverpt,ncatimestamp['START'])
	# print " - Line With STOP is :- ", linecache.getline(driverpt,ncatimestamp['STOP'])

	genline = driverpt + ';' + linecache.getline(driverpt,ncatimestamp['START']) + ';' + linecache.getline(driverpt,ncatimestamp['STOP'])
	
	return genline;

def scrubdata(reportcontent):
	# This method removes unwanted text and replaces all commas with semi-colons
    wkngcontent1 = reportcontent.replace(path,"")
    wkngcontent2 = wkngcontent1.replace("#START,","")
    wkngcontent3 = wkngcontent2.replace("#STOP,","")
    wkngcontent1 = wkngcontent3.replace(",,",";")
    wkngcontent2 = wkngcontent1.replace(",",";")
    wkngcontent3 = wkngcontent2.replace("None","")
    wkngcontent1 = wkngcontent3.replace("\n","")

    wkngcontent1 = "\n" + wkngcontent1 
    return wkngcontent1

# This would print all the files and directories
filenames = ['report.py']
counter = 0
for file in dirs:
    filenames.insert(counter, path + file)
    # print file
    counter += 1

# Removing script file from the final report 
filenames.remove('report.py')
filenames.remove(path + 'report.py')

# Writing the report file header
print('FILE NAME ;START TIME ;START DATE ;STOP TIME ;STOP DATE ')
fwriter = open(path + "zellsreport.csv","wb")
fwriter.write('FILE NAME ;START TIME ;START DATE ;STOP TIME ;STOP DATE ')
fwriter.close()

for spread in filenames:
	# print spread
	writedatasource = scrubdata(reportonfile(spread))
	if writedatasource is not None:
		fwriter = open(path + "zellsreport.csv","a+")
		fwriter.write(writedatasource)
		fwriter.close()

	print writedatasource
