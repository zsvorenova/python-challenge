# import required modules
import os
import csv

total_month = 0
total_profit = 0
profit = 0
total_change = 0
max_change = 0
min_change = 0

csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    #print(budget_data)

    budget_header = next(budget_data)
    #print(f"CSV Header: {budget_header}")

    for row in budget_data:
        total_month += 1
        change_profit = int(row[1])-profit
        profit = int(row[1])
        total_profit += profit
        total_change += change_profit
        if change_profit > max_change:
            max_change = change_profit
            max_month = str(row[0])
        if change_profit < min_change:
            min_change = change_profit
            min_month = str(row[0])
        
        #print(profit, change)
        #change_profit += int(row[1])
        #change_profit = int(row[1]) - int((row-1)[1])

    average_change = round((total_change / total_month),2)

print(f"Financial Analysis")
print("-------------------------------------")
print(f"Total months: {total_month}")
print(f"Total profit: ${total_profit}")
print(f"Average change: ${average_change}")
print(f"Greatest increase in profits: {max_month} (${max_change})")
print(f"Greatest decrease in profits: {min_month} (${min_change})")
  
analysis = open(os.path.join("analysis", "PyBank_analysis.txt"),"a")

print(f"Financial Analysis", file = analysis)
print("-------------------------------------", file = analysis)
print((f"Total months: {total_month}"), file = analysis)
print((f"Total profit: ${total_profit}"), file = analysis)
print((f"Average change: ${average_change}"), file = analysis)
print((f"Greatest increase in profits: {max_month} (${max_change})"), file = analysis)
print((f"Greatest decrease in profits: {min_month} (${min_change})"), file = analysis)

analysis.close()
# months = str(budget_data[0])
# profit = float(budget_data[1])

# The total number of months included in the dataset
# # Returns the length of the List
# months = len(list(budget_data))
# print(months)

#months_total = 0
#total_profit = 0
#for row in open(os.path.join('Resources', 'budget_data.csv')):
 #  months_total += 1
  # total_profit += int(row[1])
#print(f"Total months: {months_total-1}")
#print(total_profit)

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period