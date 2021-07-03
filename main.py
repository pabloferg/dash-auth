import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from components import navbar


from app import dash_app
from apps import app1, app2





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