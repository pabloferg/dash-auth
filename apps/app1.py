import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from main import app

from components import input
from components import input_headers
from components import channel_card
from components import button_add_channel
from components import button_get_results
from components import restrictions_main



layout = html.Div([
    html.Div([
        html.H3(''),
        html.Br(),
        button_get_results.layout,
        html.Br(),
        html.Br(),
        restrictions_main.layout,
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        button_add_channel.layout,
        html.Br(),
        html.Br(),
        input_headers.layout,
        html.Div([],
                 id="channels",
                 style={"margin-top":"5px",
                                               "background-color":"white"}),
        html.P(children="aaaaa",id="some-text",style={"visibility":"hidden"}),
        html.P(children="aaaaa",id="some-text2",style={"visibility":"hidden"})


    ], style={"float":"left",
                                     "background-color":"white",
                                     "width":"50%"})

    ,html.Div([
        html.H3(''),
        html.Div([
            html.P("", id="maximise-text"),
            html.P("", id="equation")
        ])]
        ,style={"background-color":"white"} )
        ],

style={"padding-top" : "50px",
       "margin":"auto",
       "width" : "80%",
       "background-color": "white",
       "diplay":"inline-block"})



