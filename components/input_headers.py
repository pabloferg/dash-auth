import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


layout = html.Div([
    html.H5(id="channelName_header", children="Channel",
              style={"background-color":"white",
                     "width":"25%", "margin-right":"20px"
                     }),

    html.H5(id="pctwomen_header", children="% Women",
            style={"background-color": "white",
                   "width": "25%", "margin-right": "20px"
                   }),

    html.H5(id="pctretention_header", children="% Retention",
              style={"background-color":"white",
                     "width":"25%", "margin-right":"20px"
                     }),
    html.H5(id="cpu_header", children="CPU $",
            style={"background-color": "white",
                   "width": "25%"
                   })
    ,

], style={"background-color":"white",
          "border-radius":"0px",
          "padding":"0px 15px 0px 15px",
          "display":"flex",
          "position":"relative",
          "justify-content": "space-between",
          "text-align":"center"
          })