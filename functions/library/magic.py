import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

markdown = dcc.Markdown('''
```py
def prettify(fig):
    
    fig.update_layout(template="simple_white")
    fig.layout.font = dict(family="Helvetica",
                       size=12,
                       color='rgb(20,20,20)'
                       )
    fig.update_xaxes(tickfont=dict(family='Helvetica',
                                    color='rgb(20,20,20)',
                                    size=12))
    
    fig.update_xaxes(showline=True, linewidth=0.7,
    linecolor='rgb(20,20,20)', tickfont=dict(family='Helvetica',color='rgb(20,20,20)',size=12))
    fig.update_yaxes(showline=True, linewidth=0.7,
    linecolor='rgb(20,20,20)', tickfont=dict(family='Helvetica',color='rgb(20,20,20)',size=12))
    
    return fig
```
''', highlight_config = {'theme':'light'},
    style={'padding-left':'20px',
            'padding-right':'20px', 'width':'700px'})

layout = html.Div([
                html.H3("Prettify function"),
                html.P("Use it to prettify your Plotly figures."),
                ##dcc.Graph(figure=fig_bubbles, config={'displayModeBar': False}),
                html.Br(),
                markdown
                ], style={'padding':'20px', 'padding-left':'30px'})

