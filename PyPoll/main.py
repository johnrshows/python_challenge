#dependencies

import os
import csv

#path

csvpath = os.path.join('/Users/johnshows/Desktop/class/python_challenge/PyPoll/Resources/election_data.csv')
with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #print(csvreader)
    csv_header=next(csvreader)

    #variables

    votes = []
    county = []
    candidates =[]
    khan = []
    khan_votes = 0
    correy = []
    correy_votes = 0
    li = []
    li_votes = 0
    otooley = []
    otooley_votes = 0
    #csvfile.seek[0]

        

        #individual votes

    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])
        if row[2] == 'Khan':
            khan.append(row[2])
            khan_votes = len(khan)
            
        elif row[2] == 'Correy':
            correy.append(row[2])
            correy_votes = len(correy)
            
        elif row[2] == 'Li':
            li.append(row[2])
            li_votes = len(li)
            
        else:
            otooley.append(row[2])
            otooley_votes = len(otooley)
            
        

print(khan_votes)
print(correy_votes)
print(li_votes)
print(otooley_votes)

total_votes = (len(votes))
print(total_votes)

    # % of vote won per candidate

khan_percentage = round(((khan_votes / total_votes)*100),2)
correy_percentage = round(((correy_votes / total_votes)*100),2)
li_percentage = round(((li_votes / total_votes)*100),2)
otooley_percentage = round(((otooley_votes / total_votes)*100),2)
print(khan_percentage)
print(correy_percentage)
print(li_percentage)
print(otooley_percentage)

    #calculate winner
    
if khan_percentage > max(correy_percentage, li_percentage, otooley_percentage):
    winner = 'khan'
elif correy_percentage > max(khan_percentage, li_percentage, otooley_percentage):
    winner = 'correy'  
elif li_percentage > max(correy_percentage, khan_percentage, otooley_percentage):
    winner = 'li'
else:
    winner = 'otooley'

output_path = os.path.join('/Users/johnshows/Desktop/class/python_challenge/PyPoll/Analysis', 'analysis.txt')

with open(output_path,'w') as txtfile:

    txtfile.write(f'Election Results' + '\n')
    txtfile.write(f'-----------------------------------' + '\n')
    txtfile.write(f'Total Votes: {total_votes}'+ '\n')
    txtfile.write(f'-----------------------------------' + '\n')
    txtfile.write(f'khan: {khan_percentage}% ({khan_votes})' + '\n')
    txtfile.write(f'correy: {correy_percentage}% ({correy_votes})' + '\n')
    txtfile.write(f'li: {li_percentage}% ({li_votes})' + '\n')
    txtfile.write(f'otooley: {otooley_percentage}% ({otooley_votes})' + '\n')
    txtfile.write(f'-----------------------------------' + '\n')
    txtfile.write(f'Winner: {winner}' + '\n')
    txtfile.write(f'-----------------------------------')