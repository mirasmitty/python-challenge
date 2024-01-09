import os
import csv

# Path to the CSV file
csv_path = os.path.join("Resources", "budget_data.csv")

# Output file path
output_path = os.path.join("analysis", "financial_analysis.txt")

# Variables
total_months = 0
net_total = 0
prev_profit_loss = 0
changes = []
dates = []

# Read the CSV file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    header = next(csvreader)

    # Loop through rows
    for row in csvreader:
        # Extract data
        date = row[0]
        profit_loss = int(row[1])

        # Calculate changes
        if total_months != 0:
            change = profit_loss - prev_profit_loss
            changes.append(change)
            dates.append(date)

        # Update variables
        prev_profit_loss = profit_loss
        total_months += 1
        net_total += profit_loss

# Calculate average change
average_change = sum(changes) / len(changes)

# Find the greatest changes
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Print to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Write to text file
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

