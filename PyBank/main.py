import os

path = os.path.join("Resources", "budget_data.csv")

# 1. Get the total number of months in data set, excluding the header
with open(path, "r") as file: 
    header_1 = file.readline()
    budget_data_1 = file.readlines()
    data_1 = [row.strip().split(",") for row in budget_data_1]
    months = len(data_1)
# print(months)


# 2. Net total Profit/Losses
with open(path, "r") as file: 
    header_2 = file.readline()
    budget_data_2 = file.readlines()
    data_2 = [row.strip().split(",") for row in budget_data_2]
    
    total = 0
    for item in data_2:
        total += int(float(item[1]))
# print(total)
   
    
# 3. Average change    
with open(path, "r") as file: 
    header_3 = file.readline()
    budget_data_3 = file.readlines()
    data_3 = [row.strip().split(",") for row in budget_data_3]
    
    data_3a = []
    for e in data_3:
        data_3a.append(int(e[1]))
#     print(data_3a)
    
    changes = []
    for i in range(1, len(data_3a)):
        last_month = data_3a[i-1]
        current_month = data_3a[i]
#     print(current_month)
#     print(last_month)
    
        change = current_month - last_month
        changes.append(change)
    
# print(type(change))
    avg_change = round(sum(changes)/len(changes),2)
#     print(avg_change)


# 4. Greatest increase in profits


# Summary statements
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_change}")