import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('bmh')
df = pd.read_csv(r"C:\Users\mauro\Desktop\Renata\Project Python\Projects_done\SuperStore_dataset\SampleSuperstore.csv",
                 index_col=[0])
print(df.head())

# Shape, type and verify if it has value null
print('Shape = {}'.format(df.shape))
print('Data Type of each column\n{}'.format(df.dtypes))
print(df.isnull().sum())

df = df.reset_index()
# Verify the Country column if there's an unique value and skip it if not
print(df['Country'].nunique())
df = df.drop(['Ship Mode', 'Country', 'Postal Code', 'Region'], axis=1)
print(df.head())

# Some statistics
print(df.describe())
print(df['Profit'].describe())

# Format the float numbers displayed on the tables
pd.options.display.float_format = '{:20,.2f}'.format

# Total profit
total_profit = df['Profit'].sum()
print('Total profit = ${:0,.2f}'.format(total_profit))

# Create a Cost column and total cost
df['Cost'] = df['Sales'] - df['Profit']
total_cost = (df['Cost'].sum())
print('Total cost = ${:0,.2f}'.format(total_cost))

# Profit in percentage
print('Profit(%) = {:0,.2f}%'.format(total_profit / total_cost * 100))

# Which segment gives less profit and more costs
less_profit_segment = df.groupby('Segment')['Profit'].min().plot.bar(title='Least Profitable Segment',
                                                                   fontsize=9)  # Consumers - Corporate -Home
plt.ylabel('Profit ($)')
plt.xticks(rotation='horizontal')
plt.show()
costly_segment = df.groupby('Segment')['Cost'].max().sort_values(ascending=False).plot.bar(title='Costly Segment',
                                                                                          fontsize=9)  # Home Office - Corporate - Consumer
plt.ylabel('Cost ($)')
plt.xticks(rotation='horizontal')
plt.show()
# Proporcional relation, Cost more, more profit, Cost less, less profit

# TOP 3 states that result less profit and more costs
print(df.groupby('State')['Profit'].sum().nsmallest(3))
print(df.groupby('State')['Cost'].sum().nlargest(3))
# Texas has the least profit and the third most costly

# Exploring more the states with less profit and more costs
print(df.groupby(['State', 'City'])['Profit'].sum().nsmallest(3))
print(df.groupby(['State', 'City'])['Cost'].sum().nlargest(3))
# From the cities, Philadelphia (Pennsylvania state) has the least profit and the third most costly

# Graph of profit by category
# print(df.groupby(['Category', 'Sub-Category'])['Profit'].sum())
df.groupby(['Category'])['Profit'].sum().sort_values(ascending=False).plot.pie(title='Profitable category',
                                                                               autopct="%.2f%%", fontsize=9,
                                                                               figsize=(5, 5))
plt.show()
print(df.groupby(['Category'])['Profit'].sum())

# Graph of costs by category
df.groupby(['Category'])['Cost'].sum().sort_values(ascending=False).plot.pie(title='Costly category', autopct="%.2f%%",
                                                                             fontsize=9, figsize=(5, 5))
plt.show()
print(df.groupby(['Category'])['Cost'].sum())
# Costs are well distributed by category

# Graph of quantity sold by category
df.groupby('Category')['Quantity'].sum().sort_values(ascending=False).plot.pie(
    title='Quantity of products sold by category', autopct="%.2f%%", fontsize=9, figsize=(5, 5))
plt.show()
# Technology is more profitable, selling less quantities. Inversely proportional, less quantity for more profit and more quantity for less profit

# Checking which state had highest and lowest discount
print(df.groupby('State')['Discount'].max().nlargest(3))
print(df.groupby('State')['Discount'].min().nsmallest(3))

print(df.groupby(['State', 'City'])['Discount'].max().nsmallest(3))
print(df.groupby(['State', 'City'])['Discount'].min().nlargest(3))
# Discount given doesnt seems to be related to the low profit

# Checking if the total sales has relation to the low profit
# print(df.groupby('State')['Sales'].sum().nlargest(3))
# print(df.groupby('State')['Sales'].sum().nsmallest(3))

df.groupby('State')['Sales'].sum().nlargest(3).sort_values(ascending=False).plot.bar(title='Top 3 States of Sales ',
                                                                                     fontsize=8, figsize=(5, 5))
plt.xlabel('States')
plt.ylabel('Sales ($)')
plt.xticks(rotation='horizontal')
plt.show()

df.groupby('State')['Sales'].sum().nsmallest(3).sort_values(ascending=True).plot.bar(title='Last 3 States of Sales ',
                                                                                     fontsize=8, figsize=(5, 5))
plt.xlabel('States')
plt.ylabel('Sales ($)')
plt.xticks(rotation='horizontal')
plt.show()
# Texas has the least profit, but it's the third of the sales

# Save analysis as csv
df.to_csv('df_super_store_analysis.csv', index=False)
