import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file with the correct delimiter
df = pd.read_csv('emails-log.csv', delimiter=';')
df['timestamp_utc'] = pd.to_datetime(df['timestamp_utc'])
df['hour'] = df['timestamp_utc'].dt.hour

# Group by hour and calculate average email size
hourly_avg_size = df.groupby('hour')['size_kb'].mean()
peak_hour = hourly_avg_size.idxmax()
peak_size = hourly_avg_size.max()

print(f"Peak hour: {peak_hour}:00 UTC with average size: {peak_size:.2f} KB")

# Plot the results
plt.figure(figsize=(10, 6))
hourly_avg_size.plot(kind='bar', color='skyblue')
x_positions = range(len(hourly_avg_size))
peak_pos = list(hourly_avg_size.index).index(peak_hour)
plt.axvline(x=peak_pos, color='red', linestyle='--', label=f'Peak Hour: {peak_hour}')
plt.title('Average Email Size by Hour (UTC)')
plt.xlabel('Hour of Day')
plt.ylabel('Average Email Size (KB)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
