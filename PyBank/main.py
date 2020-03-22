# Import Necessary Modules

import os
import csv

# Set the File Path

csvpath = os.path.join("..", "PyBank","budget_data.csv")

# Set up an Empty List to Hold the Variable Sum

months = []
profit = []
profitchange = []
 
# Open the CSV File to Read

with open(csvpath) as File:

     # Run the CSV File through the Reader

    csvreader = csv.reader(File,delimiter=",") 

    # Skip the Header

    header = next(csvreader)  

    # Start the Loop

    for row in csvreader: 

        # Sum the Variables

        months.append(row[0])
        profit.append(int(row[1]))

    # Calculate the change in Profit/Loss from the Prior Month

    for i in range(len(profit)-1):
        
        # Sum the Profit/Loss difference between Two Months

        profitchange.append(profit[i+1]-profit[i])
        
# Caculate Max and Min of the Profit/Loss Change

maxincrease = max(profitchange)
maxdecrease = min(profitchange)

# Tie the Max and Min Value to the Corresponding Date

maxincreasemonth = profitchange.index(max(profitchange)) + 1
maxdecreasemonth = profitchange.index(min(profitchange)) + 1 

# Print Calculations to Screen

print("Financial Analysis")
print("-----------------------------------------------------------------------------------------------")
print(f"Total Months : {len(months)}")
print(f"Total : $ {sum(profit)}")
print(f"Average Change : {(sum(profitchange)/len(profitchange))}")
print(f"Greatest Increase in Profits : {months[maxincreasemonth]} ($ {(str(maxincrease))})")
print(f"Greatest Decrease in Profits : {months[maxdecreasemonth]} ($ {(str(maxdecrease))})")

# Create the Text File

printedbudget = os.path.join("..", "PyBank", "printed_budget.txt")

# Open the The Text File

with open(printedbudget,"w") as file:
    
# Print Calculations to Text File

    file.write("Financial Analysis")
    file.write("--------------------------------------------------------------------------------------")
    file.write(f"Total Months :{len(months)}")
    file.write(f"Total : $ {sum(profit)}")
    file.write(f"Average Change : {(sum(profitchange)/len(profitchange))}")
    file.write(f"Greatest Increase in Profits : {months[maxincreasemonth]} ($ {(str(maxincrease))})")
    file.write(f"Greatest Decrease in Profits : {months[maxdecreasemonth]} ($ {(str(maxdecrease))})")