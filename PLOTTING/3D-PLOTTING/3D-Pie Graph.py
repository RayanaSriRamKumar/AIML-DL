import matplotlib.pyplot as plt
labels = ['Apples', 'Banana', 'Orange', 'Kiwi']
sizes = [40, 25, 25, 15]
colors = ['red', 'yellow', 'orange', 'darkgreen']
explode = (0.2, 0, 0, 0)
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(sizes, explode=explode, labels=None, colors=['grey']*4, 
       radius=1.05, startangle=140)
ax.pie(sizes, explode=explode, labels=labels, colors=colors, 
       autopct='%1.1f%%', startangle=140, pctdistance=0.85)
center_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(center_circle)
ax.set_title("Simulated 3D Pie", fontsize=16)
plt.tight_layout()
plt.show()
