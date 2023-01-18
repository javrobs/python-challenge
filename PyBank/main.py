#import modules for csv and os path assignment
import os
import csv

#declare variables
inputpath = os.path.join("Resources","budget_data.csv")
outputpath = os.path.join("analysis","results.txt")
proffitloss=[]  #variable storing values from csv file
months=[]       #variable storing months from csv file
changes=[]      #variable storing changes from month to month

with open(inputpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        proffitloss.append(row[1])      #populate list with values
        months.append(row[0])           #populate 

for i in range(len(proffitloss)):
    proffitloss[i]=float(proffitloss[i])
    if i>0:
        changes.append(proffitloss[i]-proffitloss[i-1])


output=[]

output.append("Financial Analysis\n----------------------------")
output.append(f"Total Months: {len(proffitloss)}")
output.append(f"Total: ${sum(proffitloss):,.2f}")
output.append(f"Average Change: {sum(changes)/len(changes):,.2f}")
output.append(f"Greatest Increase in Profits: {months[changes.index(max(changes))+1]} (${max(changes):,.2f})")
output.append(f"Greatest Decrease in Profits: {months[changes.index(min(changes))+1]} (${min(changes):,.2f})")

with open(outputpath, 'w', newline="") as textoutput:
    for line in output:
        textoutput.write(f"{line}\n")
        print(line)
