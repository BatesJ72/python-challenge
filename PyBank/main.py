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
    
    changes_3 = []
    for i in range(1, len(data_3a)):
        last_month_3 = data_3a[i-1]
        current_month_3 = data_3a[i]
#     print(current_month)
#     print(last_month)
    
        change_3 = current_month_3 - last_month_3
        changes_3.append(change_3)
    
#     print(changes_3)
    avg_change = round(sum(changes_3)/len(changes_3),2)
#     print(avg_change)


# 4. Greatest increase in profits
with open(path, "r") as file: 
    header_4 = file.readline()
    budget_data_4 = file.readlines()
    data_4 = [row.strip().split(",") for row in budget_data_4]
    
    data_4a = []
    for e in data_4:
        data_4a.append(int(e[1]))
#     print(data_4a)
    
    changes_4 = []
    for i in range(1, len(data_4a)):
        last_month_4 = data_4a[i-1]
        current_month_4 = data_4a[i]
#     print(current_month)
#     print(last_month)
    
        change_4 = current_month_4 - last_month_4
        changes_4.append(change_4)
    
#     print(changes_4)

    greatest_incr = max(changes_4)
#     print(greatest_incr)

    index = changes_4.index(greatest_incr)
#     print(index)
    month_4 = data_4[index + 1]
    month_4a = month_4[0]
#     print(month_4a)
    

# 5. Greatest decrease in profits
with open(path, "r") as file: 
    header_5 = file.readline()
    budget_data_5 = file.readlines()
    data_5 = [row.strip().split(",") for row in budget_data_5]
    
    data_5a = []
    for e in data_5:
        data_5a.append(int(e[1]))
#     print(data_4a)
    
    changes_5 = []
    for i in range(1, len(data_5a)):
        last_month_5 = data_5a[i-1]
        current_month_5 = data_5a[i]
#     print(current_month)
#     print(last_month)
    
        change_5 = current_month_5 - last_month_5
        changes_5.append(change_5)
    
#     print(changes_5)

    greatest_decr = min(changes_5)
#     print(greatest_decr)

    index = changes_5.index(greatest_decr)
#     print(index)
    month_5 = data_5[index + 1]
    month_5a = month_5[0]
#     print(month_5a)
    
    


# Summary statements
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {month_4a} (${greatest_incr})")
print(f"Greatest Decrease in Profits: {month_5a} (${greatest_decr})")


# Write file
SUMMARY_FILE = os.path.join("Analysis", "summary_file.txt")

with open (SUMMARY_FILE, "w+") as file: 
    file.write("Financial Analysis\n")
    file.write("-----------------------------------\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total: ${total}\n")
    file.write(f"Average Change: ${avg_change}\n")
    file.write(f"Greatest Increase in Profits: {month_4a} (${greatest_incr})\n")
    file.write(f"Greatest Decrease in Profits: {month_5a} (${greatest_decr})\n")
    