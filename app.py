import dash
import dash_table
from dash.dependencies import Output,State
from dash.dependencies import Input
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import requests
import pandas.io.sql as psql
import random
import plotly.graph_objs as go
from collections import deque
import datetime as dt
#import plotly.express as px
import plotly
import dash_bootstrap_components as dbc
import app
import datetime
from datetime import datetime as dt
import dash_daq as daq
import flask
import base64

# Define the app
app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
)
server = app.server
app.config.suppress_callback_exceptions = True

#Dashboard Title
def build_banner():
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H4("American Society of Heating, Refrigeration, and Air Conditioning Engineers"),
                    html.H6("Energy usage dashboard"),
                ],style={"color": '#FFFFFF',}
            ),
            html.Div(
                id="banner-logo",
                children=[
                    html.Button(
                        id="learn-more-button", children="LEARN MORE", n_clicks=0
                    )
                ],
            ),
        ],
    )

def build_tabs():
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="tab2",
                className="custom-tabs",
                children=[
                    dcc.Tab(
                        id="Specs-tab",
                        label="Register Site",
                        value="tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Control-chart-tab",
                        label="Consumption prediction",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],style={"color": '#FFFFFF',}
            )
        ],
    )

# test_png = 'test.png'
# test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')
def build_tab_2():
    return html.Div(
        id="quick-inputs",
        className="column",
        children=[
            html.Div(
                id="quick-inputs1",
                className="graph__container first",
                children=[
                    html.Div(
                        id='card-2',
                        children=[
                            html.P("Real Estate",style={"color": '#FFFFFF','textAlign': 'left','paddingLeft':20,'paddingTop':20, 'marginTop':20, 'marginBottom':20}),
                            dcc.Dropdown(
                                id='demo-dropdown',
                                options=[
                                    {'label': 'Building 0', 'value': 'SiteID_0'},
                                    {'label': 'Building 1', 'value': 'SiteID_1'},
                                    {'label': 'Building 2', 'value': 'SiteID_2'},
                                    {'label': 'Building 3', 'value': 'SiteID_3'},
                                    {'label': 'Building 4', 'value': 'SiteID_4'},
                                    {'label': 'Building 5', 'value': 'SiteID_5'},
                                    {'label': 'Building 6', 'value': 'SiteID_6'},
                                    {'label': 'Building 7', 'value': 'SiteID_7'},
                                    {'label': 'Building 8', 'value': 'SiteID_8'},
                                    {'label': 'Building 9', 'value': 'SiteID_9'},
                                    {'label': 'Building 10', 'value': 'SiteID_10'},
                                    {'label': 'Building 11', 'value': 'SiteID_11'},
                                    {'label': 'Building 12', 'value': 'SiteID_12'},
                                    {'label': 'Building 13', 'value': 'SiteID_13'},
                                    {'label': 'Building 14', 'value': 'SiteID_14'},
                                    {'label': 'Building 15', 'value': 'SiteID_15'},
                                ],
                                
                                style={'width': '95%', 'textAlign': 'start','color':"#1e2130", "paddingLeft":20}
                            ),
                            # dcc.Input(id='Input',type="number",style={'width': '95%', 'textAlign': 'center','background': "#1e2130",'color':"#92e0d3"})

                        ]
                    ),
                    html.Br(),
                    html.Div(
                        id='card-2',
                        children=[
                            html.P("Meter Type",style={"color": '#FFFFFF','textAlign': 'left',"paddingLeft":20}),
                            dcc.RadioItems(
                                id="meter-type",
                                options=[
                                {'label': 'Electricity', 'value': 'Electricity'},
                                {'label': 'Chilled Water', 'value': 'Chilled Water'},
                                {'label': 'Steam', 'value': 'Steam'},
                                {'label': 'Hot Water', 'value': 'Hot Water'},
                                {'label': 'All', 'value': 'All'}
                            ],
                            labelStyle={'display': 'inline-block'},
                            style={"color": '#FFFFFF','textAlign': 'left',"paddingLeft":20}
                        ),
                        html.Br() 

                        ]
                    ),

                ]
            ),
            html.Br(),
            html.Div(id="my-graph")

        ]
    )

