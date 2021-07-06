import dash_core_components as dcc
import dash_bootstrap_components as dbc

import dash_html_components as html

from functions.library.bubbles_test import layout as layout_bubbles
from functions.library.colors import layout as layout_colors
from functions.library.colors import layout as layout_magic



container = {
  'display': 'grid',
  'grid-template-columns': '0.4fr 1.6fr',
  'grid-template-rows': '1fr',
  'gap': '15px 15px',
  'grid-auto-flow': 'row',
  'grid-template-areas': '"sidebar main"',
  'width': '73.3%',
  'height': '100%',
  'padding-top': '50px',
   'margin': 'auto',
   'background-color': 'white'
}
sidebar = { 'grid-area': 'sidebar',
            'background-color':'white'}
main = {
  'display': 'grid',
  'grid-template-columns': '1fr',
  'grid-template-rows': '0.3fr 1.7fr',
  'gap': '0px 0px',
  'grid-auto-flow': 'row',
  'grid-template-areas': '"header" content"',
  'grid-area': 'main',
    'background-color':'white'
}
header = { 'grid-area': 'header' }
content = { 'grid-area': 'content' }

sidebar_content = html.Div(
    [
        dbc.Nav(
            [   dbc.Button("Colors", id='button_colors', color="light", style={'margin':'5px'}),
                dbc.Button("Bubbles",  id='button_bubbles', color="light", style={'margin':'5px'}),
                dbc.Button("Magic functions",  id='button_magic', color="light", style={'margin':'5px'})
            ],
            vertical=True,
            pills=True,
            style={'border-right':'1px solid rgba(20,20,20,0.1)',
                   'width':'200px'}
        ),
    ])

markdown = dcc.Markdown('''
```py
class BumbleColors:
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

main_content = html.Div([], id="main_content", style={'background-color':'white'})

layout = html.Div([
        html.Div(sidebar_content, style=sidebar),
        html.Div(main_content, style=main),
    ], style=container)

