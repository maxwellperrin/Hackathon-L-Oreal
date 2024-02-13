import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import pandas as pd 
from sklearn.neighbors import NearestNeighbors

import dash
import dash_bootstrap_components as dbc
from dash import dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from pages import Routine, p2, p1

from derm_ita import get_ita
from PIL import Image
from derm_ita import get_kinyanjui_type




df_data_merged = pd.read_csv(r'C:\Users\theov\Desktop\Hackaton_2\Dash\data_merged.csv')
df = pd.read_csv("assets/data_to_ML.csv")
df_palette = pd.read_csv("assets/data_palette.csv")


app = dash.Dash(external_stylesheets=[dbc.themes.LUX])# the style arguments for the sidebar. We use position:fixed and a fixed width

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
    "left": "-13rem",
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
    "background-color": "#0D0D0D",
}

CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#0D0D0D"
}

#0D0D0D
sidebar = html.Div(
    [
        html.H2("", className="display-4"),
        dbc.Button("Close", outline=True, color="secondary", className="mr-1", id="btn_sidebar", style=BUTTON_LEFT),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Accueil", href="/page-1", id="page-1-link"),
                dbc.NavLink("Mes produits", href="/page-2", id="page-2-link"),
                dbc.NavLink("Routine", href="/page-3", id="page-3-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)
content = html.Div(id="page-content",
                                      
    style=CONTENT_STYLE)


################################" futur code ML pour couleur de peau

dico_color_skin = {"dark" : (169, 117, 78),"tan1" : (182, 137, 96),"tan2" : (196, 151, 109),
              "int1" : (212, 174, 129),"int2" : (217, 179, 134) ,"lt1" : (219, 181, 136),
              "lt2" : (222, 183, 140),"very_lt" : (225,191,154)}
image_path = 'assets/peau_bronze.jpg'
whole_image_ita = get_ita(image=Image.open(image_path))
kinyanjui_type = get_kinyanjui_type(whole_image_ita)
skin_color_code = dico_color_skin[kinyanjui_type]

##################################


app.layout = html.Div(
    [
        dcc.Store(id='side_click'),
        dcc.Location(id="url"),
        sidebar,
        content,
       
    ]
)

@app.callback(
    [
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),
        Output("btn_sidebar", "style"),
        Output("btn_sidebar", "children"),
        
    ],    
    [Input("btn_sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ]
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
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    # if pathname == "/":
    #     # Treat page 1 as the homepage / index
    #     return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]



@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname ==  "/page-1":        
        return  p1.layout        
    elif pathname == "/page-2":
        return p2.layout
    elif pathname == "/page-3":
        return Routine.layout


###################################"" Call back Page 1 
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)

def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
######################################## Call back Page 2



@app.callback(

    Output('image_alignement', 'children'),

    [Input('first_dropdown', 'value')]

)



def update_images(category):

    if category:

        filtered_df = df_data_merged[df_data_merged['category'] == category]

        return [
            dbc.Col(
                [
                    html.Img(src=row['image'], className='img-fluid'),
                    html.Div(row['productName'][:40],  style={'text-align': 'center', 'background-color': 'white'}),
                    html.Div(row['price'],  style={'text-align': 'center', 'background-color': 'white'}),
                    dbc.Button("Shop", href=row['link'], color="secondary", id="bouton_shop", 
                               style={
                            'text-align': 'center',
                            'background-color': '#d3d3d3',  # Light gray color
                            'color': 'black',  # Text color
                            'border': '2px solid black',  # Border
                            'padding': '10px 20px',  # Padding
                            'border-radius': '5px',  # Border radius
                        }),
                    dbc.Button("J'ajoute",
                        style={
                            'text-align': 'center',
                            'background-color': 'white',
                            'color': 'black',  # Text color
                            'border': '2px solid black',  # Border
                            'padding': '10px 20px',  # Padding
                            'border-radius': '5px',  # Border radius
                            'margin': '5px',  # Margin
                            }
                    ),
                    html.Hr()
                ],
                width={"size": 2},
            )
            for _, row in filtered_df.iterrows()
        ]

    else:

        return ''
    # [

        #     dbc.Col(html.Img(src=row['image'], className='img-fluid'), width={"size": 2})

        #     for _, row in df.iterrows()

        # ]
    





###################################################################### p.3

@app.callback(
    Output('dropdown_type', 'options'),
    [Input('radioitems_moment', 'value')]
)
def matin_soir(moment):
    if moment == 1:
        return  [{'label': i, 'value': i} for i in df_palette['style'].unique()]
    
    elif moment == 2:
        return [{'label': i, 'value': i} for i in df['type_peau'].dropna().unique()]
    
    
    ##########"
@app.callback(
    Output(component_id='rouge_a_levre_name', component_property='children'),
    Output(component_id='rouge_a_levre_img', component_property='src'),
    Output(component_id='rouge_a_levre_img', component_property='width'),
    Output(component_id='rouge_a_levre_img', component_property='height'),
    Output(component_id='fard_paupiere_name', component_property='children'),
    Output(component_id='fard_paupiere_img', component_property='src'),
    Output(component_id='fard_paupiere_img', component_property='width'),
    Output(component_id='fard_paupiere_img', component_property='height'),
    Output(component_id='fond_teint_name', component_property='children'),
    Output(component_id='fond_teint_img', component_property='src'),
    Output(component_id='fond_teint_img', component_property='width'),
    Output(component_id='fond_teint_img', component_property='height'),
    Input(component_id='dropdown_type', component_property='value')
)
def resultat_ML(valeur):
    if valeur in df_palette['style'].unique() :
        couleur_de_peau = '(117, 71, 54)'
        # ROUGE A LEVRE
        df_levre = df[df['category'] == 'levres']
        couleur_levre = df_palette[(df_palette['couleur_peau'] == couleur_de_peau)&(df_palette['style'] == valeur)]['C1'].values[0]
        couleur_levre_tri = [int(x) for x in couleur_levre.replace('(','').replace(')','').split(',')]
        # ML
        X = df_levre[['R','G','B']]
        KNN = NearestNeighbors(n_neighbors=1).fit(X)
        rouge_levre = KNN.kneighbors([couleur_levre_tri])
        rouge_a_levre_name = df_levre.iloc[rouge_levre[1][0][0]]['productName']
        rouge_a_levre_img = df_levre.iloc[rouge_levre[1][0][0]]['image']    
        # FARD A PAUPIERE
        df_fard = df[df['category'] == 'fard-a-paupieres-palette']
        couleur_fard = df_palette[(df_palette['couleur_peau'] == couleur_de_peau)&(df_palette['style'] == valeur)]['C2'].values[0]
        couleur_fard_tri = [int(x) for x in couleur_fard.replace('(','').replace(')','').split(',')]
        # ML
        X = df_fard[['R','G','B']]
        KNN = NearestNeighbors(n_neighbors=1).fit(X)
        rouge_levre = KNN.kneighbors([list(couleur_fard_tri)])
        fard_paupiere_name = df_fard.iloc[rouge_levre[1][0][0]]['productName']
        fard_paupiere_img = df_fard.iloc[rouge_levre[1][0][0]]['image']    # FOND DE TEINT
        df_fond_teint = df[df['category'] == 'teint']
        fond_teint_name = df_fond_teint[df_fond_teint['RGB'] == str(couleur_de_peau)].iloc[0]['productName']
        fond_teint_img = df_fond_teint[df_fond_teint['RGB'] == str(couleur_de_peau)].iloc[0]['image']
        width = '400'
        height = '400'    
        return rouge_a_levre_name, rouge_a_levre_img, width, height, fard_paupiere_name, fard_paupiere_img, width, height, fond_teint_name, fond_teint_img, width, height
    else:
        return '','','','','','','','','','','',''
@app.callback(
    Output(component_id='skin_care_name', component_property='children'),
    Output(component_id='skin_care_img', component_property='src'),
    Output(component_id='skin_care_img', component_property='width'),
    Output(component_id='skin_care_img', component_property='height'),
    Input(component_id='dropdown_type', component_property='value')
)
def update_skin_care(value):
    if value in df['type_peau'].dropna().unique() :
        choix_peau = value
        df_demaquillant = df[df['category'] == 'nettoyant-demaquillant']
        df_soin = df[df['category'] == 'soin-de-nuit']
        # DEMAQUILLANT 'peau_sensible', 'peau_seche', 'peau_mixte_a_grasse'
        if choix_peau in list(df[df['category'] == 'nettoyant-demaquillant']['type_peau'].unique()):
            demaquillant_name = df_demaquillant[df_demaquillant['type_peau'] == choix_peau].iloc[0]['productName']
            demaquillant_img = df_demaquillant[df_demaquillant['type_peau'] == choix_peau].iloc[0]['image']
            return demaquillant_name, demaquillant_img, '400', '400'
        # SKIN CARE ['anti_age', 'hydratation']
        if choix_peau in list(df[df['category'] == 'soin-de-nuit']['type_peau'].unique()):
            soin_name = df_soin[df_soin['type_peau'] == choix_peau].iloc[0]['productName']
            soin_img = df_soin[df_soin['type_peau'] == choix_peau].iloc[0]['image']
            return soin_name, soin_img, '400', '400'
    else:
        return '','','',''
    


######################################""
    


if __name__ == "__main__":
    app.run_server(debug=True, port=8086)