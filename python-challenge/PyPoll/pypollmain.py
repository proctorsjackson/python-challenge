#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:05:18 2023

@author: jacksonproctor
"""

#import modules
import pandas as pd
from pathlib import Path

#set path
election_csv = Path("Resources/election_data.csv")

#set csv as df
election_df = pd.read_csv(election_csv)

#find total votes (entries)
Total_Votes = len(election_df)

#find all the unique entries in the "Candidate" column / identify candidates in the election
candidates = election_df["Candidate"].unique()

#find the count of votes recieved separated by candidates
votes = election_df["Candidate"].value_counts()

#make votes by candidate a dataframe
votes_df = pd.DataFrame(votes)

#find percentage of votes recieved by each candidate
percentage = (votes / Total_Votes) * 100

#turn percentage info into dataframe
percentage_df = pd.DataFrame(percentage)

#merge count of votes recieved and percentage of votes recieved into one dataset
merged_df = pd.merge(percentage_df, votes_df, on='Candidate')

#rename merged columns
merged_df = merged_df.rename(
    columns={"count_x": "Percentage", "count_y": "Total Votes"})

#identify highest vote getter and thus election winner
winner = votes.idxmax()

#Print analysis to terminal
print("Election Analysis")
print("------------------")
print(f"Total Votes: {Total_Votes}")
print("------------------")
print(merged_df.head(3))
print("------------------")
print(f"Winner: {winner}")
print("------------------")

#print analysis to text file (had to use another method becuase I couldn't figure out how to save a df as text file)
with open("election_analysis.txt", "w") as text_file:
    text_file.write("Election Analysis\n")
    text_file.write("--------------------\n")
    text_file.write(f"Total Votes: {Total_Votes}\n")
    
    for candidate in candidates:
        text_file.write(f"{candidate}: {percentage[candidate]:.3f}% ({votes[candidate]})\n")
        
    text_file.write("--------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("--------------------\n")
    
text_file.close()   