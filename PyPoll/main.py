import os

path = os.path.join("Resources", "election_data.csv")

# 1. Total number of votes
with open(path, "r") as file: 
    header_1 = file.readline()
    budget_data_1 = file.readlines()
    data_1 = [row.strip().split(",") for row in budget_data_1]
    
    
    data_1a = []
    for e in data_1:
        data_1a.append(e[0])
    count_1 = len(data_1a)
#     print(count_1)






# Summary 
print("Election Results")
print("--------------------------")
print(f"Total Votes: {count_1}")
print("--------------------------")