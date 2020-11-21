import os
import csv

# PyBankFile = '/Users/lilycarbonara/Desktop/Python_Challenge/PyBank/Resources_PyBank/budget_data.csv'

#set the file path 
PyBankFile = os.path.join('..', 'PyBank','Resources_PyBank', 'budget_data.csv')

#open and read the csv file 
with open(PyBankFile, 'r') as csvfile:
    PyBankData = csv.reader(csvfile, delimiter = ",")

#Identify column headers 
    csvheader=next(PyBankData)  

#Set Counter Variables to increment for each row read
    monthcount = 0
    plsum = 0

#create list to capture change calcluation 
    avgchange = []
    monthlist = []

#sum / tally up the months and total PL 
    for row in PyBankData: 
        if monthcount >0 : 
            change_v = int(row[1])-prior 
            avgchange.append(change_v)
            month = row[0]
            monthlist.append(month)
        monthcount = int(monthcount+1)
        plsum += int(row[1])
        prior = int(row[1])
        

#Capture the final counts for each variable
        totalmonths=str(monthcount)
        pltotal = str(plsum)
           
#create a dictionary of months and changes 
changedictionary = dict(zip(monthlist, avgchange))
# print(changedictionary)

#display the summary in the terminal 
print("Financial Analysis")
print("")
print("Total Months: " + totalmonths)
print("Total Amount: " + pltotal)
# print(avgchange)
AverageChange = round(sum(avgchange) / len(avgchange), 2)
print("Average Monthly Change: " + str(AverageChange))
MaxChange=max(changedictionary, key=changedictionary.get)
print('Greatest Increase: ' + MaxChange + ', ' + str(max(avgchange)))
MinChange=min(changedictionary, key=changedictionary.get)
print('Greatest Decrease: ' + MinChange + ', ' + str(min(avgchange)))


#create a list of summary details 
summarydetail = [] 
summarydetail.append(int(totalmonths))
summarydetail.append(int(pltotal))
summarydetail.append(MaxChange)
summarydetail.append(max(avgchange))
summarydetail.append(MinChange)
summarydetail.append(min(avgchange))
# print(summarydetail)


#Write to a file 
outputfile = os.path.join('..', 'PyBank', 'Analysis_PyBank', "PyBank_Analysis.csv")

with open(outputfile, "w", newline="") as datafile: 
        writer = csv.writer(datafile)
        writer.writerow(["Total Months", "Total Amount",
         "Month of Greatest Increase", "Amount of Greatest Increase", 
         "Month of Greatest Decrease", "Amount of Greatest Decrease"])
        writer.writerow(summarydetail)

