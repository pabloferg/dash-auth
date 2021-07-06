import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime


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



# Create random data with numpy
import numpy as np
np.random.seed(1)

N = 100
base = datetime.datetime.today()
x_dates = [base - datetime.timedelta(days=x) for x in range(N)]

random_y0 = np.random.randn(N) + 20
random_y1 = np.random.randn(N) + 25
random_y2 = np.random.randn(N) + 30


fig = go.Figure()



x = x_dates
bees = {'drone' : random_y0,
        'queen' : random_y1,
        'worker' : random_y2}
bees_colors = {'drone' : MagicColors.darkblue,
               'queen' : MagicColors.orange,
               'worker' : MagicColors.green ,}

for bee in bees:

    fig.add_trace(go.Scatter(x=x, y=bees[bee],
                             mode='lines',
                             name=bee,
                             line=dict( color = bees_colors[bee], width=4))
                  )

fig.update_layout( title ='Honey Production by type of bee'  )  # , height = 500, width = 600)

fig = prettify(fig)
