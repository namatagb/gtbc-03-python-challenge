#dependencies
import os
import csv

#define path to budget_data
csvpath = os.path.join('Resources', 'budget_data.csv')

total = 0
months = 0
minVal = ["Jan-2010",0]
maxVal = ["Jan-2010",0]
previous_month = 0
monthly_changes = []
average_change = 0

#open the file
with open(csvpath, newline='', encoding="utf8") as budget_data:

    #variable for content, acknowledges comma
    csvreader = csv.reader(budget_data, delimiter=',')

    csvheader = next(csvreader)

    #test reader
    for row in csvreader:
        #print(row)

        #count months
        months += 1

        #calculate net total "Profit/Losses"
        total += int(row[1])

        #find minimum and maximum
        if int(row[1]) < minVal[1]: 
            minVal = [row[0],int(row[1])]
        if int(row[1]) > maxVal[1]: 
            maxVal = [row[0],int(row[1])]
        
        #find net change
        if months != 1:
            change = int(row[1]) - previous_month
            monthly_changes.append(change)

        #save month value for next loop
        previous_month = int(row[1])

    #calculate average change
    average_change = sum(monthly_changes)/len(monthly_changes)


pb_results = []
pb_results.append(f"The total number of months: {months}")
pb_results.append(f"The net total profit and losses: ${total}")
pb_results.append(f"The lowest month {minVal[0]}: ${minVal[1]}")
pb_results.append(f"The highest month {maxVal[0]}: ${maxVal[1]}")
pb_results.append(f"The average monthly change: ${round(average_change,2)}")

    

    #print all results

#export as txt
with open('Analysis/pb_results.txt', 'w') as f:
    for line in pb_results:
        f.write(line)
        print(line)




