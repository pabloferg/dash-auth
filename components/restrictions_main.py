import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


layout = html.Div([
    html.H4("Restrictions:", style={"margin-bottom":"20px"}),
    html.Div([
        html.Div([
                html.P("Budget:", style={"margin":"auto",
                                          "margin-right":"5px",
                                          "text-align":"right",
                                          "width":"150px",
                                          "background-color":"white"}),
                dcc.Input(id="input5", type="text", placeholder="", debounce=True,
                      style={
                             "border-top":"0px solid rgba(20,20,20,0.5)",
                             "border-left":"0px solid rgba(20,20,20,0.5)",
                             "border-right":"0px solid rgba(20,20,20,0.5)",
                             "border-bottom":"2px solid rgba(20,20,20,0.5"}),

            ], style={"background-color":"white",
                      "margin":"auto",
                      "display": "flex",
                      "float":"left",
                      }),
        html.Div([
                html.P("% Women:", style={"margin":"auto",
                                          "margin-right":"5px",
                                          "text-align":"right",
                                          "width":"150px",
                                          "background-color":"white"}),
                dcc.Input(id="input5", type="text", placeholder="", debounce=True,
                      style={
                             "border-top":"0px solid rgba(20,20,20,0.5)",
                             "border-left":"0px solid rgba(20,20,20,0.5)",
                             "border-right":"0px solid rgba(20,20,20,0.5)",
                             "border-bottom":"2px solid rgba(20,20,20,0.5"}),

            ], style={"background-color":"white",
                      "margin":"auto",
                      "display": "flex",
                      "float":"left",
                      }),

        html.Div([
                html.P("% Retention:", style={"margin":"auto",
                                          "margin-right":"5px",
                                          "text-align":"right",
                                          "width":"150px",
                                          "background-color":"white"}),
                dcc.Input(id="input2", type="text", placeholder="", debounce=True,
                          style={
                              "border-top": "0px solid rgba(20,20,20,0.5)",
                              "border-left": "0px solid rgba(20,20,20,0.5)",
                              "border-right": "0px solid rgba(20,20,20,0.5)",
                              "border-bottom": "2px solid rgba(20,20,20,0.5"}),

            ], style={"background-color": "white",
                      "margin": "auto",
                      "display": "flex",
                        "float":"left",
                      }),
        html.Div([
                html.P("Cost per User $:", style={"margin":"auto",
                                          "margin-right":"5px",
                                          "text-align":"right",
                                          "width":"150px",
                                          "background-color":"white"}),
                dcc.Input(id="input2", type="text", placeholder="", debounce=True,
                          style={
                              "border-top": "0px solid rgba(20,20,20,0.5)",
                              "border-left": "0px solid rgba(20,20,20,0.5)",
                              "border-right": "0px solid rgba(20,20,20,0.5)",
                              "border-bottom": "2px solid rgba(20,20,20,0.5"}),

            ], style={"background-color": "white",
                      "margin": "auto",
                      "display": "flex",
                    "float":"left",
                      })


            ] , style={"background-color":"white",
          "display":"grid",
                       "float":"left"
         })

]
, style={"background-color":"white",
          "display":"block"
         })

