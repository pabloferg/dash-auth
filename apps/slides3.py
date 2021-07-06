import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from functions.figures.bees_trendline import fig as fig_bee_trendline
from functions.figures.bees_bars import fig as fig_bee_bars

lightyellow = "rgba(255, 254, 219,1"

container = {
  'display': 'grid',
  'grid-template-columns': '1fr 1fr',
  'grid-template-rows': '0fr 0fr 0fr 0fr',
  'gap': '15px 15px',
  'grid-auto-flow': 'row',
  'grid-template-areas':'"header header" "a b" "c d" "footer footer"',
  'width': '73.3%',
  'height': 'full',
  'padding-top' : '50px',
    'margin': 'auto',
}

c_white = 'white'

header = { 'grid-area': 'header',
      'background-color':c_white,
      'border':'0px solid rgba(235, 234, 206,1)',
      'height':'50px'}

a = { 'grid-area': 'a' ,
      'background-color':c_white,
'border':'0px solid rgba(235, 234, 206,1)',
      'height':'300px'}
b= { 'grid-area': 'b', 'background-color':c_white,
     'border':'0px solid rgba(235, 234, 206,1)',}
c = { 'grid-area': 'c' ,
      'background-color':c_white,
'border':'0px solid rgba(235, 234, 206,1)',
      'height':'300px'}
d = { 'grid-area': 'd', 'background-color':c_white,
      'border':'0px solid rgba(235, 234, 206,1)',}
footer = { 'grid-area': 'footer',
           'background-color':c_white,
'border':'0px solid rgba(235, 234, 206,1)',
           'height':'50px'}

header_text = html.H2("The bees are the best insect in United Kingdom")
bee_graph_trend = dcc.Graph(figure=fig_bee_trendline,
                      config={'displayModeBar': False},
                      style={'height':'100%'})
bee_graph_bars = dcc.Graph(figure=fig_bee_bars,
                      config={'displayModeBar': False},
                      style={'height':'100%'})
layout = html.Div([
        html.Div(header_text, style=header),
        html.Div(bee_graph_trend, style=a),
        html.Div(bee_graph_bars,style=b),
        html.Div(bee_graph_trend,style=c),
        html.Div(bee_graph_bars,style=d),
        html.Div("",style=footer)
    ], style=container)



style={"padding-top" : "50px",
       "margin":"auto",
       "width" : "80%",
       "background-color": "white",
       "diplay":"inline-block"}



