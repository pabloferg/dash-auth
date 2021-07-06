import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

markdown = dcc.Markdown('''
```py
class MagicColors:
    yellow = 'rgba(255,189,54,1)'
    purple = 'rgba(95,20,218,1)'
    pink = 'rgba(239,138,172,1)'
    darkblue = 'rgba(0,118,155,1)'
    lightblue = 'rgba(68,168,202,1)'
    red = 'rgba(181,45,93,1)'
    green = 'rgba(0,145,141,1)'
    orange = 'rgba(255,93,54,1)'
```
''', style={'padding-left':'20px',
            'padding-right':'20px'})

layout = html.Div([
                html.H3("Colors"),
                html.P("Make your graphs look great with these colors."),
                ##dcc.Graph(figure=fig_bubbles, config={'displayModeBar': False}),
                html.Br(),
                markdown
                ], style={'padding':'20px', 'padding-left':'30px'})