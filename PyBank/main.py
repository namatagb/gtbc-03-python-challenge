#dependencies
import os
import csv

#define path to budget_data
csvpath = os.path.join('Resources', 'budget_data.csv')

#open the file
with open(csvpath) as budget_data:

    #variable for content, acknowledges comma
    csvreader = csv.reader(budget_data, delimiter=',')

    #test header
    csvheader = next(csvreader)
    #print(csvheader)
    
    #count months
    months = len(list(csvreader))
    #print(months)

    #calculate net total "Profit/Losses"
    numbers = s(float(row[1]) for row in csvreader)
    total = sum(numbers)
    print(total)



