import os
import csv

inputpath=os.path.join("Resources","election_data.csv")
outputpath=os.path.join("analysis","results.txt")
total_votes=0
candidates=["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]
votes=[0] * len(candidates)

with open(inputpath,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    next(csvreader)
    for row in csvreader:
        total_votes += 1
        for i,candidate in enumerate(candidates):
            if row[2]==candidate:
                votes[i]+=1



outputs=[]
outputs.append(f"Election Results\n-------------------------")
outputs.append(f"Total votes: {total_votes}\n-------------------------")
for i,candidate in enumerate(candidates):
    outputs.append(f"{candidate}: {votes[i]/total_votes*100:.3f}% ({votes[i]})")
outputs.append(f"-------------------------\nWinner: {candidates[votes.index(max(votes))]}\n-------------------------")


with open(outputpath,'w',newline="") as textoutput:
    [textoutput.write(f"{line}\n") for line in outputs]
    [print(line) for line in outputs]
