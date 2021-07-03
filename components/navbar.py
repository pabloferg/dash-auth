import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

NAV_LOGO = "assets/android-chrome-512x512.png"

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=NAV_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("  ", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://plotly.com",
        ),
        dbc.NavLink("Intro", active=True, style={"color":"rgba(0,0,0,1)"}, href='/apps/app2'),
        dbc.NavLink("Linear Programming", style={"color":"rgba(0,0,0,1)"}, active=True, href='/apps/app1')

    ],
    color="rgba(0,0,0,0)",
    #dark=True,
)