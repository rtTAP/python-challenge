import os
import csv

greatest_increase = 0
greatest_decrease = 0
sum_change = 0

#find csv file to read
csvpath = os.path.join("PyBank", "Resources","budget_data.csv")

#open and read csv file
with open(csvpath, 'r') as csvfile:
    budgetdata = csv.reader(csvfile)

    #read header row first
    csv_header = next(budgetdata)

    # Loop to read the data
    rows = []
    for row in budgetdata:
        rows.append(row)

greatest_increase = 0
greatest_decrease = 0
sum_change = 0
sum_profit = int(rows[0][1])
num_change = 0
time_of_greatest_increase = ''
time_of_greatest_decrease = ''

for i in range(1, len(rows)):
    # Sum the total profit and loss over the period
    sum_profit += int(rows[i][1])
    #sum_profit = sum_profit + int(rows[i][1])

    # Calculate the change between this month and last month
    change = int(rows[i][1]) - int(rows[i-1][1])

    # Calculate the sum of change
    sum_change += change
    #sum_change = sum_change + change
    num_change = num_change + 1

    # Track the greatest increase
    if change > greatest_increase:
        greatest_increase = change
        time_of_greatest_increase = rows[i][0]

    # Track the greatest decrease
    if change < greatest_decrease:
        greatest_decrease = change
        time_of_greatest_decrease = rows[i][0]

average_change = round(sum_change/num_change, 2)

print("Total Months: " + str(len(rows)))
print("Total: " + "$" + str(sum_profit))
print("Average Change: " + "$" + str(average_change))
print("Greatest Increase in Profits: " + time_of_greatest_increase + " $" + str(greatest_increase))
print("Greatest Decrease in Profits: " + time_of_greatest_decrease + " $" + str(greatest_decrease))