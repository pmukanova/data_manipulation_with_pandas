# Import pandas using the alias pd
import pandas as pd

temperatures = pd.read_csv("/Users/perizatmenard/Documents/advanced_python/data_manipulation_with_pandas/data/temperatures.csv")

# Look at temperatures
print(temperatures.head())

# Index temperatures by city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind.head())

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop=True))