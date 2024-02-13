import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html



import dash
import dash_bootstrap_components as dbc
from dash import dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# from interface import app

# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

carousel = dbc.Carousel(
    items=[
        {"key": "1", "src": r"\assets\photo.png", "header": "L'innovation au service de la beauté"},
        {"key": "2", "src": "https://api.ellequebec.com/app/uploads/2023/07/Kendall-Jenner-x-LOreal-1024x512.jpg"},
        {"key": "3", "src": "https://cdn.decrypt.co/resize/1024/height/512/wp-content/uploads/2023/01/NFT-Access-Pass-Visual-Cropped-gID_4.jpg", "header": "Parce que vous le valez bien !"},
    ],
    controls=True,
    indicators=True,
    interval=3500,
    ride="carousel",
    variant = 'dark',
    className = 'my-custom-carousel'
)

#############################################################################################
email_input = html.Div(
    [
        dbc.Label("Email", html_for="example-email"),
        dbc.Input(type="email", id="example-email", placeholder="Email"),
    ],
    className="mb-3",
)

password_input = html.Div(
    [
        dbc.Label("Password", html_for="example-password"),
        dbc.Input(
            type="password",
            id="example-password",
            placeholder="Mot de passe",
        ),
    ],
    className="mb-3",
)

checklist =  dbc.Checkbox(
            label=html.Div(
                ["J'accepte les ", html.A("conditions générales et la politique de confidentialité", href = 'https://www.loreal-paris.fr/customer-service/customer-service-terms-and-conditions.html')]
                ),
            value=False,
        )




inline_switches = html.Div(
    [
        # dbc.Label("Toggle a bunch"),
        dbc.Checklist(
            options=[
                {"label": "Animation", "value": 1},
                {"label": "Contraste", "value": 2},
            ],
            value=[],
            id="switches-inline-input",
            inline=True,
            switch=True,
        ),
    ]
)
form = dbc.Form([email_input, password_input, checklist, inline_switches])


##########################################################################################


modal_acess = html.Div(
    [
        dbc.Button("Se connecter", id="open", n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Acessibilité")),
                dbc.ModalBody( className="text-center", children=form),  # Ajoutez la classe text-center ici
                dbc.ModalFooter(
                    dbc.Button("Se connecter", id="close", className="mx-auto", n_clicks=0)  # Ajoutez la classe mx-auto ici
                ),
            ],
            id="modal",
            is_open=False,
        )])

modal = html.Div(
    [
        dbc.Button("Se connecter", id="open", n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Connexion")),
                dbc.ModalBody(className="text-center", children=form),  # Ajoutez la classe text-center ici
                dbc.ModalFooter(
                    dbc.Button("Se connecter", id="close", className="mx-auto", n_clicks=0)  # Ajoutez la classe mx-auto ici
                ),
            ],
            id="modal",
            is_open=False,
        )])


##################################################
layout = html.Div([
       dbc.Row(
        [
            dbc.Col(html.Div("")),
            dbc.Col(html.Img(src=r'assets\logo.png')),
            dbc.Col(html.Div(""))
        ]),
    modal,
    carousel,
    ])


