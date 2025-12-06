import pandas as pd
import matplotlib.pyplot as plt
import sys 


print("Loading dataset...")

try:
    df = pd.read_csv("temperature.csv")
    print("\nFirst 10 rows:")
    print(df.head(10))
except FileNotFoundError:
    print("Error: 'temperature.csv' not found. Please ensure the file is in the current directory.")
    sys.exit() 

print("\nChecking missing values:")
print(df.isnull().sum())


if "temperature" in df.columns:
    df["temperature"] = pd.to_numeric(df["temperature"], errors='coerce')
    df["temperature"] = df["temperature"].fillna(df["temperature"].mean())


df = df.dropna(subset=["date"])

print("\nMissing values after cleaning:")
print(df.isnull().sum())

df["date"] = pd.to_datetime(df["date"])


plt.figure(figsize=(10,5))
plt.plot(df["date"], df["temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature Variation Over Time")
plt.tight_layout()
plt.savefig("line_plot.png")
plt.close()

print("Saved line plot as line_plot.png")



df["month"] = df["date"].dt.month_name()


month_order = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]


df["month"] = pd.Categorical(df["month"], categories=month_order, ordered=True)


monthly_avg = df.groupby("month", observed=True)["temperature"].mean()

plt.figure(figsize=(10,5))
plt.bar(monthly_avg.index, monthly_avg.values, color='skyblue') # Added color for visibility
plt.xlabel("Month")
plt.ylabel("Average Temperature")
plt.title("Average Monthly Temperature")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()

print("Saved bar chart as bar_chart.png")

if "min_temp" in df.columns and "max_temp" in df.columns:
   
    df["min_temp"] = pd.to_numeric(df["min_temp"], errors='coerce')
    df["max_temp"] = pd.to_numeric(df["max_temp"], errors='coerce')
    
    plt.figure(figsize=(8,5))
    plt.scatter(df["min_temp"], df["max_temp"], alpha=0.5) # alpha adds transparency
    plt.xlabel("Minimum Temperature")
    plt.ylabel("Maximum Temperature")
    plt.title("Min vs Max Temperature")
    plt.tight_layout()
    plt.savefig("scatter_plot.png")
    plt.close()
    print("Saved scatter plot as scatter_plot.png")

print("\nAll tasks completed successfully!")
