import pandas as pd

#Ask for name of file, should be located in same folder as amazon-orders.py
filename = input("What is the CSV file name? ")

#Open CSV and replace all NaN values with 0
try:
    df = pd.read_csv(filename)
    df = df.fillna(0)
except:
    print("\n\nUnable to locate file. Please make sure it is in the same directroy as this python script.")
    exit()

#Change values in CSV to something python can read
df["Total Charged"] = df["Total Charged"].str.replace('$', '', regex=True).astype(float)
df["Order Date"] = pd.to_datetime(df["Order Date"])


#Get sum, mean, max, and min of Total Charges in CSV file rounded to two decimal places
sum_of_total_charges = round(df["Total Charged"].sum(), 2)
mean_of_total_charges = round(df["Total Charged"].mean(), 2)
max_of_total_charges = round(df["Total Charged"].max(), 2)
min_of_total_charages = round(df["Total Charged"].min(), 2)

print("Sum of Total Charges: $", sum_of_total_charges)
print("Mean: $", mean_of_total_charges)
print("Max per single order: $", max_of_total_charges)
print("Min per single order: $", min_of_total_charages)




