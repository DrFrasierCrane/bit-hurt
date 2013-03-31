## This script takes in a long list of numbers and returns a text file full of CSVs. ##
# Written by Tyler Sartin on 29 March 2013 #

# Some example data sets. The name of the data then each number with no separation.
set1 = "AJ 0.05 0.2 0.4 0.1 0.5 0.7 0.08 0.2 0.4 0.01 0.02 0.06 0.03 0.05 0.08 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"
set2 = "JO 4.0 4.0 30.0 1.0 1.25 3.0 0.75 0.75 4.0 0.15 0.2 1.0 0.75 1.0 2.0 0.1 0.5 0.6 0.1 0.5 0.6 0.25 0.75 1.0 0.2 0.75 1.0 0.2 0.75 1.0 0.1 1.0 1.25 0.1 0.75 1.25 0.1 0.75 1.25 0.25 1.0 1.5"
set3 = "JB 0.5 2.0 5.0 3.0 5.0 7.0 3.0 5.0 7.0 1.0 2.0 3.0 1.0 2.0 3.0 0.1 0.2 0.3 0.1 0.2 0.3 0.1 0.2 0.3 0.2 0.3 0.4 0.15 0.25 0.35 0.05 0.15 0.2 0.05 0.15 0.2 0.2 0.25 0.3 0.1 0.2 0.3"
set4 = "BSG 3.0 5.0 10.0 1.0 10.0 15.0 1.0 10.0 15.0 1.0 5.0 10.0 1.0 5.0 10.0 1.0 2.0 5.0 0.5 1.0 2.0 0.5 1.0 2.0 2.0 5.0 27.0 2.0 5.0 27.0 1.0 2.0 5.0 1.0 2.0 5.0 2.0 5.0 27.0 5.0 10.0 15.0" 
set5 = "JW 0.6 1.0 2.0 0.6 1.5 3.0 0.6 1.0 2.0 0.6 1.0 2.0 0.6 1.0 2.0 0.7 0.5 0.2 0.7 0.5 0.2 0.7 0.5 0.2 0.7 0.5 0.2 0.7 0.5 0.2 0.7 0.5 0.2 0.7 0.5 0.2 0.7 0.5 0.2 0.7 0.5 0.2"
set6 = "KF 1.0 3.0 5.0 2.0 3.0 8.0 0.5 1.0 3.0 2.0 4.0 8.0 0.2 1.0 2.0 0.2 1.0 3.0 0.2 1.0 2.0 0.2 1.0 2.0 0.2 1.0 2.5 0.2 1.0 2.5 0.5 3.0 5.0 0.5 2.0 4.0 0.2 1.0 2.5 0.5 2.0 4.0"


# Place all data sets into a list and create a new file named 'target_file.csv'. You can 
# change this name to whatever you want.
all = [set1, set2, set3, set4, set5, set6]
file = open('target_file.csv', 'w')

# Split the data and join by commas for full comma separated value file.
for i in all:
	i = ','.join(i.split())
	file.write(i)
	file.write("\n")

file.close()