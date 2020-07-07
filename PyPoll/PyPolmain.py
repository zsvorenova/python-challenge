# import required modules
import os
import csv

# idetify the path for csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# set Candidate as list
Candidate = []

#open csv file and append candidate data to Candidate list
with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Candidate.append(row["Candidate"])

# Calculate Total Votes submitted
total_votes=len(Candidate)

# identify list of candidates a unique names and set variable for each candidate
Candidate_set=list(set(Candidate))
number_candidates=len(Candidate_set)
candidate1 = Candidate_set[0]
candidate2 = Candidate_set[1]
candidate3 = Candidate_set[2]
candidate4 = Candidate_set[3]

# calculate number of votes for each candidate separately and the percentage of total votes received
votes_candidate1 = 0
votes_candidate2 = 0
votes_candidate3 = 0
votes_candidate4 = 0

for candidate in Candidate:
    if candidate == candidate1:
        votes_candidate1 += 1
    elif candidate == candidate2:
        votes_candidate2 += 1
    elif candidate == candidate3:
        votes_candidate3 += 1
    elif candidate == candidate4:
        votes_candidate4 += 1
    
perc_can1 = "{:.3%}".format(round((votes_candidate1 / total_votes),2))
perc_can2 = "{:.3%}".format(round((votes_candidate2 / total_votes),2))
perc_can3 = "{:.3%}".format(round((votes_candidate3 / total_votes),2))
perc_can4 = "{:.3%}".format(round((votes_candidate4 / total_votes),2))

# identify who is the winner
winner_perc= max(perc_can1, perc_can2, perc_can3, perc_can4)
if winner_perc == perc_can1:
    winner_name = candidate1
elif winner_perc == perc_can2:
    winner_name = candidate2
elif winner_perc == perc_can3:
    winner_name = candidate3
else:
    winner_name = candidate4

# Generate summary of results
output = (
    f"\nElection Results\n"
    f"----------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------\n"
    f"{candidate1}: {perc_can1} ({votes_candidate1})\n"
    f"{candidate2}: {perc_can2} ({votes_candidate2})\n"
    f"{candidate3}: {perc_can3} ({votes_candidate3})\n"
    f"{candidate4}: {perc_can4} ({votes_candidate4})\n"
    f"----------------------\n"
    f"Winner: {winner_name}\n"
    f"----------------------\n")
  
# Print all of the results (to terminal)
print(output)

# Save the results to analysis text file
file_to_output = os.path.join("analysis", "PyPoll_analysis.txt")
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


