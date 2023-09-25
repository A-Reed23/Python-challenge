import os
import csv
pypol = os.path.join('./Resources/election_data.csv')
with open(pypol) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


# Read the header row first 
    csv_header = next(csvreader)

#vairable defintion section
#stores candidate name that is in the current row
    Cand = []
#stores a list of candidates, added to when a new candidate is found in the CSV
    CandOpt=[]
#dictionary that will contain the candidates, and how many votes they got
    resul ={}
#counts total number of ballots
    BallTot = 0
    VotTot = 0
    # Read each row of data after the header
    for row in csvreader:
#candidate name in active cell
       Cand = row[2]
#If candidate is new, this will add them to the list, 
#and add name and 0 votes to the dictionary
       if Cand not in CandOpt:
           CandOpt.append(Cand)     
           resul[Cand]=0
#this will add the new vote to the candidates total
       resul[Cand]+=1
#this will increase total vote count
       BallTot+=1
       VotTot+=1

#sort the dictionnary holding the candidates and their vote counts
sortCans = sorted(resul.items(), key=lambda x:x[1], reverse=True)
converted_dict = dict(sortCans)
#Ballots in order of most to least


#Heading
print("               Election Results")
print("__________________________________________________________")
print("")
#prints out total ballots
print("Total ballots cast: " +str(VotTot))
#Printout formating
print("----------------------------------------------------------")
print("                 Results")
#vote percentages for each candidate in order of number of votes
for Cand in converted_dict:
#candidate totals
    tot = (f'{resul[Cand]}')
#takes candidate total, devides by total votes, converts to percent
    perc= (int((f'{resul[Cand]}'))/VotTot)*100
#print statment with percentage rounded. then turned into a string, as python likes
    print(Cand + ": " +str(round(float(perc),2))+ "% (" +tot + ")")
#Printout formating
print("------------------------------------------------------------")
print("The winner is :")
print(max(resul.items(), key=lambda x:x[1]))

