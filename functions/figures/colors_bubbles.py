import plotly.graph_objects as go
from functions.helpers.helpers import prettify

MagicColors = dict(
    yellow = 'rgba(255,189,54,1)',
    purple = 'rgba(95,20,218,1)',
    pink = 'rgba(239,138,172,1)',
    darkblue = 'rgba(0,118,155,1)',
    lightblue = 'rgba(68,168,202,1)',
    red = 'rgba(181,45,93,1)',
    green = 'rgba(0,145,141,1)',
    orange = 'rgba(255,93,54,1)',
)

x=[ color for color in MagicColors]
y = [1]* len(x)

fig = go.Figure(data=[go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker_color = [MagicColors[color] for color in MagicColors],
    marker_size=[70 for color in MagicColors],
    marker_opacity=1)

])
fig.update_layout(height=400, width=1000, xaxis_visible=False, yaxis_visible=False)
fig = prettify(fig)
