import os
import csv

path = os.path.join("Resources", "budget_data.csv")

# Get the total number of months in data set, excluding the header
#redo this as a dict_reader, then skip the header line, then count the length of the list
with open(path, "r") as file: 
    # prints data as a list
    budget_data = file.readlines()
    data = [row.strip().split(",") for row in budget_data]

    months = -1
    for n in data:
        months += 1
    print(f"Total Months: {months}")

    
    
with open(path, "r") as file: 
    # eliminate the header
    header = file.readline()
    
    # print the net total of "Profits/Losses"
    budget_data = file.readlines()
    data = [row.strip().split(",") for row in budget_data]
    total = 0
    for item in data: 
        total += int(float(item[1]))
    print(f"Total: ${total}")
        


# redo this - first create a list that contains all the differences from month to month, and then take the average of that        
with open(path, "r") as file: 
    # eliminate the header
    header = file.readline()
    
    # print the avg of changes of "Profits/Losses"
    
    budget_data = file.readlines()
    data = [row.strip().split(",") for row in budget_data]
    
    # get the sum
    total = 0
    for item in data: 
        total += int(float(item[1]))
   
    # get the number of records
    records = 0
    for item in range(len(data)): 
        records += 1
    
    # Average calc
    avg = round(total/records,2)
    print(f"Average Change: ${avg}")
        
        
        
# redo this - it needs to be the greatest increase from month to month, not the greatest month       
with open(path, "r") as file: 
    # eliminate the header
    header = file.readline()
    
    # get max "Profits/Losses"
    budget_data = file.readlines()
    data = [row.strip().split(",") for row in budget_data]
    total = 0
    month = 0
    for item in data: 
        if int(float(item[1])) > total:
            total = int(float(item[1]))
            month = item[0]
    print(f"Greatest Increase in Profits: {month} (${total})")
        
        
        
        
# redo this - it needs to be the greatest decrease from month to month, not the lowest month  
with open(path, "r") as file: 
    # eliminate the header
    header = file.readline()
    
    # get min "Profits/Losses"
    budget_data = file.readlines()
    data = [row.strip().split(",") for row in budget_data]
    total = 0
    month = ""
    for item in data: 
        if int(float(item[1])) < total:
            total = int(float(item[1]))
            month = item[0]
    print(f"Greatest Decrease in Profits: {month} (${total})")
        
#     print(type(data[:1]))
#     PL = [data[:1] for e in data]
#     print(PL)
    
    

# with open(path, "r") as file: 
#     dict_reader = csv.DictReader(file)
    
#       # prints data as a dictionary 1
# #     for row in dict_reader:
# #         print(dict(row))

#     # prints data as a dictionary 2
#     dict_data = [dict(ordered_dict) for ordered_dict in dict_reader]
# #     print(dict_data)
#     print(max("Profit/Losses"))
    
# #     print([e["Date"] for e in dict_data] in max("Profit/Losses"))
