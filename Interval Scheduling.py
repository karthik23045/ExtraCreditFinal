import matplotlib.pyplot as plt

intervals = [(2, 5), (5, 10), (10, 20), (20, 30), (30, 45)]

# sorting the intervals
intervals.sort(key=lambda x: x[1])
print(intervals)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the intervals as horizontal bars
for i, interval in enumerate(intervals):
    ax.barh(i, interval[1] - interval[0], left=interval[0], color='skyblue', edgecolor='black')
    ax.text(interval[0] + (interval[1] - interval[0]) / 2, i, f"{interval[0]} - {interval[1]}", ha='center', va='center', color='black')

# Set y-axis labels
ax.set_yticks(range(len(intervals)))
ax.set_yticklabels([f"Interval {i+1}" for i in range(len(intervals))])

# Set x-axis label
ax.set_xlabel('Time')

# Set title
ax.set_title('Non-overlapping Intervals')

# Invert y-axis
ax.invert_yaxis()

# Show plot
plt.show()
