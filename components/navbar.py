import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State


navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src="assets/android-chrome-512x512.png", height="30px")),
                    dbc.Col(dbc.NavbarBrand("  ", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://plotly.com",
        ),
        dbc.NavLink("Intro", id='button_navbar_intro', active=True, style={"color":"rgba(0,0,0,1)"}, href='/app2'),
        dbc.NavLink("Linear Programming", id='button_navbar_lp',  style={"color":"rgba(0,0,0,1)"}, active=True, href='/app1'),
        dbc.NavLink("Slides", id='button_navbar_slides',  style={"color": "rgba(0,0,0,1)"}, active=True, href='/slides'),
        dbc.NavLink("Slides2", id='button_navbar_slides2',  style={"color": "rgba(0,0,0,1)"}, active=True, href='/slides2'),
        dbc.NavLink("Slides3", id='button_navbar_slides3',  style={"color": "rgba(0,0,0,1)"}, active=True, href='/slides3'),
        dbc.NavLink("Library", id='button_navbar_library',  style={"color": "rgba(0,0,0,1)"}, active=True, href='/library')

    ],
    color="rgba(0,0,0,0)",
    #dark=True,
)