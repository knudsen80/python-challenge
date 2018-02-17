# main.py for PyPoll

import csv
import os

#Need to update csv file name below, which I don't consider a "major re-write".
election_data_csv = 'election_data_2.csv'

election_data_txt = election_data_csv.replace('csv','txt')
election_results = os.path.join('results_'+ election_data_txt)

total_votes = 0
cand_list = []
num_votes = {}
perc_votes = {}
max_votes = 0
winner = ""

with open(election_data_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip headers
    next(csvreader)

    for row in csvreader:
        total_votes += 1
        cand = row[2]
        if cand not in cand_list:
            cand_list.append(cand)
            num_votes[cand] = 1
        else:
            num_votes[cand] += 1
    
    for cand, votes in num_votes.items():
        perc_votes[cand] = votes/total_votes
        if votes>max_votes:
            max_votes = votes
            winner = cand

# Print results to terminal
print("Election results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for cand, votes in num_votes.items():
    print(cand + ": " + str("{:.1f}".format(100*perc_votes[cand])) + "% (" + str(votes) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

# Print ressults to text file
with open(election_results, 'w', newline="") as text:
    
    # I googled how to print strings to text. Showed most recent way to do it is with {}.
    # But this didn't work for my percentage line, so I used %s and %, which I had learned in codecademy
    
    text.write("Election results" + "\n")
    text.write("-------------------------" + "\n")
    text.write("Total Votes: %s" % total_votes + "\n")
    text.write("-------------------------" + "\n")
    for cand, votes in num_votes.items():
        perc = "{:.1f}".format(100*perc_votes[cand])
        text.write("%s" % cand + ": %s" % perc + "% (" + "%s" % votes + ")" + "\n")
    text.write("-------------------------" + "\n")
    text.write("Winner: " + winner + "\n")
    text.write("-------------------------" + "\n")