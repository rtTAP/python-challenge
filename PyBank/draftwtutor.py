
import os
import csv

#create variables for calculations
total_months = 0
month_of_change = []
net_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
total_net = 0

#find csv file to read
csvpath = os.path.join("PyBank","Resources","budget_data.csv")
#open and read csv file
with open(csvpath) as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=',')
    csvreader = csv.reader(csvfile)

    #print(csvreader)

#read header row first
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')
    first_row = next(csvreader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])


#read each row of data after the header
#loop through to find 
#Calculate for PyBank
#   Total number of months included in data set

    for row in csvreader:
      
     total_months += 1   
     total_net += int(row[1])

     net_change = int(row[1]) - prev_net
     prev_net = int(row[1])
     net_change_list = [net_change]
     month_of_change += [row[0]]

     

     #greatest_increase[1] = int(row[1]) - prev_net
     

#if net_change >= greatest_increase[1]:
    #greatest_increase = [month_of_change, net_change]

     #greatest_decrease <= [net_change]


    print(net_change)
    print(total_months)
    print(total_net)
    #print(greatest_increase)





#   net change in Profit/Loss over the whole period


#       the average of that change
        #def average(Profit/Losses):

#   Date & amount of the greatest increase in profits over the whole period
         

#   Date & amount of the greatest decrease in profits over the whole period

