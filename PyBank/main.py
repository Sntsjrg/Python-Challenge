import csv
import os

#set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

#Initalize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
loss_changes = []
dates = []

#Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])

        #Calculate months
        total_months += 1

        #Calculate the net total amount of "Profit/Losses"
        net_total += profit_loss

        #Calculate the change in "Profit/Losses" since the previous month
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            loss_changes.append(change)
            dates.append(date)
        previous_profit_loss = profit_loss

#Calculate the average change in "Profit/Losses"
total_change = sum(loss_changes)
average_change = total_change/(total_months-1)

# Print the analysis results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")