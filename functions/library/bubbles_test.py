import plotly.graph_objects as go
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from functions.helpers.helpers import prettify

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



markdown = dcc.Markdown('''
```py
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
                dcc.Graph(figure=fig, config={'displayModeBar': False}),
                html.Br(),
                markdown
                ], style={'padding':'20px', 'padding-left':'30px'})
