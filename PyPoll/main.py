import os
import csv

#set the file path

PyPollFile = '/Users/lilycarbonara/Desktop/Python_Challenge/PyPoll/Resources_PyPoll/election_data.csv'

#define a function and accept datafile as sole parameter 

# def PyPollInfo(PollData): 
# #Create the list of variables 
#     candidate = str(PollData[2])
#     county =str(PollData[1])
#     voterID = str(PollData[0])

#read the file 
with open(PyPollFile, 'r') as csvfile:
    PyPollData = csv.reader(csvfile, delimiter = ",")

#Identify headers 
    csvheader=next(PyPollData)
    # print(f"CSVHeader:{csvheader}")

# # #

#create a complete list of candidates and sum total votes 
    candidatelist = []
    shortcandidatelist = []
    totalvotecount=0


    for row in PyPollData: 
        candidatelist.append(row[2])
        totalvotecount = int(totalvotecount+1)
    totalvotes=totalvotecount
    print('Total Votes Cast: ' + str(totalvotes))


    for each in candidatelist:
        if each not in shortcandidatelist: 
            shortcandidatelist.append(each)
    print('The candidates were: ')
    print(shortcandidatelist)


#Count the number of times each candidate name appears in the candidates list
    VotesPerCandidate = []
    KhanVotes = candidatelist.count("Khan")
    VotesPerCandidate.append(KhanVotes)
    CorreyVotes= candidatelist.count("Correy")
    VotesPerCandidate.append(CorreyVotes)
    LiVotes = candidatelist.count("Li")
    VotesPerCandidate.append(LiVotes)
    OTooleyVotes = candidatelist.count("O'Tooley")
    VotesPerCandidate.append(OTooleyVotes)
    print(VotesPerCandidate)



# Calculate the percent of votes per person 
    PercentPerCandidate = []
    KhanPercent= (KhanVotes/totalvotes)*100
    PercentPerCandidate.append(KhanPercent)
    CorreyPercent= (CorreyVotes/totalvotes)*100
    PercentPerCandidate.append(CorreyPercent)
    LiPercent= (LiVotes/totalvotes)*100
    PercentPerCandidate.append(LiPercent)
    OTooleyPercent= (OTooleyVotes/totalvotes)*100
    PercentPerCandidate.append(OTooleyPercent)
    print(PercentPerCandidate)
    
    VoteSummary = dict(zip(shortcandidatelist, PercentPerCandidate))
    print(VoteSummary)

    Winner = max(VoteSummary, key=VoteSummary.get)
    print('The winner was ' + Winner + ' with ' + str(max(PercentPerCandidate)) + '% of votes.')





    # votetally = []
    # votecount=0
    # votecount1=sum(1 for row in PyPollData if str(row[2]) == str(candidatelist[1]))
    

    # for row in PyPollData:
    #     candidate1 = string.count(candidatelist[0])
    # print(candidate1)



    # for each in candidatelist: 
    #     for row in PyPollData: 
    #         if each == row[2]: 
    #             votecount=votecount+1
    #         votetally.append(votecount)
    # print(votetally)
            

# # candidatetally = dict(zip(candidatelist, votetally))

#     for each in PyPollInfo:
#         if row[2] == candidatelist[0]: 
#             votecount = votecount+1
#             votetally.append(votecount)
#     print(votetally)











