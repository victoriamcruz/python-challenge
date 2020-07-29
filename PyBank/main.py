#pybank

import os

# current_working_directory = os.getcwd()
# print(current_working_directory)

# Module for reading CSV files
import csv


##setting variables
Total_Count = 0
Total_Months = []

Net = 0
Total_Net = []

Monthly_Change = []
Date = []

Greatest_Increase = 0
Greatest_Increase_Month = 0
Greatest_Decrease = 0
Greatest_Decrease_Month = 0


#define file path to open
csvpath = os.path.join("..", "PyBank", "Resource", "PyBank.csv")

#CSV reader specifies delimiter and variable that holds contents
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)
    # print(f"CSV Header: {csv_header}")
    row = next(csv_reader)
    # print(row)
    
    ##pulling data from row 1 
    previous_row = int(row[1])
    Total_Count += 1
    Net += int(row[1])

    for row in csv_reader:
        #counters for months
        Total_Count += 1

        #counter for net amount pulling in data in numbers from the row 1
        Net += int(row[1])

        ##list of dates bringing in the data from row 1
        Date.append(row[0])
        Net_Change = int(row[1]) - previous_row

        ##data from Net_change "row 1" being added to Monthly Change list 
        Monthly_Change.append(Net_Change)  
        previous_row = int(row[1])

        ##Data from row 0 being added to Total Months List
        Total_Months.append(row[0])

        ##math for increase
        if int(row[1]) > Greatest_Increase: 
            Greatest_Increase = int(row[1])
            Greatest_Increase_Month = row[0]

        ##math for decrease
        if int(row[1]) < Greatest_Decrease:
            Greatest_Decrease = int(row[1])
            Greatest_Decrease_Month = row[0]


        ##defining max and min 
        Max = max(Monthly_Change)
        Min = min(Monthly_Change)

        ##math for avg
        Average = round(sum(Monthly_Change)/ len(Monthly_Change), 2)

print("Financial Analysis")
print("----------------------------------------------------------")
print(f"Total_Months: {Total_Count}")
print(f"Total_Net: ${Net}")
print(f"Average_Change: {Average}") 
print(f"Greatest_Increase: {Greatest_Increase_Month}, ${Max}")
print(f"Greatest_Decrease: {Greatest_Decrease_Month}, ${Min}")

output_file = os.path.join("..", "PyBank", "Analysis", "PyBank.text")

with open(output_file, 'w') as txtfile:

    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------------------------------------\n")
    txtfile.write(f"Total_Months: {Total_Count}\n")
    txtfile.write(f"Total_Net: ${Net}\n")
    txtfile.write(f"Average_Change: {Average}\n") 
    txtfile.write(f"Greatest_Increase: {Greatest_Increase_Month}, (${Max})\n")
    txtfile.write(f"Greatest_Decrease: {Greatest_Decrease_Month}, (${Min})\n")