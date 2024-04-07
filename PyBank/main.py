
import os
import csv

#2 columns of data



#find csv file to read
csvpath = os.path.join("PyBank","Resources","budget_data.csv")
#open and read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

#    read header row first
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

#    number of months of data
for row in csv.reader:
  
    row_count = sum(1 for row in ('csv.reader'))

#read each row of data after the header
#for rows in csvreader:
       
#print(rows)

#loop through to find the below calculations

#Calculate for PyBank
#   Total number of months included in data set


#   net change in Profit/Loss over the whole period

#       the average of that change


#   Date & amount of the greatest increase in profits over the whole period


#   Date & amount of the greatest decrease in profits over the whole period

