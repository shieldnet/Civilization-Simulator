import dash
from dash.dependencies import Input, Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import datetime
from firebase import firebase
import plotly

app = dash.Dash()

app.scripts.config.serve_locally = True

firebase = firebase.FirebaseApplication('https://villiagesimulator.firebaseio.com', None)
vil1 = firebase.get('/Civilization1', None)
print(vil1)

vil2 = firebase.get('/Civilization2', None)
print(list(map(int,vil1.values())))
print(list(map(int,vil2.values())))

app.layout = html.Div([

    dcc.Interval(id='interval-component',interval=1*1000),
    dcc.Interval(id='interval-component2',interval=1*1000),
    html.H1(children='Village Simulator'),

     html.Div(children='''
         2017 OOP Project4 : Village Simulator
     '''),

    dcc.Graph(id = 'live-update-graph'),
    dcc.Graph(id = 'live-update-graph2')

], style={
    'width': '80%',
    'fontFamily': 'Sans-Serif',
    'margin-left': 'auto',
    'margin-right': 'auto'
})


@app.callback(Output('live-update-graph', 'figure'),events=[Event('interval-component', 'interval')])
def update_alldata_server2():
    vil1 = firebase.get('/Civilization1', None)
    vil2 = firebase.get('/Civilization2', None)
    figure = {'data': [
        {'x': list(vil1.keys()), 'y': list(map(int, vil1.values())), 'type': 'bar', 'name': 'Village1'},
        {'x': list(vil1.keys()), 'y': list(map(int, vil2.values())), 'type': 'bar', 'name': 'Village2'},

    ],

        'layout': {
            'title': 'All data on Village1,2'
        },
        'legend': {'x': 0, 'y': 1}
    }
    return figure


@app.callback(Output('live-update-graph2', 'figure'),events=[Event('interval-component2', 'interval')])
def update_alldata_server():
    vil1 = firebase.get('/Civilization1', None)
    vil2 = firebase.get('/Civilization2', None)
    figure2 = {'data': [
        {'labels': ['Civilization1-people', 'Civilization2-people'], 'values': [vil1['Civil1_NumPeople'],vil2['Civil2_NumPeople']], 'type': 'pie', 'name': 'Village'},

    ],

        'layout': {
            'title': 'population data on Village1,2'
        },
        'legend': dict(
         font=dict(color='#CCCCCC', size='10'),
         orientation='h',
         bgcolor='rgba(0,0,0,0)')
    }

    return figure2





if __name__ == '__main__':
    app.run_server(debug=True)