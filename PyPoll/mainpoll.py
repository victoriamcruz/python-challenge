#this will be used for poll hw

import os
import csv

vote_count = 0
candidates_list = []
total_votes = []
candidate_votes = {}

csvpath = os.path.join( "..", "PyPoll", "Resource", "Poll Data.csv")

  
with open(csvpath) as csvfile:
  electionreader = csv.reader(csvfile, delimiter = ',')
  csv_header = next(electionreader)
  # row = next(electionreader)

  for row in electionreader:

    ##vote counter
    vote_count += 1
    candidates = (row[2])

    ##candidate work for votes
    if candidates not in candidates_list:
        candidates_list.append(candidates)
        candidate_votes[candidates] = 0
    candidate_votes[candidates] = candidate_votes[candidates] + 1
    # Total_Net += int(row[1])


##print data
print("Election Results")
print("------------------")
print(f"Total Votes: {vote_count}")
potential_candidate = candidates_list[0]
winning_votes = candidate_votes[potential_candidate]

print("------------------")

for key in candidate_votes:
    print(f" {key}, {round(100 * candidate_votes[key]/vote_count, 2)}%,  ({candidate_votes[key]})")
    if candidate_votes[key] > winning_votes:
        potential_candidate = key
        winning_votes = candidate_votes[key]
print("------------------")
print(f"Winner: {potential_candidate} with {winning_votes} votes!")    

print("------------------")

# Specify File To Write To
output_file = os.path.join("..", "PyPoll", "Analysis", "Poll_Data_remix.text")

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w') as txtfile:

# Write New Data
    txtfile.write("Election Results\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Votes: {vote_count}\n")
    txtfile.write("---------------------------\n")
    for key in candidate_votes:
      txtfile.write(f"{key}, {round(100 * candidate_votes[key]/vote_count, 2)}%,  ({candidate_votes[key]})\n")
  
    txtfile.write("--------------------------\n")

    txtfile.write(f"Winner: {potential_candidate} with {winning_votes} votes!\n")  
    
    txtfile.write("---------------------------\n")
