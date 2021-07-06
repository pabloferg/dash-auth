import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from components import navbar
from components import codesnippet
from components import channel_card



from app import app, dash_app
from apps import app1, app2, slides, slides2, slides3, library

# library content
from functions.library.bubbles_test import layout as layout_bubbles
from functions.library.colors import layout as layout_colors
from functions.library.magic import layout as layout_magic

external_stylesheets = [dbc.themes.BOOTSTRAP]

dash_app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

dash_app.title = "( ͡❛ ͜ʖ ͡❛)"

app = dash_app.server




dash_app.layout = html.Div([



    navbar.navbar,
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),
    # content will be rendered in this element
    html.Div(id='page-content'),
])


@dash_app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return app2.layout
    if pathname == '/app1':
        return app1.layout
    if pathname == '/app2':
        return app2.layout
    if pathname == '/slides':
        return slides.layout
    if pathname == '/slides2':
        return slides2.layout
    if pathname == '/slides3':
        return slides3.layout
    if pathname == '/library':
        return library.layout
    else:
        return '404'




@dash_app.callback(
    Output("channels", 'children'),
    [Input('add-channel', 'n_clicks')]
    )
def update_output(n_clicks):
    list_channels = [channel_card.create(n) for n in range(n_clicks)]
    return list_channels

@dash_app.callback(
    Output("some-text", 'children'),
    [Input('channels', 'children')],
    )
def update_output(children):
    global num_channels
    num_channels = len(children)
    return str(len(children))

@dash_app.callback(
    Output("some-text2", 'children'),
    [Input('button-get-results', 'n_clicks')],
    [State("channels",'children')]
    )
def update_output(children, state):
    print("pablo")
    print(len(state))
    for s in state:
        print(s)
        for input in s['props']['children']:
            if 'value' in input['props'].keys():
                print(input['props']['id'] +"---", input['props']['value'])
            else:
                print(input['props']['id'])

@dash_app.callback(
    Output("main_content", "children"),
    [Input('button_colors', 'n_clicks'),
     Input('button_bubbles', 'n_clicks'),
     Input('button_magic', 'n_clicks')]
)
def on_button_click(btn1, btn2,btn3):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'button_colors' in changed_id:
        main_content_layout = layout_colors
    elif 'button_bubbles' in changed_id:
        main_content_layout = layout_bubbles
    elif 'button_magic' in changed_id:
        main_content_layout = layout_magic
    else:
        main_content_layout = []
    return main_content_layout


    return str(len(state))





if __name__ == '__main__':
    dash_app.run_server(debug=True)