import os
import csv

#set the file path

# PyPollFile = '/Users/lilycarbonara/Desktop/Python_Challenge/PyPoll/Resources_PyPoll/election_data.csv'
PyPollFile = os.path.join('..', 'PyPoll','Resources_PyPoll', 'election_data.csv')

#read the file 
with open(PyPollFile, 'r') as csvfile:
    PyPollData = csv.reader(csvfile, delimiter = ",")

#Identify headers 
    csvheader=next(PyPollData)
    # print(f"CSVHeader:{csvheader}")

#create a complete list of candidates and sum total votes 
    candidatelist = []
    shortcandidatelist = []
    totalvotecount=0


    for row in PyPollData: 
        candidatelist.append(row[2])
        totalvotecount = int(totalvotecount+1)
    totalvotes=totalvotecount
    # print('Total Votes Cast: ' + str(totalvotes))

#Create a condensed list of candidates 

    for each in candidatelist:
        if each not in shortcandidatelist: 
            shortcandidatelist.append(each)
    # print('The candidates were: ')
    # print(shortcandidatelist)


#Count the number of times each candidate name appears in the full candidates list 
#Note: I had tried a nested for loop with a conditional to do this by reading each row in the data file and couldn't get it to work
    VotesPerCandidate = []
    KhanVotes = candidatelist.count("Khan")
    VotesPerCandidate.append(KhanVotes)
    CorreyVotes= candidatelist.count("Correy")
    VotesPerCandidate.append(CorreyVotes)
    LiVotes = candidatelist.count("Li")
    VotesPerCandidate.append(LiVotes)
    OTooleyVotes = candidatelist.count("O'Tooley")
    VotesPerCandidate.append(OTooleyVotes)
    # print(VotesPerCandidate)



# Calculate the percent of votes per person 
    PercentPerCandidate = []
    KhanPercent= round(((KhanVotes/totalvotes)*100),2)
    PercentPerCandidate.append(KhanPercent)
    CorreyPercent= round(((CorreyVotes/totalvotes)*100),2)
    PercentPerCandidate.append(CorreyPercent)
    LiPercent= round(((LiVotes/totalvotes)*100),2)
    PercentPerCandidate.append(LiPercent)
    OTooleyPercent= round(((OTooleyVotes/totalvotes)*100),2)
    PercentPerCandidate.append(OTooleyPercent)
    # print(PercentPerCandidate)
    
    #zip all of my lists together to create a final summary 
    VoteSummary = zip(shortcandidatelist, VotesPerCandidate, PercentPerCandidate)
    
    #use a dictionary of the candidates and vote counts and a max function to identify the winner
    Results = dict(zip(shortcandidatelist, VotesPerCandidate))
    Winner = max(Results, key=Results.get)


#Display the summary of results in the terminal 
    print('Election Results')
    print('-----------------')
    print('Total Votes: ' + str(totalvotes))
    print('-----------------')
    print('Results per Candidate')
    print(shortcandidatelist[0] + " | " + str(VotesPerCandidate[0]) + " | " + str(PercentPerCandidate[0])+"%")
    print(shortcandidatelist[1] + " | " + str(VotesPerCandidate[1]) + " | " + str(PercentPerCandidate[1])+"%")
    print(shortcandidatelist[2] + " | " + str(VotesPerCandidate[2]) + " | " + str(PercentPerCandidate[2])+"%")
    print(shortcandidatelist[3] + " | " + str(VotesPerCandidate[3]) + " | " + str(PercentPerCandidate[3])+"%")
    print('-----------------')
    print('The winner: ' + Winner)

#Write results to a file 
outputfile = os.path.join('..', 'PyPoll', 'Analysis_PyPoll', "PyPoll_Analysis.csv")

with open(outputfile, "w", newline="") as datafile: 
        writer = csv.writer(datafile)
        writer.writerow(["Candidate", "Vote Count", "Vote Percent"])
        writer.writerows(VoteSummary)











