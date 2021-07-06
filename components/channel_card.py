import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

def create(channel_number):
    channel_number =str(channel_number)
    layout = html.Div([
        dcc.Input(id="channelName"+channel_number, type="text", placeholder="i.e. TikTok", debounce=True,
                  style={"background-color":"white",
                         "width":"25%",
                         "margin-right":"20px",
                         "text-align":"center",
                         "border-top": "0px solid rgba(20,20,20,0.5)",
                         "border-left": "0px solid rgba(20,20,20,0.5)",
                         "border-right": "0px solid rgba(20,20,20,0.5)",
                         "border-bottom": "2px solid rgba(20,20,20,0.5"

                         }),

        dcc.Input(id="pctwomen"+channel_number, type="text", placeholder="i.e. 0.45", debounce=True,
                  style={"background-color":"white" , "width":"25%",
                        "margin-right":"20px",
                         "text-align": "center",
                         "border-top": "0px solid rgba(20,20,20,0.5)",
                         "border-left": "0px solid rgba(20,20,20,0.5)",
                         "border-right": "0px solid rgba(20,20,20,0.5)",
                         "border-bottom": "2px solid rgba(20,20,20,0.5"
                         }),

        dcc.Input(id="pctretention"+channel_number, type="text", placeholder="i.e. 0.6", debounce=True,
                  style={"background-color":"white",  "width":"25%",
                        "margin-right":"20px",
                         "text-align": "center",
                         "border-top": "0px solid rgba(20,20,20,0.5)",
                         "border-left": "0px solid rgba(20,20,20,0.5)",
                         "border-right": "0px solid rgba(20,20,20,0.5)",
                         "border-bottom": "2px solid rgba(20,20,20,0.5"
                         }),
        dcc.Input(id="cpu"+channel_number, type="text", placeholder="i.e. 1.5", debounce=True,
                  style={"background-color":"white", "width":"25%",
                         "text-align": "center",
                         "border-top": "0px solid rgba(20,20,20,0.5)",
                         "border-left": "0px solid rgba(20,20,20,0.5)",
                         "border-right": "0px solid rgba(20,20,20,0.5)",
                         "border-bottom": "2px solid rgba(20,20,20,0.5"
                         })
    ], style={"background-color":"white",
              "border-radius":"5px",

              "padding":"15px",
              "height":"70px",
              "display":"flex",
              "position":"relative",
              "justify-content": "space-around",
              "margin-bottom":"10px"
              },
    id="card"+channel_number)
    return layout