"""SpaceX Falcon 9 launch dashboard — derived from the supplied, executed IBM lab.

This historical educational dataset is provided by IBM Skills Network.
Install dependencies inside your selected Python environment:
    pip install pandas dash plotly
Then run this script or the corresponding JupyterLab notebook.
"""
from pathlib import Path

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

CSV_FILE = Path(__file__).with_name('spacex_launch_dash.csv')
IBM_URL = (
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/'
    'IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv'
)
spacex_df = pd.read_csv(CSV_FILE if CSV_FILE.exists() else IBM_URL)
required = {'Launch Site', 'class', 'Payload Mass (kg)', 'Booster Version Category'}
missing = required - set(spacex_df.columns)
if missing:
    raise ValueError(f'Dataset is missing required columns: {sorted(missing)}')
spacex_df['class'] = pd.to_numeric(spacex_df['class'])
spacex_df['Payload Mass (kg)'] = pd.to_numeric(spacex_df['Payload Mass (kg)'])
spacex_df = spacex_df.dropna(subset=list(required)).copy()

sites = sorted(spacex_df['Launch Site'].unique())
site_options = [{'label': 'All Sites', 'value': 'ALL'}] + [
    {'label': site, 'value': site} for site in sites
]
app = Dash(__name__)
app.title = 'SpaceX Launch Records Dashboard | IBM Capstone'
app.layout = html.Div([
    html.H1('SpaceX Launch Records Dashboard', style={'textAlign': 'center'}),
    html.P('IBM Capstone · historical data; class = 1 means a successful first-stage landing',
           style={'textAlign': 'center'}),
    html.Label('Select launch site'),
    dcc.Dropdown(id='site-dropdown', options=site_options, value='ALL', searchable=True),
    dcc.Graph(id='success-pie-chart'),
    html.Label('Select payload mass range (kg)'),
    dcc.RangeSlider(id='payload-slider', min=0, max=10000, step=1000,
                    value=[0,10000], marks={i:str(i) for i in range(0,10001,2000)}),
    dcc.Graph(id='success-payload-scatter-chart'),
], style={'maxWidth':'1100px','margin':'auto','fontFamily':'Arial, sans-serif',
          'padding':'30px','backgroundColor':'white'})


@app.callback(Output('success-pie-chart','figure'), Input('site-dropdown','value'))
def get_pie_chart(selected_site):
    if selected_site == 'ALL':
        success = spacex_df.loc[spacex_df['class'] == 1].groupby('Launch Site').size()
        counts = success.rename('Successful landings').reset_index()
        return px.pie(counts, values='Successful landings', names='Launch Site',
                      title='Successful first-stage landings by launch site')
    filtered = spacex_df.loc[spacex_df['Launch Site'] == selected_site]
    counts = filtered['class'].value_counts().reindex([0,1],fill_value=0)
    counts = counts.rename_axis('class').reset_index(name='Count')
    counts['Outcome'] = counts['class'].map({0:'Other / failed',1:'Successful landing'})
    return px.pie(counts, values='Count', names='Outcome',
                  title=f'Landing outcomes: {selected_site}',
                  color='Outcome',color_discrete_map={'Successful landing':'#269e71',
                                                     'Other / failed':'#d75b5b'})


@app.callback(Output('success-payload-scatter-chart','figure'),
              Input('site-dropdown','value'), Input('payload-slider','value'))
def get_scatter_chart(selected_site,payload_range):
    lo,hi = payload_range
    frame = spacex_df[spacex_df['Payload Mass (kg)'].between(lo,hi,inclusive='both')]
    if selected_site != 'ALL':
        frame = frame[frame['Launch Site'] == selected_site]
    fig=px.scatter(frame,x='Payload Mass (kg)',y='class',
                   color='Booster Version Category',hover_data=['Launch Site'],
                   title='Payload and first-stage landing outcome',
                   labels={'class':'Landing outcome (0=no, 1=yes)'})
    fig.update_yaxes(tickmode='array',tickvals=[0,1],range=[-.2,1.2])
    return fig


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8050, debug=False)
