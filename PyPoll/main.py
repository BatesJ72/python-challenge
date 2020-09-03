import os

path = os.path.join("Resources", "election_data.csv")


with open(path, "r") as file: 
    header = file.readline()
    voting_data = file.readlines()
    data_a = [row.strip().split(",") for row in voting_data] 

    data = []
    for e in data_a:
        data.append(e[2])
        
# print(data)   

# 1. Total number of votes
count_1 = len(data)
#     print(count_1)


# 2. A distinct list of candidates        
candidates = []
for c in data:
    if not c in candidates:
        candidates.append(c)
# print(candidates)
    
    
# 3. Percentage won by candidate
votes_khan = data.count("Khan")
votes_correy = data.count("Correy")
votes_li = data.count("Li")
votes_otooley = data.count("O'Tooley")

# print(votes_kahn)
# print(votes_correy)
# print(votes_li)
# print(votes_otooley)

# 4. Get proportions
percentage_khan = '{:.3f}'.format(round(100*(votes_khan/count_1),3))
# print(percentage_khan)
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

# print(winner)


# Summary 
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