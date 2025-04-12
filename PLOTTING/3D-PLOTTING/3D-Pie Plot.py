import matplotlib.pyplot as plt
labels = ['Apples', 'Banana', 'Orange', 'Kiwi']
sizes = [40, 25, 25, 15]
colors = ['red', 'yellow', 'orange', 'darkgreen']
explode = (0, 0, 0, 0.3) 
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, startangle=120, explode=explode,
        shadow=True, colors= colors, textprops={'fontsize': 12, 'color': 'black'})
plt.title("Fruits in the store", fontsize=16, fontweight= 'bold')
plt.axis('equal')
plt.tight_layout()
plt.show()