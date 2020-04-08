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
                                    {'label': 'Building 1', 'value': 'SiteID_1'},
                                    {'label': 'Building 2', 'value': 'SiteID_2'},
                                    {'label': 'Building 3', 'value': 'SiteID_3'},
                                    {'label': 'Building 4', 'value': 'SiteID_4'},
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
    if (demo_dropdown == "SiteID_1" and meter_type == "All" ):
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
                        html.Img(src = app.get_asset_url ('test.png'), height=460,width=1200),
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
                        html.Img(src = app.get_asset_url ('site15_hotwater.png'), height=460,width=1200),
                        ])
                    ],
            ))
    else:
        return ()
if __name__ == '__main__':
    app.run_server(debug=True, port=8054)