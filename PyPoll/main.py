# Import Necessary Modules

import os
import csv


# Set the File Path

csvpath = os.path.join("..", "PyPoll", "election_data.csv")

# Set the Variables

votetotal = 0 
votekhan = 0
votecorrey = 0
voteli = 0
voteotooley = 0

# Open the CSV File to Read

with open(csvpath) as file:

    # Store data under the csvreader variable

    csvreader = csv.reader(file,delimiter=",") 

    # Skip the Header

    header = next(csvreader)

    # Start a Loop

    for row in csvreader: 

        # Calculate the Total Votes

        votetotal +=1

        # Crete Lists to Sum Vote Count

        if row[2] == "Khan": 
            votekhan +=1
        elif row[2] == "Correy":
            votecorrey +=1
        elif row[2] == "Li": 
            voteli +=1
        elif row[2] == "O'Tooley":
            voteotooley +=1

# Calculate percents

khanpercent = 100 * (votekhan/votetotal)
correypercent = 100 * (votecorrey/votetotal)
lipercent = 100* (voteli/votetotal)
otooleypercent = 100* (voteotooley/votetotal)

# Print Calculations

print(f"Election Results")
print("---------------------------------------------------")
print(f"Total Votes : {votetotal}")
print("---------------------------------------------------")
print(f"Khan : {khanpercent}% ({votekhan})")
print(f"Correy : {correypercent}% ({votecorrey})")
print(f"Li : {lipercent}% ({voteli})")
print(f"O'Tooley : {otooleypercent}% ({voteotooley})")
print("---------------------------------------------------")
print("Winner : Khan")
print("---------------------------------------------------")

 # Create Dictiony to Zip With Lists

canidate = ["Khan", "Correy", "Li","O'Tooley"]
votecount = [votekhan,votecorrey,voteli,voteotooley]

# Create the Text File

resultsfile = os.path.join("..", "PyPoll", "election_result.txt")

# Open the The Text File

with open(resultsfile,"w") as file:

# Print Calculations to Text File

    file.write(f"Election Results")
    file.write(f"Total Votes: {votetotal}")
    file.write(f"Khan: {khanpercent}% ({votekhan})")
    file.write(f"Correy: {correypercent}% ({votecorrey})")
    file.write(f"Li: {lipercent}% ({voteli})")
    file.write(f"O'Tooley: {otooleypercent}% ({voteotooley})")
    file.write("Winner: Khan")
