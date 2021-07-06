import plotly.graph_objects as go
import numpy as np

def prettify(fig):
    fig.update_layout(template="simple_white")

    fig.layout.font = dict(family="Helvetica",
                           size=12,
                           color='rgb(20,20,20)'
                           )
    fig.update_xaxes(tickfont=dict(family='Helvetica',
                                   color='rgb(20,20,20)',
                                   size=12))

    fig.update_xaxes(showline=True, linewidth=0.7, linecolor='rgb(20,20,20)',
                     tickfont=dict(family='Helvetica', color='rgb(20,20,20)', size=12))
    fig.update_yaxes(showline=True, linewidth=0.7, linecolor='rgb(20,20,20)',
                     tickfont=dict(family='Helvetica', color='rgb(20,20,20)', size=12))

    return fig


class MagicColors:
    yellow = 'rgba(255,189,54,1)'
    purple = 'rgba(95,20,218,1)'
    pink = 'rgba(239,138,172,1)'
    darkblue = 'rgba(0,118,155,1)'
    lightblue = 'rgba(68,168,202,1)'
    red = 'rgba(181,45,93,1)'
    green = 'rgba(0,145,141,1)'
    orange = 'rgba(255,93,54,1)'


locations = ['London', 'Manchester', 'Liverpool', 'Northamptonshire', 'Edinburgh', 'Glasgow']

bees = {'drone': [0.1, 0.4, 0.3, 0.6, 0.2, 0.4],
        'queen': [0.5, 0.1, 0.5, 0.9, 0.2, 0.6],
        'worker': [0.3, 0.7, 0.5, 0.8, 0.6, 0.6]}
bees_colors = {'drone': MagicColors.darkblue,
               'queen': MagicColors.orange,
               'worker': MagicColors.green, }

fig = go.Figure(data=[
    go.Bar(x=locations, y=np.array(bees['drone']) * 100, marker_color=bees_colors['drone']),
    go.Bar(x=locations, y=np.array(bees['queen']) * 100, marker_color=bees_colors['queen']),
    go.Bar(x=locations, y=np.array(bees['worker']) * 100, marker_color=bees_colors['worker'])

])

# Change the bar mode


fig = fig.update_layout(title="Honey Production by Region", showlegend=False)
fig=prettify(fig)
# fig.update_yaxes(tickfont_size=15)
# fig.update_xaxes(tickfont_size=15)


