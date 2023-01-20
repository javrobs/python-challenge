#import modules for csv and os path assignment
import os
import csv

#declare variables
inputpath = os.path.join("Resources","budget_data.csv") #path to csv file for reading
outputpath = os.path.join("analysis","results.txt")     #path to txt file for writing
proffit=[]                                              #variable storing values from csv file
months=[]                                               #variable storing months from csv file
changes=[]                                              #variable storing changes from month to month

with open(inputpath, newline="") as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=",")      #create file reader
    next(csvreader)                                     #skip headers
    for row in csvreader:                               
        proffit.append(float(row[1]))                   #populate list with values while casting as floating point numbers
        months.append(row[0])                           #populate list with months

for i in range(len(proffit)):                           #skipping the first i, substract last proffit/loss from current one to see chain and store in changes list
    if i>0:
        changes.append(proffit[i]-proffit[i-1])


output=[]                                               #initialize a value to cycle through string outputs

output.append("Financial Analysis\n----------------------------")                                                   #text header
output.append(f"Total Months: {len(proffit)}")                                                                      #length of proffit list to see amount of months
output.append(f"Total: ${sum(proffit):,.2f}")                                                                       #the sum of all values in the proffit list, formatted with two decimal points.
output.append(f"Average Change: {sum(changes)/len(changes):,.2f}")                                                  #divided the sum of all changes over the amount of changes from list, formatted with two decimal points
output.append(f"Greatest Increase in Profits: {months[changes.index(max(changes))+1]} (${max(changes):,.2f})")      #look for the matching index +1 value in the months list corresponding to the maximum value in the changes list
output.append(f"Greatest Decrease in Profits: {months[changes.index(min(changes))+1]} (${min(changes):,.2f})")      #look for the matching index +1 value in the months list corresponding to the minimum value in the changes list

with open(outputpath, 'w') as textoutput:   #text should be stored in outputpath defined earlier, and overwrite any content in file results.txt every time the code is run. 
    for line in output:
        textoutput.write(f"{line}\n")                   #write a line of text and skip to the next line for every line in the output list
        print(line)                                     #print out a line of text for each line in the output list
