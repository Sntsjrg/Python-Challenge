import csv
import os 

#set path for file
csvpath = os.path.join("Resources", "election_data.csv")

#Initalize variables
total_votes = 0 
candidate_votes = {}
candidates = []

#Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        #Update candidates vote count
        if candidate in candidate_votes:
            candidate_votes[candidate] +=1
        else:
            candidate_votes[candidate] = 1
            candidates.append(candidate)

#Initialize variables to find the winner
winner = ""
max_votes = 0

#Calculate and print results
print("Election Results")
print("------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------")

for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = ((votes/total_votes)*100)
    print(f"{candidate}: {percentage:.3f}%({votes})")

    #Find winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

#Calculate and print results
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")

# Specify the file to write to
output_path = os.path.join("Analysis", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline ="") as outputfile:
    writer = csv.writer(outputfile)

    #Output text
    writer.writerow(["Election Results"])
    writer.writerow(["------------------------"])
    writer.writerow([f"Total Votes: {total_votes}"])
    writer.writerow(["------------------------"])

    for candidate in candidates:
        votes = candidate_votes[candidate]
        percentage = ((votes/total_votes)*100)
        writer.writerow([f"{candidate}: {percentage:.3f}%({votes})"])

   #Output text
    writer.writerow(["------------------------"])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["------------------------"])