def build_tab_1():
    return html.Div(
        id="quick-stats",
        className="seven column wind__speed__container",
        children=[
            html.Div(
                id="content__tab1",
                className=" column content__tab1",
                children=[
                    html.Div(
                        id="card-1",
                        children=[
                            html.P("Name of the Organization",style={"color": '#FFFFFF','textAlign': 'left', "paddingTop":20}),
                            #html.P("Start Date",style={"color": '#FFFFFF','textAlign': 'left'}),
                            dcc.Input(
                                        id="company-name",
                                        type="text",
                                        placeholder="name",
                                        style={"color": '#FFFFFF','textAlign': 'left'}

                                    )
                        ],
                    ),
                    html.Br(),
                    html.Div(
                        id="card-2",
                        children=[
                            html.P("Line of Business/ Primary Use",style={"color": '#FFFFFF','textAlign': 'left'}),
                            #html.P("End Date",st,yle={"color": '#FFFFFF','textAlign': 'left'}),
                            dcc.Dropdown(
                                id='demo-dropdown',
                                options=[
                                    {'label': 'Education', 'value': 'Education'},
                                    {'label': 'Engineering', 'value': 'SiteID_2'},
                                    {'label': 'Building 3', 'value': 'SiteID_3'},
                                    {'label': 'Building 4', 'value': 'SiteID_4'},
                                ],
                                
                                style={'width': '95%', 'textAlign': 'left','color':"#1e2130", "width":200}
                            ),
                        ],
                    ),
                    html.Br(),
                    html.Div(
                        id='card-3',
                        children=[
                            html.P("Square Feet",style={"color": '#FFFFFF','textAlign': 'left'}),
                            dcc.Input(
                                id="square-feet",
                                type="number",
                                placeholder="square feet",
                            )
                        ]
                    ),
                    html.Br(),
                    html.Div(
                        id='card-4',
                        children=[
                            html.P("Floor Count",style={"color": '#FFFFFF','textAlign': 'left'}),
                            dcc.Input(
                                id="floor-count",
                                type="number",
                                placeholder="floor count",
                            )

                        ]
                    ),
                    html.Br(),
                    html.Div(
                        id="utility-card1",
                        children=[
                            #html.P("Convert",style={"color": '#FFFFFF','textAlign': 'left'}),
                            html.Button("Go",id="button",n_clicks=0,style={'width': '16.5%', 'textAlign': 'center',"color": '#FFFFFF', "backgroundColor":"#E74C3C"})]
                        #, style={'width': '90%', 'textAlign': 'center'}
                    ),
                    html.Br(),
                    html.Div(
                        id="card-5 P",
                        children=[html.P(id="currency_converted",style={"color": '#FFFFFF','textAlign': 'left'})]
                        #html.H2(id="total-rides-selection"),
                        #html.H1(id="date-value"),],style={"text-align": "center",'padding': 40,'color':app_colors['text']}
                    )

                ]),
        ],
    )



@app.callback(
    [Output("app-content", "children"), Output("interval-component", "n_intervals")],
    [Input("app-tabs", "value")],
    [State("n-interval-stage", "data")],
)
def render_tab_content(tab_switch, stopped_interval):
    if tab_switch == "tab1":
        return html.Div(id="status-container1",
                        children=[
                            html.Br(),
                            build_tab_1(),
                                #   html.Div(
                                #       id="graphs-container1",
                                #       children=[build_top_panel_tab1(stopped_interval)]
                                #   )
                                  ]), stopped_interval
    return (
        html.Div(
            id="status-container",
            children=[
                build_tab_2(),
            ],
        ),
        stopped_interval,
    )
    #Markdown for Learn more

def generate_modal():
    return html.Div(
        id="markdown",
        className="modal",
        children=(
            html.Div(
                id="markdown-container",
                className="markdown-container",
                children=[
                    html.Div(
                        className="close-container",
                        children=html.Button(
                            "Close",
                            id="markdown_close",
                            n_clicks=0,
                            className="closeButton",
                        ),
                    ),
                    html.Div(
                        className="markdown-text",
                        children=dcc.Markdown(
                            children=(
                                """
                        ###### What is this mock app about?
                        This is a dashboard for
                        ###### What does this app shows
                    """
                            )
                        ),
                    ),
                ],
            )
        ),
    )

