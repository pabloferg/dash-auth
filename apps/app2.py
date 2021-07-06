import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import dash_app

layout = html.Div([
    html.H1('Welcome to the Proof Of Concept of Dash'),
    html.Br(),
    html.P('This application is written in Python and deployed in GCP App Engine ☁️'),
    html.P('and deployed via Github Actions'),
    html.Br(),
    html.H2('Why?'),
    html.Br(),
    html.P('Notebooks and Slides are great to analyse and present data.'),
    html.P('Notebooks and Slides are great to analyse and present data.'),

    html.Br(),

]
, style={"padding-top" : "50px",
         "margin":"auto",
         "width" : "50%",
         "background-color": "white"})


