#import modules for csv and os path assignment
import os
import csv

#declare variables
inputpath=os.path.join("Resources","election_data.csv")                             #path to csv file for reading
outputpath=os.path.join("analysis","results.txt")                                   #path to txt file for writing                                                                      
candidates=[]                                                                       #initialize a list to store candidates found in csv
votes=[]                                                                            #initialize a list to store votes for each candidate

with open(inputpath,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")                                     #create file reader
    next(csvreader)                                                                 #skip headers
    
    for row in csvreader:                                                           #read through file row by row
        if row[2] not in candidates:                                                #if candidate not in candidate list, then:
            candidates.append(row[2])                                                   #add candidate
            votes.append(0)                                                             #create a corresponding votes value
        for i,candidate in enumerate(candidates):                                   #holding a single row, go through candidate list:
            if row[2]==candidate:                                                       #if candidate in csv row is found in candidates list, then:
                votes[i]+=1                                                                 #add 1 vote to the corresponding value in the vote list

outputs=[]                                                                          #initialize a value to cycle through string outputs
outputs.append(f"Election Results\n-------------------------")                      #text header
outputs.append(f"Total votes: {sum(votes)}\n-------------------------")             #total votes is the sum of all values in the votes list
for i,candidate in enumerate(candidates):                                           #for each candidate in the candidates list (3):
    outputs.append(f"{candidate}: {votes[i]/sum(votes)*100:.3f}% ({votes[i]})")         #add one line that says the name, the percentage of votes i/total with centecimals and the votes in parentheses
outputs.append(f"-------------------------\nWinner: {candidates[votes.index(max(votes))]}\n-------------------------")      #calculate winner by finding the index from highest value in votes, and retrieving the candidate with the same index

with open(outputpath,'w',newline="") as textoutput:                                 #text should be stored in outputpath defined earlier, and overwrite any content in file results.txt every time the code is run. 
    [textoutput.write(f"{line}\n") for line in outputs]                             #write a line of text and skip to the next line for every line in the output list
    [print(line) for line in outputs]                                               #print out a line of text for each line in the output list
