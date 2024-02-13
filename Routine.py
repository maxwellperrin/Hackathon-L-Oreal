import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd 
from sklearn.neighbors import NearestNeighbors



df = pd.read_csv("assets/data_to_ML.csv")
df_palette = pd.read_csv("assets/data_palette.csv")
radioitems_moment = html.Div(
    [   
        # dbc.Label("Choose one"),
        dbc.RadioItems(
            options=[
                {"label": "Le matin", "value": 1},
                {"label": "Le soir", "value": 2},
            ],
            value=1,
            id="radioitems_moment",
        ),
    ]
)
liste_deroulante = html.Div(dcc.Dropdown(id='dropdown_type',
                                options=[{'label': i, 'value': i} for i in df_palette['style'].unique()],
                                value='',
                                multi=False,
                                placeholder="Sélectionner une catégorie"),
                    )




layout = html.Div([
    dbc.Row(
        [
            dbc.Col(html.Div("")),
            dbc.Col(html.Img(src=r'assets/logo.png')),
            dbc.Col(html.Div(""))
        ]
    ),
    html.Div(style={'height': '50px'}), 
    dbc.Row(html.Hr()),
    dbc.Row(
        [
            dbc.Col(html.H1('Ma routine Make up', style={'color': 'white'})),
        ]
    ),

    html.Div(style={'height': '30px'}), 

    dbc.Row(
        [
            dbc.Col
                (
                dbc.Card
                    ([
                    dbc.CardHeader("On se prépare pour ..."),
                    dbc.CardBody(radioitems_moment)
                    ],
                    className="rounded",
                    style={"width": "18rem"}
                    )
                ),
            dbc.Col
                (
                dbc.Card
                    ([
                    dbc.CardBody([
                                dbc.Button("J'ajoute ma photo" , className="mx-auto"),
                                html.P('Ou', style={"text-align": "center"}),
                                dbc.Button("Je choisis mon teint" , className="mx-auto")
                                ])
                    ],
                    className="rounded",
                    style={"text-align": "center"}
                    )
                ),
            dbc.Col
                (
                dbc.Card
                    ([
                    dbc.CardHeader("Et je recherche plutôt ..."),
                    dbc.CardBody(liste_deroulante)
                    ],
                    className="rounded",
                    # style={"width": "18rem"}
                    )
                ),
        ]
    ),
    dbc.Row(html.Br()),
    dbc.Row(html.Br()),
    dbc.Row(html.Br()),
    dbc.Row([
        dbc.Col(''),
        dbc.Col
            ([
                html.Img(src ='', id = 'rouge_a_levre_img', width = '', height = ''),
                html.P('', id ='rouge_a_levre_name', style={'color': 'white'}),
                html.Img(src ='', id = 'skin_care_img', width = '', height = ''),
                html.P('', id ='skin_care_name', style={'color': 'white'})
            ]),
        dbc.Col(''),
    ]),
    dbc.Row([
        dbc.Col(''),
        dbc.Col
            ([
                html.Img(src ='', id = 'fard_paupiere_img',  width = '', height = ''),
                html.P('', id ='fard_paupiere_name', style={'color': 'white'})
            ]),
        dbc.Col(''),
    ]),
    dbc.Row([
        dbc.Col(''),
        dbc.Col
            ([
                html.Img(src ='', id = 'fond_teint_img',  width = '', height = ''),
                html.P('', id ='fond_teint_name', style={'color': 'white'})
            ]),
        dbc.Col(''),
    ])
])


