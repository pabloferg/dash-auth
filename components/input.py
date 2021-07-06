import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


layout = html.Div([
    html.H4("Budget:", style={"margin-bottom":"20px"}),
    dcc.Input(id="input2", type="text", placeholder="i.e. 8000000", debounce=True,
              style={
                     "border-top":"0px solid rgba(20,20,20,0.5)",
                     "border-left":"0px solid rgba(20,20,20,0.5)",
                     "border-right":"0px solid rgba(20,20,20,0.5)",
                     "border-bottom":"2px solid rgba(20,20,20,0.5"}),
], style={"background-color":"red"})

