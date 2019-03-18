import os
import csv

#Set variables
totalMonths = 0
netTotal = 0
avgChange = 0
previousChange = 0
changeList = []
monthOfChange = []
greatestIncreaseProfit = ["", 0]
greatestDecreaseLoss = ["", 0]
totalAvgChange = 0

#Path to collect data from folder
PyBankCSV = os.path.join( "budget_data.csv")

# Read in the CSV file
with open(PyBankCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.DictReader(csvfile, delimiter=',')

    # Loop thru to find total months
    for row in csvreader:

        #Total number of months included in the dataset:
        totalMonths = totalMonths + 1

        #The net total amount of "Profit/Losses" over the entire period
        netTotal = netTotal + int(row["Profit/Losses"])

        #The average of the changes in "Profit/Losses" over the entire period
        avgChange = float(row["Profit/Losses"]) - previousChange
        previousChange = float(row["Profit/Losses"])
        changeList = changeList + [avgChange]
        monthOfChange = [monthOfChange] + [row["Date"]]

        #The greatest increase in profits (date and amount) over the entire period
        if avgChange > greatestIncreaseProfit[1]:
            greatestIncreaseProfit[1] = avgChange
            greatestIncreaseProfit[0] = row["Date"]
    
        #The greatest decrease in losses (date and amount) over the entire period
        if avgChange < greatestDecreaseLoss[1]:
            greatestDecreaseLoss[1] = avgChange
            greatestDecreaseLoss[0] = row["Date"]
    totalAvgChange = sum(changeList)/len(changeList)

#Print functions
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {totalMonths}")
print (f"Net Total: ${netTotal}")
print(f"Average Change: ${totalAvgChange}")
print(f"Greatest Increase in Profits: {greatestIncreaseProfit[0]}, {greatestIncreaseProfit[1]}")
print(f"Greatest Decrease in Losses: {greatestDecreaseLoss[0]}, {greatestDecreaseLoss[1]}")

#Set output of text file 
text_file = "text_file.txt"

#Exporting to a text file
with open(text_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-----------------------\n")
    file.write("Total Months: %d\n" % totalMonths)
    file.write("Net Total: $%d\n" % netTotal)
    file.write("Average Change: $%d\n" % totalAvgChange)
    file.write(f"Greatest Increase in Profits: {greatestIncreaseProfit[0]}  $({greatestIncreaseProfit[1]})\n")
    file.write(f"Greatest Decrease in Losses: {greatestDecreaseLoss[0]} $({greatestDecreaseLoss[1]})\n")