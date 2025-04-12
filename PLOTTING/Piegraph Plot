import plotly.graph_objects as go

labels = ['apples', 'bananas', 'oranges', 'kiwi']
values = [40, 25, 20, 15]

fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3)])
fig.update_traces(textinfo='percent+label', pull=[0, 0, 0, 0.3])
fig.update_layout(title="3D-Style Pie Plot")

fig.show()
