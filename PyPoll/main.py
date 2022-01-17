#dependencies
import collections
import os
import csv

#create path for file
csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidate = []
candidates = []
votes = collections.defaultdict(int)

#open the file
with open(csvpath, newline='', encoding='utf-8') as election_data:

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

    
        




pp_results = []
pp_results.append(f"The total votes for this election: {total_votes}")
pp_results.append(f"First place to {candidates[0]}")
pp_results.append(f"Second place to {candidates[1]}")
pp_results.append(f"Third place to {candidates[2]}")
pp_results.append(f"Fourth place to {candidates[3]}")

#export as txt and print
with open('Analysis/pp_results.txt', 'w', newline='') as f:
    for line in pp_results:
        f.write(line)
        print(line)
   