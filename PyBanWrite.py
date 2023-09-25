import os
import csv
# import file with budget data
pybudg = os.path.join('./Resources/budget_data.csv')
with open(pybudg) as csvfile:
    tomato = csv.reader(csvfile, delimiter=',')
    
   
# Read the header row first 
    csv_header = next(tomato)

#Get dates for the time difference- date in the active cell
    Datez = []
# this is the list of the Profit/loss values
    PLData = []
#previous Profit /Loss
    PasPLVal = 0
#List of Profit loss differnces for list
    PLDiff = []

#This will count the number of rows so that I can:
    #1. do an average, 2. Work out how many months are in the data 
    roCount = 0
#Used to find Profit /Loss min/max, so I can find the days    
    PLMax = 0
    PLMin = 0
#This will go through the data and add 
    for row in tomato:   
#add value to the date list
        Datez.append(row[0])
#add value to the Profit/Loss
        PLData.append(int(row[1]))
#Increase the count of how may loops by one
        roCount+=1
# calculate difference between proffit/ loss for the month, store in list
        PLCalc= (int(row[1])-int(PasPLVal))
        PLDiff.append(int(PLCalc))
#this will find the date of the maximum value
        if PLCalc > PLMax:
            PLMaxDay = row[0]
            PLMax = PLCalc
 #this will find the date of the minimum value           
        elif PLCalc < PLMin:
            PLMinDay =row[0]
            PLMin = PLCalc
#store Profit / Loss value for the next loop        
        PasPLVal = int(row[1])
 
#create text output
with open('Py1Bank.txt', 'w') as txt:
# Write to the file        
#Print out of data, heading        
    txt.write("                Finacial Analysis   \n----------------------------------------------------------\n" )
#Spacer
    txt.write("\n Total Months: ")
#printout total months    
    txt.write(str(roCount))
#Spacer
    txt.write("\n \n Total Proffits: ")
#Total Profit /Loss
    NetProfit = sum(PLData)
    txt.write(str(NetProfit))
#Spacer
    txt.write("\n \n Average Change: $")
#Takes the differance between the Profit/loss for one month (calculated in loop)
#removes the first row as there was no change
    PLDiff.pop(0)
#and the next and then averages and prints return
    AvgPL = round(sum(PLDiff)/(roCount-1),2)
    txt.write(str(AvgPL)) 
#max and min changes
    bigest = max(PLDiff)
    small = min(PLDiff)
    txt.write("\n \n Greatest Proffit: ($")
    txt.write(str(bigest))
    txt.write(") \n \n Greatest Loss: ($")
    txt.write(str(small))
    txt.write(") ")