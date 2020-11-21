import os
import csv
import collections 

#set the file path

PyPollFile = '/Users/lilycarbonara/Desktop/Python_Challenge/PyPoll/Resources_PyPoll/election_data.csv'

# define a function and accept datafile as sole parameter 

# def PyPollInfo(PollData): 
# #Create the list of variables 
#     candidate = str(PollData[2])
#     county =str(PollData[1])
#     voterID = str(PollData[0])

# #read the file 
with open(PyPollFile, 'r') as csvfile:
    PyPollData = csv.reader(csvfile, delimiter = ",")

#Identify headers 
    csvheader=next(PyPollData)
    print(f"CSVHeader:{csvheader}")

# # #

#create a complete list of candidates and sum total votes 
    candidatelist = []
    totalvotecount=0
    votetally = collections.Counter()

    for row in PyPollData: 
        votetally[row[2]] += 1
        totalvotecount = int(totalvotecount+1)
    totalvotes=totalvotecount
    print(totalvotes)
    print(votetally)
    
    # result = (votetally/totalvotes)*100
    # print(result)

 

    # 
    

    

    # print(result)


    # # print(candidatelist)

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











