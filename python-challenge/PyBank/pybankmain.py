#!/usr/bin/env python3
# -*- coding: utf-8 -*-




#import modules
import pandas as pd
from pathlib import Path

#set path
budget_csv = Path("Resources/budget_data.csv")

#set csv as df
budget_df = pd.read_csv(budget_csv)
budget_df.head()

#find total months (entries) in dataset
Total_Months = len(budget_df)
Total_Months

#find the total of profits/losses
net_pl = budget_df["Profit/Losses"].sum()

#find the change in p/l and create new column
budget_df["P/L Change"] = budget_df["Profit/Losses"].diff()


#find the average change with newly created column
pl_change_average = budget_df["P/L Change"].mean()


#find greatest increase/decrease rows
greatest_increase_row = budget_df[budget_df["P/L Change"] == budget_df["P/L Change"].max()]
greatest_decrease_row = budget_df[budget_df["P/L Change"] == budget_df["P/L Change"].min()]

#find date and amount of greatest increase
greatest_increase_day = greatest_increase_row.iloc[0]["Date"]
greatest_increase_amount = greatest_increase_row.iloc[0]["P/L Change"]

#find date and amount of greatest decrease
greatest_decrease_day = greatest_decrease_row.iloc[0]["Date"]
greatest_decrease_amount = greatest_decrease_row.iloc[0]["P/L Change"]

#print analysis to terminal
print("Financial Analysis")
print("------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${net_pl}")
print(f"Average Change: ${pl_change_average}")
print(f"Greatest Increase in Profits: {greatest_increase_day}(${greatest_increase_amount:})")
print(f"Greatest Decrease in Profits: {greatest_decrease_day}(${greatest_decrease_amount:})")

#save analysis as .txt file 
with open("financial analysis", "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("----------------\n") 
    text_file.write(f"Total Months: {Total_Months}\n")
    text_file.write(f"Total: ${net_pl}\n") 
    text_file.write(f"Average Change: ${pl_change_average}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase_day} (${greatest_increase_amount:})\n") 
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_day} (${greatest_decrease_amount:})\n")