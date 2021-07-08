import plotly.graph_objects as go
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from functions.helpers.helpers import prettify

size = [20, 40, 60, 80, 100, 80, 60, 40, 20, 40]
fig_bubbles = go.Figure(data=[go.Scatter(
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    y=[11, 12, 10, 11, 12, 11, 12, 13, 12, 11],
    mode='markers',
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        color='rgba(20,20,20,1)'
    )
)])
fig_bubbles.update_layout(height=300, width=1000, xaxis_visible=True, yaxis_visible=True)
fig_bubbles = prettify(fig_bubbles)



markdown = dcc.Markdown('''
```py
#Helloooo!!!
import plotly.graph_objects as go
import prettify # see Magic Functions

size = [20, 40, 60, 80, 100, 80, 60, 40, 20, 40]
fig = go.Figure(data=[go.Scatter(
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    y=[11, 12, 10, 11, 12, 11, 12, 13, 12, 11],
    mode='markers',
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4
    )
)])

fig = prettify(fig)
```
''', style={'padding-left':'20px',
            'padding-right':'20px'})

layout = html.Div([
                html.H3("Bubbles"),
                html.P("Bubbles are great to show multiple variables at the same time."),
                dcc.Graph(figure=fig_bubbles, config={'displayModeBar': False}),
                html.Br(),
                markdown
                ], style={'padding':'20px', 'padding-left':'30px'})
