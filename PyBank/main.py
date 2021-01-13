import os
import csv

#Define variables

months = []
months_total = profitChange = 0
Dates = []
p = []
Net_total_profit = 0
changes_profit_loss = []
changes_date = []
Profit_loss = 0
Differences = []
Greatest_Increase_Date = ""
Greatest_Decrease_Date = ""
average_net_change = 0
net_change = []



#open csv file
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

    #Skip header row
    csv_header = next(csvfile)

    #read through the row of csv
    for row in csvreader:
  
        #calc total number of months
        months_total +=1

        #calc total profit
        Net_total_profit += int(row[1])
        changes_profit_loss.append(int(row[1]))

        #calculate the monthly changes
        changes_date.append(row[0])
        previous = int(row[1])
        change = int(row[1])- previous


        #changes_profit_loss.append(int(row[1]))
        profitChange = profitChange + [change]
        length = len(profitChange) - 1

        #Calculate the profit change
        meanProfitChange = sum(profitChange[1:])/ length

        #calculate the greatest increase in profits
        increase = max(profitChange)

        #calculate greatest decrease in profits
        decrease = min(profitChange)

        

print("Financial Analysis")
print("-------------------------------")
print("Total Months: " + str(months_total))
print("Net Total Profits: " + str(Net_total_profit))
print("Profit Change:" + str(meanProfitChange))