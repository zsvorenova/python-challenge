# import required modules
import os
import csv

# set variables needed and their starting value
total_month = 0
total_profit = 0
profit = 0
total_change = 0
max_change = 0
min_change = 0

#open the csv file and read data 
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    
    budget_header = next(budget_data)
    # set variables needed and their starting value

    # as reading data calculate
    for row in budget_data:
        # the total number of months included in the data set
        total_month += 1
        # change in profit and record it in next column
        change_profit = int(row[1])-profit
        profit = int(row[1])
        # total profit for the data set
        total_profit += profit
        # total change in profit 
        total_change += change_profit
        # identify maximum increase in profit
        if change_profit > max_change:
            max_change = change_profit
            max_month = str(row[0])
        # identify the maximum decrease in profit
        if change_profit < min_change:
            min_change = change_profit
            min_month = str(row[0])

    # calculate average change in profit during the period
    average_change = round((total_change / total_month),2)

# Generate summary of results
output = (
    f"\nFinancial Analysis\n"
    f"-------------------------------\n"
    f"Total Months: {total_month}\n"
    f"Total Profit: ${total_profit}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {max_month} (${max_change})\n"
    f"Greatest Decrease in Profits: {min_month} (${min_change})\n"
   )
  
# Print all of the results (to terminal)
print(output)

# Save the results to analysis text file
file_to_output = os.path.join("analysis", "PyBank_analysis.txt")
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


