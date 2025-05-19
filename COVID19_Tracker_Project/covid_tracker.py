# covid_tracker.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("synthetic_covid19_data.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Filter countries of interest
countries = ['Kenya', 'USA', 'India']
df = df[df['location'].isin(countries)]

# Drop rows with critical missing values
df = df.dropna(subset=['total_cases', 'total_deaths', 'total_vaccinations'])

# Fill remaining missing values
df = df.fillna(method='ffill')

# Plot: Total Cases Over Time
plt.figure(figsize=(10,6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.tight_layout()
plt.savefig("cases_over_time.png")
plt.show()

# Plot: Total Deaths Over Time
plt.figure(figsize=(10,6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)
plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.tight_layout()
plt.savefig("deaths_over_time.png")
plt.show()

# Plot: Total Vaccinations Over Time
plt.figure(figsize=(10,6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
plt.title('Total COVID-19 Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.tight_layout()
plt.savefig("vaccinations_over_time.png")
plt.show()

# Compute and print death rates
print("\n🧮 Death Rates:")
for country in countries:
    latest = df[df['location'] == country].iloc[-1]
    rate = latest['total_deaths'] / latest['total_cases']
    print(f"{country}: {rate:.2%}")

