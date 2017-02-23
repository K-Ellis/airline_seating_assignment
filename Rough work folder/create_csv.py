import pandas as pd
df = pd.read_csv("bookings.csv", header=None)
print(df.head())
df[1] = df[1].apply(lambda x: x*2)
# df[1]*2
print(df.head())
df.to_csv("bookings_large_parties.csv", header=False, index=False)