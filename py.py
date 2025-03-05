
import pandas as pd
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    "Timestamp (min:sec)": ["00:00", "05:00", "10:00", "15:00", "20:00", "25:00", "30:00",
                             "35:00", "40:00", "45:00", "50:00", "55:00", "60:00"],
    "Total Viewers": [10000, 9800, 9200, 8700, 8500, 7900, 6500, 6300, 6100, 5800, 5600, 5100, 4500],
    "Viewers Dropped Off": [0, 200, 600, 500, 200, 600, 1400, 200, 200, 300, 200, 500, 600],
    "Drop-Off Rate (%)": [0.00, 2.00, 6.12, 5.43, 2.30, 7.06, 17.72, 3.08, 3.17, 4.92, 3.45, 8.93, 11.76],
    "Ad Placement": ["No", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "Yes"],
    "Engagement Score (1-10)": [7, 8, 9, 9.5, 8.8, 7.5, 5.0, 6.5, 7.0, 8.2, 7.8, 6.0, 5.5]
}

# Converting to a DataFrame
df = pd.DataFrame(data)

# Plotting the trends
fig, ax1 = plt.subplots(figsize=(10,5))

# Plotting Total Viewers (on the left y-axis)
ax1.plot(df["Timestamp (min:sec)"], df["Total Viewers"], marker='o', label="Total Viewers", color='b')
ax1.set_xlabel("Timestamp (min:sec)")
ax1.set_ylabel("Total Viewers", color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Creating a second y-axis for the Drop-Off Rate (%)
ax2 = ax1.twinx()
ax2.plot(df["Timestamp (min:sec)"], df["Drop-Off Rate (%)"], marker='s', label="Drop-Off Rate (%)", color='r')
ax2.set_ylabel("Drop-Off Rate (%)", color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Highlighting Ad Placements
ad_placements = df[df["Ad Placement"] == "Yes"]
ax1.scatter(ad_placements["Timestamp (min:sec)"], ad_placements["Total Viewers"], color='g', s=100, label="Ad Placement", zorder=5)

# Adding grid, title, and legend
fig.tight_layout()
plt.title("Viewer Engagement, Drop-Off, and Ad Placement Analysis")
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
