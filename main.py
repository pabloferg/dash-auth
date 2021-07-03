import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from components import navbar


from app import app, dash_app
from apps import app1, app2

external_stylesheets = [dbc.themes.BOOTSTRAP]

dash_app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

dash_app.title = "( ͡❛ ͜ʖ ͡❛)"

app = dash_app.server




dash_app.layout = html.Div([

    navbar.navbar,
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),
    # content will be rendered in this element
    html.Div(id='page-content', style={"padding": "20px"})
])


@dash_app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return app2.layout
    if pathname == '/apps/app1':
        return app1.layout
    if pathname == '/apps/app2':
        return app2.layout
    else:
        return '404'

if __name__ == '__main__':
    dash_app.run_server(debug=True)