import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from main import app

lightyellow = "rgba(255, 254, 219,1"

container = {
  'display': 'grid',
  'grid-template-columns': '1fr 1fr 1fr',
  'grid-template-rows': '0fr 0fr 0fr 0fr',
  'gap': '15px 15px',
  'grid-auto-flow': 'row',
  'grid-template-areas':'"header header header" \
                        "a b c" \
                        "d e f"\
                        "footer footer footer"',
  'width': '73.3%',
  'height': 'full',
  'padding-top' : '50px',
    'margin': 'auto',
}


header = { 'grid-area': 'header',
      'background-color':lightyellow,
      'border':'1px solid rgba(235, 234, 206,1)',
      'height':'50px'}

a = { 'grid-area': 'a' ,
      'background-color':lightyellow,
'border':'1px solid rgba(235, 234, 206,1)',
      'height':'300px'}
b= { 'grid-area': 'b', 'background-color':lightyellow,
     'border':'1px solid rgba(235, 234, 206,1)',}
c = { 'grid-area': 'c' ,
      'background-color':lightyellow,
'border':'1px solid rgba(235, 234, 206,1)',
      'height':'300px'}
d = { 'grid-area': 'd' ,
      'background-color':lightyellow,
        'border':'1px solid rgba(235, 234, 206,1)',
      'height':'300px'}

e = { 'grid-area': 'e', 'background-color':lightyellow,
      'border':'1px solid rgba(235, 234, 206,1)',}
f = { 'grid-area': 'f', 'background-color':lightyellow,
      'border':'1px solid rgba(235, 234, 206,1)',}

footer = { 'grid-area': 'footer',
           'background-color':lightyellow,
'border':'1px solid rgba(235, 234, 206,1)',
           'height':'50px'}


layout = html.Div([
        html.Div("", style=header),
        html.Div("", style=a),
        html.Div("",style=b),
        html.Div("",style=c),
        html.Div("",style=d),
        html.Div("",style=e),
        html.Div("",style=f),
        html.Div("",style=footer)
    ], style=container)



style={"padding-top" : "50px",
       "margin":"auto",
       "width" : "80%",
       "background-color": "white",
       "diplay":"inline-block"}



