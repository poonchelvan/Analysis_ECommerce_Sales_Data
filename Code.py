# =====================================
# 1. Import Required Libraries
# =====================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)
# =====================================
# 2. Generate Synthetic Dataset
# =====================================

dates = pd.date_range(start='2024-01-01', periods=365, freq='D')

categories = ['Electronics', 'Clothing', 'Home Appliances']

data = pd.DataFrame({
    'Date': dates,
    'Product Category': np.random.choice(categories, size=365),
    'Units Sold': np.random.randint(1, 50, size=365),
    'Customer Rating': np.random.randint(1, 6, size=365)
})

price_per_unit = np.random.uniform(10, 200, size=365)
data['Revenue'] = data['Units Sold'] * price_per_unit

print('Sample Data:')
print(data.head())
# =====================================
# 3. Data Validation and Cleaning Check
# =====================================

print('\n--- Missing Values Check ---')
print(data[['Units Sold', 'Revenue']].isnull().sum())

print('\n--- Data Types ---')
print(data[['Units Sold', 'Revenue']].dtypes)
# =====================================
# 4. Descriptive Statistics for Revenue
# =====================================

revenue_stats = {
    'Mean': data['Revenue'].mean(),
    'Median': data['Revenue'].median(),
    'Std Dev': data['Revenue'].std(),
    'Min': data['Revenue'].min(),
    'Max': data['Revenue'].max()
}

print('\n--- Revenue Descriptive Statistics ---')
for key, value in revenue_stats.items():
    print(f"{key}: {value:.2f}")
# =====================================
# 5. Monthly Revenue Aggregation
# =====================================

data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.to_period('M')

monthly_revenue = data.groupby('Month')['Revenue'].sum()

plt.figure()
monthly_revenue.plot(kind='line')
plt.title('Total Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.show()
# =====================================
# 6. Customer Rating Frequency Distribution
# =====================================

rating_freq = data['Customer Rating'].value_counts().sort_index()

print('\n--- Customer Rating Frequency ---')
print(rating_freq)

plt.figure()
rating_freq.plot(kind='bar')
plt.title('Customer Rating Distribution')
plt.xlabel('Customer Rating')
plt.ylabel('Frequency')
plt.show()
