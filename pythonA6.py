import pandas as pd
import numpy as np

# Given DataFrame
df = pd.DataFrame({
    'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'],
    'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
    'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
    'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']
})

# 1. Fill missing FlightNumber values and convert to integer
df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)


# 2. Split From_To column into two separate columns
temp_df = df['From_To'].str.split('_', expand=True)
temp_df.columns = ['From', 'To']

# 3. Standardize capitalization in From and To columns
temp_df['From'] = temp_df['From'].str.capitalize()
temp_df['To'] = temp_df['To'].str.capitalize()


# 4. Drop the original From_To column from df and attach temp_df
df = df.drop('From_To', axis=1)
df = pd.concat([df, temp_df], axis=1)

# 5. Expand RecentDelays into separate columns and rename them
delays = df['RecentDelays'].apply(pd.Series)
delays.columns = ['delay_{}'.format(i+1) for i in range(delays.shape[1])]

# Replace the original RecentDelays column with delays DataFrame
df = df.drop('RecentDelays', axis=1)
df = pd.concat([df, delays], axis=1)

# Display the cleaned DataFrame
print("Cleaned DataFrame:")
print(df)
