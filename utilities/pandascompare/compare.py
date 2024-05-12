import pandas as pd

# Load the two CSV files into pandas DataFrames
df1 = pd.read_csv('/Users/deepakdas/InterviewKickStart/InterviewKickStart-1/utilities/pandascompare/file1.csv')
df2 = pd.read_csv('/Users/deepakdas/InterviewKickStart/InterviewKickStart-1/utilities/pandascompare/file2.csv')

# Find the differences between the two DataFrames
diff_df = df1.compare(df2)

# Write the differences to a new CSV file
diff_df.to_csv('differences.csv', index=False)

print("Differences have been written to differences.csv file.")
