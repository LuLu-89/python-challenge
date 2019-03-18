import os
import csv

#Set variables:
totalVotes = 0
candidateList = []
percentageVotes = {}
totalNumberVotes = 0
electionWinner = ""

#Path to collect data from folder
PyPoll_CSV = os.path.join( "election_data.csv")

# Read in the CSV file
with open(PyPoll_CSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.DictReader(csvfile, delimiter=',')

    # Loop thru to find total votes
    for row in csvreader:

        #Total number of votes:
        totalVotes = totalVotes + 1

        #Complete list of candidates who received votes:
        candidate = row["Candidate"]
        if candidate not in candidateList:
            candidateList.append(candidate)
            percentageVotes[candidate] = 1
           
        #Forming a list of unique candidates and dictionary with the candidate names and votes
        percentageVotes[candidate] = percentageVotes[candidate] + 1

        #Finding the winner
        for candidate in percentageVotes:
            votes = percentageVotes[candidate]
            candidateVotePercentage = (float(votes)/float(totalVotes) * 100)
            if (votes > totalNumberVotes):
                totalNumberVotes = votes
                electionWinner = candidate

#Print results
print("Election Results")
print("-----------------------")
print(f"Total Votes: {totalVotes}")
print("-----------------------")
#for candidate, candidateVotePercentage, votes in candidateList: 
# Keep getting an error that I don't know how to resolve :(
print(f"{candidate}: {candidateVotePercentage: .3f}% ({votes})")
print("-----------------------")
print(f"Winner: {electionWinner}")


#Set output of text file
electionResults = "electionResults.txt"

#Exporting to a text file
with open(electionResults, "w") as file:
    file.write("Election Results\n")
    file.write("-----------------------\n")
    file.write("Total Votes: %d\n" % totalVotes)
    file.write("-----------------------\n")
    file.write(f"{candidate}, {candidateVotePercentage}, {votes}\n")
    file.write("-----------------------\n")
    file.write("Winner: %s\n" % electionWinner)