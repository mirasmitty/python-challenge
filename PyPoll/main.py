import os
import csv

# Path to the CSV file
csv_path = os.path.join("Resources", "election_data.csv")

# Output file path
output_path = os.path.join("analysis", "election_results.txt")

# Variables
total_votes = 0
candidates = {}

# Read the CSV file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    header = next(csvreader)

    # Loop through rows
    for row in csvreader:
        # Extract data
        voter_id = row[0]
        candidate = row[2]

        # Update total votes
        total_votes += 1

        # Update candidate votes
        if candidate in candidates:
            candidates[candidate]["votes"] += 1
        else:
            candidates[candidate] = {"votes": 1}

# Text file
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")

    # Calculate and print the results for each candidate
    for candidate, info in candidates.items():
        votes = info["votes"]
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    # Find the winner
    winner = max(candidates, key=lambda x: candidates[x]["votes"])
    winner_votes = candidates[winner]["votes"]

    # Print the winner
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------")

# Print to the terminal
print("-------------------------")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Print the results for each candidate
for candidate, info in candidates.items():
    votes = info["votes"]
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

# Print the winner
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
