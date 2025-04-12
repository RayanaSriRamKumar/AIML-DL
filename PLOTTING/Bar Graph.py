import matplotlib.pyplot as plt

# Data
labels = ['Apples', 'Banana', 'Orange', 'Kiwi']
sizes = [40, 25, 25, 15]
colors = ['red', 'yellow', 'orange', 'darkgreen']

# Create the bar plot
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(labels, sizes, color=colors)

# Annotate each bar with its value
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Set title and labels
ax.set_title("Fruit Distribution", fontsize=16)
ax.set_ylabel("Percentage")
ax.set_ylim(0, max(sizes) + 10)  # add some space on top

plt.tight_layout()
plt.show()
