import os
import csv

profit_loss=[]
pl_summary={}
total=0
total_months=0

#open csv file
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

    #Skip header row
    csv_header = next(csvfile)


    for line in csvreader:
        profit_loss.append(line)

        # The total net amount of "Profit/Losses" over the entire period
        total+=int(line[1])
        
        # The total number of months included in the dataset
        total_months+=1
       
    subtract_month=0
    total_MoM=0
    Avg_Mom=0
    # Initialize max increase and max decrease values with latest increase/decrease value
    max_decrease=int(profit_loss[total_months-1][1])-int(profit_loss[total_months-2][1])
    max_increase=int(profit_loss[total_months-1][1])-int(profit_loss[total_months-2][1])

    # Calc the change in "Profit/Losses" between months over the entire period
    
    for i in range(total_months,1,-1): # stops when i is 2
        subtract_month=int(profit_loss[i-1][1])-int(profit_loss[i-2][1])

        # Find the Greatest Increase (max_increase) and Greatest Decrease (max_decrease)

        if subtract_month < max_decrease:
            min_month_yr=profit_loss[i-1][0]
            max_decrease=subtract_month
        elif subtract_month > max_increase:
            max_increase=subtract_month
            max_month_yr=profit_loss[i-1][0]

        # Total amount change in "Profit/Losses" between months over the entire period
        total_MoM=total_MoM+subtract_month

    #The average change in "Profit/Losses" between months over the entire period    
    Avg_MoM=total_MoM/(total_months-1)

print('Financial Analysis')
print('----------------------------')
print('Total Months: '+str(total_months))
print('Total: $'+str(total))
print('Average  Change: $'+str(round(Avg_MoM,2)))
print('Greatest Increase in Profits: '+max_month_yr+' ($'+str(max_increase)+')')
print('Greatest Decrease in Profits: '+min_month_yr+' ($'+str(max_decrease)+')')