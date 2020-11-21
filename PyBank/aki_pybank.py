import os
import csv
# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'PyBank','Resources_PyBank', 'budget_data.csv')
# Read in the CSV file
with open(budget_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skips header
    header = next(csvreader)
    #Set num rows = 0 before the loop so it doesn't reset after each row
    Num_rows = 0
    #Set p/l = 0 before the loop starts up so it doesn't reset after each row
    Profit_loss = 0
    Average_change = []
    Month_tracker = []
    print(csvreader)
    # Loop through the data
    for row in csvreader:
# prior_pl =
# append example
# average_change = []
# a = 1
# b = 3
# average_change.append(a)
# [1]
# average_change.append(b)
# [1,3]
      if Num_rows > 0:
        Change_PL = int(row[1]) - Prior_PL
        Average_change.append(Change_PL)
        MoM = row[0]
        Month_tracker.append(MoM)
        # print(row)
        # print(row[0])
        # print("")
      Num_rows += 1
      Profit_loss += int(row[1])
      Prior_PL = int(row[1])
    print("Financial Analysis")
    print("---------------------------------")
    print("Total Months: " + str(Num_rows))
    print("Total: " + str(Profit_loss))
    Average_ans = round(sum(Average_change) / len(Average_change),2)
    print("Average Change: $" + str(Average_ans))
    #print(row[0],max(Average_change))
    index = Average_change.index(max(Average_change))
    index2 = Average_change.index(min(Average_change))
    print(f'Greatest Increase in Profits: {Month_tracker[index]} (${max(Average_change)})')
    print(f'Greatest Decrease in Profits: {Month_tracker[index2]} (${min(Average_change)})')