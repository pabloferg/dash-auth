import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import dash_app


layout = html.Div([
    html.Button('Add channel', id='add-channel', n_clicks=2,
                style={'background-color':'rgba(166, 166, 166,0.3)',
                       'border-color':'rgba(166, 166, 166,1)',
                       'border':'5px',
                       'border-radius':'10px',
                       "float":"right"})
    ,

], style={"background-color":"pink",
            "display":"absolute",
          "margin-bottom":"20px",
          "position":"relative",
          })


