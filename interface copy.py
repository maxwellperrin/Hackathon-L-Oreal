import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html



import dash
import dash_bootstrap_components as dbc
from dash import dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd

from pages import Routine, p2, p1

#  <__name__, use_pages=True

df = pd.read_csv("assets/data_to_ML.csv")
df_palette = pd.read_csv("assets/data_palette.csv")

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])# the style arguments for the sidebar. We use position:fixed and a fixed width


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 62.5,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    "background-color": "#F8F9FA",
}

BUTTON_LEFT = {
    "margin-left": "auto",
    "children": "Close",# Ajustez la marge à gauche pour le bouton lorsqu'il est à gauche
}

BUTTON_RIGHT = {
    "margin-left": "14rem",
    "children": ">",  # Définissez la marge à gauche sur "auto" pour décaler vers la droite
}

SIDEBAR_HIDEN = {
    "position": "fixed",
    "top": 62.5,
    "left": "-14rem",
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    # "background-color": "#F8F9FA",
    }
# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#F8F9FA",
}

CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#F8F9FA",
}


sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        dbc.Button("Close", outline=True, color="secondary", className="mr-1", id="btn_sidebar", style=BUTTON_LEFT),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Page 1", href="/page-1",),
                dbc.NavLink("Page 2", href="/page-2", ),
                dbc.NavLink("Routine", href="/page-3",),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)
content = html.Div(    id="page-content",
                   
    style=CONTENT_STYLE)

# app.layout = html.Div(
#     [
#         dcc.Store(id='side_click'),
#         dcc.Location(id="url"),
#         sidebar,
#         content,
#     ]
# )

app.layout = html.Div([    
                       dcc.Location(id='url', refresh=False),
    sidebar,    
    html.Div( [html.Div( [html.H6('1')], id = 'page-1-link' ),
               html.Div( [html.H6('2')], id = 'page-2-link' ),
               html.Div( [html.H6('3')], id = 'page-3-link' )],
              style = {'display': 'block'})
])

@app.callback(
    [
        Output("sidebar", "style"),
        # Output("page-content", "style"),
        # Output("side_click", "data"),
        Output("btn_sidebar", "style"),
        Output("btn_sidebar", "children"),
        
    ],    
    [Input("btn_sidebar", "n_clicks")],
    # [
        # State("side_click", "data"),
    # ]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDEN
            button_style = BUTTON_RIGHT
            content_style = CONTENT_STYLE1
            cur_nclick = "HIDDEN"
            button_text = ">"

        else:
            sidebar_style = SIDEBAR_STYLE
            button_style = BUTTON_LEFT
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"
            button_text = "Close"

    else:
        sidebar_style = SIDEBAR_STYLE
        button_style = BUTTON_LEFT
        content_style = CONTENT_STYLE
        cur_nclick = 'SHOW'
        button_text = "Close"    
    
    return sidebar_style, content_style, cur_nclick, button_style, button_text






# corresponding nav link to true, allowing users to tell see page they are on
# @app.callback(
#     [Output(f"page-{i}-link", "active") for i in range(1, 4)],
#     [Input("url", "pathname")],
# )
# def toggle_active_links(pathname):
#     # if pathname == "/":
#     #     # Treat page 1 as the homepage / index
#     #     return True, False, False
#     return [pathname == f"/page-{i}" for i in range(1, 4)]

# @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
# def render_page_content(pathname):
#     if pathname ==  "/page-1":
#         return  p1.layout
#     elif pathname == "/page-2":
#         return p2.layout
#     elif pathname == "/page-3":
#         return Routine.layout





################################### Est-ce qu'il vaut mieux pas faire une autre page pour être précis dans le code ? 
# Eventuellement sur la page d'accueil, les promotions directement ? Les produits les plus en vogues, les tendances, les tutos etc
#Caler le caroussel a ce moment la ? 


# Puis, directement la deuxième page routine etc... Ca permettra de modifier les pages indivduellements

# nav_menu = html.Div([
#     dcc.Link('  [Page A]  ', href='/page-a'),
#     dcc.Link('  [Page B]  ', href='/page-b'),

# ])

@app.callback(
    Output(component_id='page-1-link', component_property='style'),
    [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return {'display': 'block'}
    else:
        return {'display': 'none'}

@app.callback(
    Output(component_id='page-2-link', component_property='style'),
    [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/page-2':
        return {'display': 'block'}
    else:
        return {'display': 'none'}
    
@app.callback(
    Output(component_id='page-3-link', component_property='style'),
    [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/page-3':
        return {'display': 'block'}
    else:
        return {'display': 'none'}
    
if __name__ == "__main__":
    app.run_server(debug=True, port=8086)

