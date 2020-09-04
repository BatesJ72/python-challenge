import os

path = os.path.join("Resources", "election_data.csv")

# Organize the data
with open(path, "r") as file: 
    header = file.readline()
    voting_data = file.readlines()
    data_a = [row.strip().split(",") for row in voting_data] 

    data = []
    for e in data_a:
        data.append(e[2])


# 1. Total number of votes
count_1 = len(data)


# 2. A distinct list of candidates        
candidates = []
for c in data:
    if not c in candidates:
        candidates.append(c)
    
    
# 3. Percentage won by candidate
votes_khan = data.count("Khan")
votes_correy = data.count("Correy")
votes_li = data.count("Li")
votes_otooley = data.count("O'Tooley")


# 4. Get proportions
percentage_khan = '{:.3f}'.format(round(100*(votes_khan/count_1),3))
percentage_correy = '{:.3f}'.format(round(100*(votes_correy/count_1),3))
percentage_li = '{:.3f}'.format(round(100*(votes_li/count_1),3))
percentage_otooley = '{:.3f}'.format(round(100*(votes_otooley/count_1),3))


# 5. Find Winner
winner = ""

if votes_khan > votes_correy and votes_khan > votes_li and votes_khan > votes_otooley:
    winner = "Khan"
elif votes_correy > votes_khan and votes_correy > votes_li and votes_correy > votes_otooley:
    winner = "Correy"
elif votes_li > votes_khan and votes_li > votes_correy and votes_li > votes_otooley:
    winner = "Li"
else:
    winner = "O'Tooley"


# Summary Statements
print("Election Results")
print("--------------------------")
print(f"Total Votes: {count_1}")
print("--------------------------")
print(f"Kahn: {percentage_khan}% ({votes_khan})")
print(f"Correy: {percentage_correy}% ({votes_correy})")
print(f"Li: {percentage_li}% ({votes_li})")
print(f"O'Tooley: {percentage_otooley}% ({votes_otooley})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")


# Write file
SUMMARY_FILE = os.path.join("Analysis", "summary_file.txt")

with open(SUMMARY_FILE, "w+") as file: 
    file.write("Election Results\n")
    file.write("--------------------------\n")
    file.write(f"Total Votes: {count_1}\n")
    file.write("--------------------------\n")
    file.write(f"Kahn: {percentage_khan}% ({votes_khan})\n")
    file.write(f"Correy: {percentage_correy}% ({votes_correy})\n")
    file.write(f"Li: {percentage_li}% ({votes_li})\n")
    file.write(f"O'Tooley: {percentage_otooley}% ({votes_otooley})\n")
    file.write("--------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("--------------------------\n")