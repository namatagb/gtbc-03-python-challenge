#dependencies
import os
import csv

#create path for file
csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidates = []
vote_count = 0
khan_votes = 0

#open the file
with open(csvpath, newline='') as election_data:

    #read the file
    csvreader = csv.reader(election_data, delimiter=',')
    
    #skip header
    csvheader = next(csvreader)
    
    #loop
    for row in csvreader:

        #calculate total votes
        total_votes += 1

        #find candidates
        if row[2] not in candidates:
            candidates.append(row[2])
        
        #count votes per candidate
        khan_votes = row[2].count('Khan')
        
        





print(total_votes)
print(candidates)
print(khan_votes) 
   