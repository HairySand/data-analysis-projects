import pandas as pd  # Make sure pandas is imported
import numpy as np
import matplotlib as plot

# Step 1: Define the data in a dictionary
data = {
    'Seller': ['Orchid Jewels', 'Ducky Ducks', 'Candy Yarns', 'Parks Pins', 'Sierra\'s Stationary', 'Star Stitchery'],
    'Sales': [17896, 5478, 89974, 6897, 112988, 53483],
    'Total_Rating': [4.5, 3.8, 4.8, 4.9, 6.7, 4.2],
    'Current_Items': [22, 10, 18, 87, 347, 52]
}

# Step 2: Create the DataFrame
etsy_sellers = pd.DataFrame(data)

# Step 3: Now you can print the DataFrame
print(etsy_sellers)

# outlier = np.where((etsy_sellers['Total_Rating'] < 0.0) | (etsy_sellers['Total_Rating'] > 5.0))
# etsy_sellers.drop(etsy_sellers.index[outlier], inplace=True)


# print(etsy_sellers)

etsy_sellers.plot.hist(column="Total_Rating")