# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 03:33:04 2024

@author: IAN CARTER KULANI
"""
# -*- coding: utf-8 -*-
#This software prompts the user to enter total number of published centers,total number of registered votes, total number of null and void votes, total number of valid votes and total valid votes for each candidate. Afterward, it determines the candidate with the majority of votes and displays the results on the screen.
#NOTE:For a candidate to be a majority winner the candidate total valid votes should be greater than majority votes.

print("Dyna-stat software [version 1]\n(c) Dyna-stat software.All rights Reserved.")

print("====================================RUSSIA 2024 ELECTION====================================\n") 

Totalpublishedcenters=int(input("Enter Total published centers:"))
#Get the total number of registered votes
TotalRegisteredvotes=int(input("Enter Total Registered Voters/Turnout:"))
#Get Total number of votes cast
Totalvotescast=int(input("Enter Total Votes Cast/Total Votes:"))
#Get total number of Null_&_Void votes
Nullandvoid=int(input("Enter Total Null_&_Void Votes/Invalid Votes:"))
#Get Total Valid Votes for All candidates
Totalvalidvotes=int(input("Enter Total Valid Votes:"))
#Get total valid votes for Vladimir Putin
Totalvalidvotesfor_Vladimir_Putin=int(input("Enter Total Valid Votes for Vladimir Putin:"))
#Get total valid votes for Nikolay Khritinov
Totalvalidvotesfor_Nikolay_Khritinov=int(input("Enter Total Valid Votes for Nikolay Khritinov:"))
#Get total valid votes for Leonid Slutsky
Totalvalidvotesfor_Vladislav_Davankov=int(input("Enter Total Valid Votes for Vladislav Davankov:"))
#Get total valid votes for Leonid Slutsky
Totalvalidvotesfor_Leonid_Slutsky=int(input("Enter Total Valid Votes for Leonid Slutsky:"))
percent=100


if Totalvalidvotesfor_Vladimir_Putin>Totalvalidvotes/2+1:
   print("Cogratulations Vladimir Putin  you're the winner of 2024 election\n\n")
 
elif Totalvalidvotesfor_Nikolay_Khritinov>Totalvalidvotes/2+1:
     print("Cogratulations Nikolay Khritinov  you're the winner of 2024 election\n\n")
   
elif Totalvalidvotesfor_Vladislav_Davankov>Totalvalidvotes/2+1:
     print("Cogratulations Vladislav_Davankov  you're the winner of 2024 elections")
    
elif Totalvalidvotesfor_Leonid_Slutsky>Totalvalidvotes/2+1:
     print("Cogratulations Leonid_Slutsky  you're the winner of 2024 election\n\n")

else:
    print("No majority winner was found RUN OFF May be required\n\n")     

print("_________________________________ELECTION STATISTICS_____________________________________\n") 

#Calculating Percentage    
Percentage=round(Totalvalidvotes*percent/Totalvalidvotes, 2);
print("Total Votes Cast in percentage=",Percentage)
Percentage=round(Totalvalidvotes*percent/Totalvotescast, 2);
print("Total Valid Votes for all candidtes in percentage=",Percentage)
#Calculating percentage for null_&_void votes
Percentage=round(Nullandvoid*percent/Totalvalidvotes, 2);
print("Total Null_&_Void votes in percentage=",Percentage)
#
Percentage=round(Totalvalidvotesfor_Vladimir_Putin*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Vladimir Putin in percentage=",Percentage )
Percentage=round(Totalvalidvotesfor_Nikolay_Khritinov*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Nikolay Khritinov in percentage=",Percentage )
Percentage=round(Totalvalidvotesfor_Vladislav_Davankov*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Vladislav Davankov in percentage=",Percentage )
Percentage=round(Totalvalidvotesfor_Leonid_Slutsky*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Leonid Slutsky in percentage=",Percentage )
print("==========================================================================================\n") 