app.layout = html.Div(
    id="big-app-container",
    children=[
        build_banner(),
        dcc.Interval(
            id="interval-component",
            interval=2 * 1000,  # in milliseconds
            n_intervals=50,  # start at batch 50
            disabled=True,
        ),
        html.Div(
            id="app-container",
            children=[
                build_tabs(),
                # Main app
                html.Div(id="app-content"),
            ],
        ),
        dcc.Store(id="value-setter-store"),
        dcc.Store(id="n-interval-stage", data=50),
        generate_modal(),
    ],)

@app.callback(
    dash.dependencies.Output('my-graph', 'children'),
     [dash.dependencies.Input('demo-dropdown', 'value'),
     dash.dependencies.Input('meter-type', 'value'),],
    [dash.dependencies.State('demo-dropdown', 'value'),
    dash.dependencies.State('meter-type', 'value'),]
)
def graph_display(demo_dropdown,meter_type,a,b):
    if (demo_dropdown == "SiteID_0" and meter_type == "All" ):
        return (
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_0_All.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_0" and meter_type == "Hot Water" ):
        return(
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_0_Hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_0" and meter_type == "Chilled Water" ):
        return (html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_0_Chilledwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_0" and meter_type == "Steam" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_0_Steam.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_0" and meter_type == "Electricity" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_0_Electric.png'), height=460,width=1200),
                        ])
                    ],
            ))

    elif (demo_dropdown == "SiteID_1" and meter_type == "All" ):
        return (
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_1_All.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_1" and meter_type == "Hot Water" ):
        return(
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_1_Hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_1" and meter_type == "Chilled Water" ):
        return (html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_1_Chilledwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_1" and meter_type == "Steam" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_1_Steam.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_1" and meter_type == "Electricity" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_1_Electric.png'), height=460,width=1200),
                        ])
                    ],
            ))

    
    elif (demo_dropdown == "SiteID_2" and meter_type == "All" ):
        return (
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_2_All.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_2" and meter_type == "Hot Water" ):
        return(
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_2_Hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_2" and meter_type == "Chilled Water" ):
        return (html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_2_Chilledwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_2" and meter_type == "Steam" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_2_Steam.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_2" and meter_type == "Electricity" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_2_Electric.png'), height=460,width=1200),
                        ])
                    ],
            ))

    elif (demo_dropdown == "SiteID_3" and meter_type == "All" ):
            return (
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_3_All.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_3" and meter_type == "Hot Water" ):
        return(
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_3_Hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_3" and meter_type == "Chilled Water" ):
        return (html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_3_Chilledwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_3" and meter_type == "Steam" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_3_Steam.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_3" and meter_type == "Electricity" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_3_Electric.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_4" and meter_type == "All" ):
            return (
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_4_All.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_4" and meter_type == "Hot Water" ):
        return(
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_4_Hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_4" and meter_type == "Chilled Water" ):
        return (html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_4_Chilledwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_4" and meter_type == "Steam" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_4_Steam.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_4" and meter_type == "Electricity" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_4_Electric.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_5" and meter_type == "All" ):
            return (
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_5_All.png'), height=460,width=1200),
                        ])
                    ],
            ))
        
    elif (demo_dropdown == "SiteID_5" and meter_type == "Hot Water" ):
            return(
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_5_Hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_5" and meter_type == "Chilled Water" ):
        return (html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_5_Chilledwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_5" and meter_type == "Steam" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_5_Steam.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_5" and meter_type == "Electricity" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_5_Electric.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_6" and meter_type == "All" ):
            return (
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_6_All.png'), height=460,width=1200),
                        ])
                    ],
            ))
        
    elif (demo_dropdown == "SiteID_6" and meter_type == "Hot Water" ):
            return(
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_6_Hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_6" and meter_type == "Chilled Water" ):
        return (html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_6_Chilledwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_6" and meter_type == "Steam" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_6_Steam.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_6" and meter_type == "Electricity" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_6_Electric.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_7" and meter_type == "All" ):
            return (
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_7_All.png'), height=460,width=1200),
                        ])
                    ],
            ))
        
    elif (demo_dropdown == "SiteID_7" and meter_type == "Hot Water" ):
            return(
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_7_Hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_7" and meter_type == "Chilled Water" ):
        return (html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_7_Chilledwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_7" and meter_type == "Steam" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_7_Steam.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_7" and meter_type == "Electricity" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_7_Electric.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_8" and meter_type == "All" ):
                return (
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_8_All.png'), height=460,width=1200),
                        ])
                    ],
            ))
        
    elif (demo_dropdown == "SiteID_8" and meter_type == "Hot Water" ):
            return(
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_8_Hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_8" and meter_type == "Chilled Water" ):
        return (html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_8_Chilledwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_8" and meter_type == "Steam" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_8_Steam.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_8" and meter_type == "Electricity" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_8_Electric.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_9" and meter_type == "All" ):
            return (
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_9_All.png'), height=460,width=1200),
                        ])
                    ],
            ))
        
    elif (demo_dropdown == "SiteID_9" and meter_type == "Hot Water" ):
            return(
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_9_Hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_9" and meter_type == "Chilled Water" ):
        return (html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_9_Chilledwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_9" and meter_type == "Steam" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_9_Steam.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_9" and meter_type == "Electricity" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_9_Electric.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_10" and meter_type == "All" ):
            return (
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_10_All.png'), height=460,width=1200),
                        ])
                    ],
            ))
        
    elif (demo_dropdown == "SiteID_10" and meter_type == "Hot Water" ):
            return(
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_10_Hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_10" and meter_type == "Chilled Water" ):
        return (html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_10_Chilledwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_10" and meter_type == "Steam" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_10_Steam.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_10" and meter_type == "Electricity" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_10_Electric.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_11" and meter_type == "All" ):
            return (
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_11_All.png'), height=460,width=1200),
                        ])
                    ],
            ))
        
    elif (demo_dropdown == "SiteID_11" and meter_type == "Hot Water" ):
            return(
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_11_Hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_11" and meter_type == "Chilled Water" ):
        return (html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_11_Chilledwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_11" and meter_type == "Steam" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_11_Steam.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_11" and meter_type == "Electricity" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_11_Electric.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_12" and meter_type == "All" ):
            return (
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_12_All.png'), height=460,width=1200),
                        ])
                    ],
            ))
        
    elif (demo_dropdown == "SiteID_12" and meter_type == "Hot Water" ):
            return(
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_12_Hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_12" and meter_type == "Chilled Water" ):
        return (html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_12_Chilledwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_12" and meter_type == "Steam" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_12_Steam.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_12" and meter_type == "Electricity" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_12_Electric.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_13" and meter_type == "All" ):
            return (
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_13_All.png'), height=460,width=1200),
                        ])
                    ],
            ))
        
    elif (demo_dropdown == "SiteID_13" and meter_type == "Hot Water" ):
            return(
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_13_Hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_13" and meter_type == "Chilled Water" ):
        return (html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_13_Chilledwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_13" and meter_type == "Steam" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_13_Steam.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_13" and meter_type == "Electricity" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_13_Electric.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_14" and meter_type == "All" ):
            return (
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_14_All.png'), height=460,width=1200),
                        ])
                    ],
            ))
        
    elif (demo_dropdown == "SiteID_14" and meter_type == "Hot Water" ):
            return(
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_14_Hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_14" and meter_type == "Chilled Water" ):
        return (html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_14_Chilledwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_14" and meter_type == "Steam" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_14_Steam.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_14" and meter_type == "Electricity" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_14_Electric.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_15" and meter_type == "All" ):
            return (
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_15_All.png'), height=460,width=1200),
                        ])
                    ],
            ))
        
    elif (demo_dropdown == "SiteID_15" and meter_type == "Hot Water" ):
            return(
                html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_15_Hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_15" and meter_type == "Chilled Water" ):
        return (html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_15_Chilledwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_15" and meter_type == "Steam" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_15_Steam.png'), height=460,width=1200),
                        ])
                    ],
            ))
    elif (demo_dropdown == "SiteID_15" and meter_type == "Electricity" ):
        return(html.Div(
                id="top-section-container",
                className="wind__speed__container",
                children=[
                    html.Div([
                        html.Div(
                            [html.H2("ENERGY CONSUMPTION", className="graph__title")]
                        ),
                        html.Br(),
                        html.Img(src = app.get_asset_url ('Split_ID_15_Electric.png'), height=460,width=1200),
                        ])
                    ],
            ))

    
    else:
        return ()
if __name__ == '__main__':
    app.run_server(debug=True, port=8054)