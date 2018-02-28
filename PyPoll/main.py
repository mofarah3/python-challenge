import os
import csv
import collections
import pprint

# List of Data Files


PyPoll_RD = ['1','2']

for file_Check in PyPoll_RD:
   election_csv = os.path.join("resources", "pypoll_raw_data", "election_data_" + file_Check + ".csv")

#test files
  #election_csv = os.path.join("resources", "Book" + file_Check + ".csv")

   # Create new CSV
   new_election_csv = os.path.join("resources", "output", "pypoll", "election_data_" + file_Check + ".csv")

   # Lists to store data
   votes = []
   candidates =[]  
   vote_counter =[]
   redundant_counts=[]
   max_votes =[]


   with open(election_csv, newline="") as csvfile:
       total_votes=0    

       csvreader= csv.reader(csvfile, delimiter=",")
       next(csvreader, None)
       for row in csvreader:
           # sum votes in csv
           votes.append(row[2])
           total_votes =len(votes)

           # find the different candidates
           if str(row[2]) not in candidates:
               candidates.append(row[2])

 
       # Loop through the full candidate list
       for candidate_index in range(len(candidates)):
           vote_counter = votes.count(candidates[candidate_index])

           print(str(candidates[candidate_index]) + ":   " + str(vote_counter/total_votes*100) + "%")


   print("Election Results")
   print(".........................")
   print("Total votes: "+ str(len(votes)))
   print(".........................")
           
 
 #  Open the output file
   with open(new_election_csv, 'w', newline="") as csvFile:
       csvWriter = csv.writer(csvFile, delimiter=',')

       # Write Headers into file
       
       csvWriter.writerow(str(candidates[candidate_index]) + ":   " + str(vote_counter/total_votes*100) + "%")
       csvWriter.writerow("Election Results")
       csvWriter.writerow("Total votes"+ str(len(votes)))
       csvWriter.writerow(".........................")
