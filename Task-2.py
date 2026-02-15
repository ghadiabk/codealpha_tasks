import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Datasets/Unemployment_Rate_upto_11_2020.csv')

df.columns = df.columns.str.strip()
df['Date'] = pd.to_datetime(df['Date'].str.strip(), format='%d-%m-%Y')

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)', errorbar=None)
plt.title('Impact of COVID-19: Unemployment Rate in India Over Time (2020)')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.show()

state_avg = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False).reset_index()

plt.figure(figsize=(12, 8))
sns.barplot(data=state_avg, x='Estimated Unemployment Rate (%)', y='Region', palette='viridis')
plt.title('Average Unemployment Rate by State (2020)')
plt.xlabel('Average Unemployment Rate (%)')
plt.ylabel('State / Region')
plt.show()