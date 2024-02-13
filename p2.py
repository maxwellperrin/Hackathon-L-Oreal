import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd 

df = pd.read_csv(r'C:\Users\theov\Desktop\Hackaton_2\Dash\data_merged.csv')

affichage = dbc.Row([
    dbc.Col(
        html.Img(src=row['image'], className='img-fluid'), width={"size": 2}, )
        for _, row in df.iterrows()
        ],id='image_alignement', className='mt-4')


custom_h1_style = {
    'color': 'white',
    'font-size': '3em',  # Adjust the font size
    'text-shadow': '2px 2px 4px rgba(0, 0, 0, 0.7)',  # Add a subtle text shadow
    'letter-spacing': '2px',  # Increase letter spacing
    'margin-bottom': '20px',  # Add some margin at the bottom
    'text-transform': 'uppercase',  # Convert text to uppercase
}

layout = html.Div([
    dbc.Row(
        [
            dbc.Col(html.Div("")),
            dbc.Col(html.Img(src=r'assets/logo.png')),
            dbc.Col(html.Div("")),
        ]
    ),
    html.Div(style={'height': '50px'}), 
    dbc.Row(html.Hr()),
    dbc.Row(
        [   
            dbc.Col(html.Div("")),
            dbc.Col(html.H1('Mes produits', style=custom_h1_style)),
            dbc.Col(html.Div("")),

        ]
    ),
    dbc.Row(
        [
            dbc.Col(html.P('Veuillez sélectionner vos produits : ', style={'color': 'white'})),
            dbc.Col(dcc.Dropdown(id='first_dropdown',
                                options=[{'label': i, 'value': i} for i in df['category'].unique()],
                                value='',
                                multi=False,
                                placeholder="Sélectionner une catégorie"),
                                width={"size": 6, "offset": 2}
                    )
        ]
    ),

    affichage,
    html.Br(),
    dbc.Row(
        [   
            dbc.Col(html.P("Vous avez des produits d'une autre marque ? Pas de soucis !", style={'color': 'white'})),
            dbc.Col(dcc.Dropdown(id='second_dropdown',
                                options=[{'label': i, 'value': i} for i in df['category'].unique()],
                                value='',
                                multi=False,
                                placeholder="Sélectionner une catégorie"),
                    width={"size": 6, "offset": 2}
                    ),
        ]
    ),

        dbc.Row(
        [
                dbc.Button("Visualiser mes produits", outline=True, color="secondary")
        ]
    )])
















