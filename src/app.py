from dash import dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import epicmix
import dash_daq as daq
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

server = app.server

app.layout = dbc.Container(
    [
        # Cache
        dcc.Store(id="rider_data"),
        # Title and Subtitle
        html.Br(),
        html.H1("EpicStats", style={"textAlign": "center"}),
        html.P("Visualizing your Time on the Mountain", style={"textAlign": "center"}),
        html.Br(),
        # Log in block
        html.Div(
            [
                dbc.Row(
                    dbc.Col(
                        html.P("Please Login to EpicMix", style={"textAlign": "center"})
                    ),
                    justify="center",
                ),
                dbc.Row(
                    [
                        dbc.Col(html.P("Username:"), width=1),
                        dbc.Col(
                            dcc.Input(id="username", type="email", value=""), width=2
                        ),
                    ],
                    justify="center",
                ),
                dbc.Row(
                    [
                        dbc.Col(html.P("Password:"), width=1),
                        dbc.Col(
                            dcc.Input(id="password", type="password", value=""), width=2
                        ),
                    ],
                    justify="center",
                ),
                html.Div(id="login_status", style={"textAlign": "center"}),
                dbc.Row(
                    dbc.Col(
                        dbc.Col(
                            html.Button("Submit", id="submit-button", n_clicks=0),
                            width=2,
                            style={"margin": "auto", "width": "67px"},
                        )
                    ),
                    justify="center",
                ),
            ],
            style={"display": "block"},
            id="login_box",
        ),
        # THE APP ITSELF
        html.Div(
            [
                # The Graph and filter components
                html.Div(
                    [
                        dbc.Row(
                            [
                                # filters
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.P("Hi!"),
                                        html.Div(id="welcome_msg"),
                                        html.Br(),
                                        html.P("Filters:"),
                                        dbc.Row(
                                            [
                                                dbc.Col(html.P("Units:")),
                                                dbc.Col(html.Div(id="units_text")),
                                                dbc.Col(
                                                    daq.BooleanSwitch(
                                                        id="units-switch", on=False
                                                    ),
                                                    align="start",
                                                ),
                                            ]
                                        ),
                                        html.P("Season:"),
                                        dcc.Dropdown(
                                            options=[], value="", id="season_dropdown"
                                        ),
                                        html.Br(),
                                        html.P("Metric:"),
                                        dcc.Dropdown(
                                            options=["Vertical Distance", "Lifts"],
                                            value="Vertical Distance",
                                            id="metric",
                                        ),
                                        html.Br(),
                                        html.Button("Download CSV", id="download_btn"),
                                        dcc.Download(id="download_dataframe_csv"),
                                    ],
                                    width=3,
                                ),
                                # graph
                                dbc.Col(dcc.Graph(id="graph"), width=9),
                            ]
                        )
                    ]
                ),
            ],
            id="epic_stats_app",
        ),
    ]
)


@app.callback(
    Output("login_status", "children"),
    Output("login_box", component_property="style"),
    Output("epic_stats_app", component_property="style"),
    Output("rider_data", "data"),
    Output("season_dropdown", "options"),
    Output("season_dropdown", "value"),
    Output("welcome_msg", "children"),
    Input("submit-button", "n_clicks"),
    State("username", "value"),
    State("password", "value"),
)
def login(n_clicks, username, password):
    if n_clicks == 0:
        login_status = ""
        login_box = {"display": "block"}
        epic_stats_app = {"display": "none"}
        rider_data = {}
        season_dropdown_options = []
        seasons_dropdown_value = ""
        welcome_msg = ""
    else:
        try:
            rider = epicmix.EpicMix(username, password)
            login_status = "logged in"
            welcome_msg = "You are currently logged in as " + str(username)
            login_box = {"display": "none"}
            epic_stats_app = {"display": "block"}
            rider_data = {}
            rider_data["creds"] = rider.user_creds
            szn_stats = rider.get_season_stats()
            rider_data["seasons"] = {
                szn.seasonDisplayName: szn.seasonTagId for szn in szn_stats
            }
            season_dropdown_options = list(rider_data["seasons"].keys())
            seasons_dropdown_value = list(rider_data["seasons"].keys())[0]

        except epicmix.EpicError as error:
            login_status = error.description
            login_box = {"display": "block"}
            epic_stats_app = {"display": "none"}
            rider_data = {}
            season_dropdown_options = []
            seasons_dropdown_value = ""
            welcome_msg = ""

    return (
        login_status,
        login_box,
        epic_stats_app,
        rider_data,
        season_dropdown_options,
        seasons_dropdown_value,
        welcome_msg,
    )


@app.callback(Output("units_text", "children"), Input("units-switch", "on"))
def units(units):
    if units:
        return "Meters"
    else:
        return "Feet"


@app.callback(
    Output("graph", "figure"),
    Input("units-switch", "on"),
    Input("rider_data", "data"),
    Input("season_dropdown", "value"),
    Input("metric", "value"),
    prevent_initial_call=True,
)
def plot(units, rider_data, season, metric):
    if metric == "Vertical Distance":
        if units:
            y_metric = "verticalInMeters"
            ylab = "Vertical Distance (Meters)"
            title = "Vertical Distance vs Date <br>" + season
        else:
            y_metric = "verticalInFeet"
            ylab = "Vertical Distance (Feet)"
            title = "Vertical Distance vs Date <br>" + season
    else:
        y_metric = "liftRides"
        ylab = "Number of Lifts Ridden"
        title = "Number of Lifts Ridden vs Date <br>" + season

    if rider_data:
        rider = epicmix.EpicMix(
            rider_data["creds"]["username"], rider_data["creds"]["password"]
        )
        data = rider.get_daily_stats(rider_data["seasons"][season])
        data = pd.DataFrame(data)
        trace = go.Bar(
            x=data["createdTimestampUtc"],
            y=data[y_metric],
        )
        layout = go.Layout(
            title=title, xaxis=dict(title="Date"), yaxis=dict(title=ylab), height=600
        )
        fig = go.Figure(data=[trace], layout=layout)
    else:
        fig = {}
    return fig


@app.callback(
    Output("download_dataframe_csv", "data"),
    Input("download_btn", "n_clicks"),
    State("rider_data", "data"),
    State("season_dropdown", "value"),
    prevent_initial_call=True,
)
def func(n_clicks, rider_data, season):
    rider = epicmix.EpicMix(
        rider_data["creds"]["username"], rider_data["creds"]["password"]
    )
    data = rider.get_daily_stats(rider_data["seasons"][season])
    data = pd.DataFrame(data)

    return dcc.send_data_frame(
        data.to_csv, f"{rider_data['creds']['username']}-{season}.csv"
    )


if __name__ == "__main__":
    app.run_server(debug=True)
