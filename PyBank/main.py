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

# Find the greatest increase and decrease in profits
max_increase = max(loss_changes)
max_increase_index = loss_changes.index(max_increase)
max_increase_date = dates[max_increase_index]

max_decrease = min(loss_changes)
max_decrease_index = loss_changes.index(max_decrease)
max_decrease_date = dates[max_decrease_index]

# Print the analysis results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

# Specify the file to write to
output_path = os.path.join("Analysis", "new.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline ="") as outputfile:
    writer = csv.writer(outputfile)

    #Output text
    writer.writerow(["Financial Analysis"])
    writer.writerow(["------------------------"])
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Total: ${net_total}"])
    writer.writerow([f"Average Change: ${average_change:.2f}"])
    writer.writerow([f"Greatest Increase in Profits: {max_increase_date} (${max_increase})"])
    writer.writerow([f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})"])