import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import dash_app

layout = html.Div([
    html.H3('Welcome to the Proof Of Concept of Dash 😊'),
    html.P('This application is written in Python and deployed in GCP App Engine ☁️'),
    html.P('and deployed via Github Actions')

])


