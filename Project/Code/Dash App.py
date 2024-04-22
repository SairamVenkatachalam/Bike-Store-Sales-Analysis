#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import matplotlib.font_manager as fm
title_font = fm.FontProperties(family='serif', size=16, weight='bold')
label_font = fm.FontProperties(family='serif', size=14)
title_color = 'blue'
label_color = 'darkred'
colormap='Set2'
#%%

# filepath="C:/Users/saira/OneDrive/Desktop/GWU Courses/Semester 2/Data Visualization/Project/Data/European Bike Sales.csv"
filepath='Bikes_Filtered.csv'
bikes=pd.read_csv(filepath)
print(bikes.head(10))

#%%

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

filepath='Bikes_Filtered.csv'
bikes=pd.read_csv(filepath)
# print(bikes.head(10))
numerical_cols = ['Customer_Age', 'Order_Quantity','Profit', 'Cost', 'Revenue']

bikes['Date']=pd.to_datetime(bikes['Date'], format='%d-%m-%Y')


# Create the Dash app
app = dash.Dash('My_App')

# Define the app layout
# Define the app layout
app.layout = html.Div([
    html.H1("Bikes Data Visualization"),
    dcc.Tabs([
        dcc.Tab(label='Country-wise Metrics Over Time', children=[
            html.Div([
                html.Label("Select a metric:"),
                dcc.Dropdown(
                    id='metric-dropdown',
                    options=[
                        {'label': 'Revenue', 'value': 'Revenue'},
                        {'label': 'Quantity', 'value': 'Order_Quantity'},
                        {'label': 'Profit', 'value': 'Profit'}
                    ],
                    value='Revenue'
                ),
                html.Label("Select a country:"),
                dcc.Dropdown(
                    id='country-dropdown',
                    options=[
                        {'label': country, 'value': country} for country in bikes['Country'].unique()
                    ],
                    value='Canada'
                ),
                dcc.Graph(id='country-metrics-graph'),
                html.Div([
                    dcc.Graph(id='animated-bar-bubble-chart')
                ])
            ])
        ]),
        dcc.Tab(label='Customer Segments', children=[
            html.Div([
                html.Label("Select a metric:"),
                dcc.Dropdown(
                    id='segment-metric-dropdown',
                    options=[
                        {'label': 'Revenue', 'value': 'Revenue'},
                        {'label': 'Quantity', 'value': 'Quantity'},
                        {'label': 'Profit', 'value': 'Profit'}
                    ],
                    value='Revenue'
                ),
                dcc.Graph(id='customer-segments-pie-chart')
            ])
        ]),

        dcc.Tab(label='Product Analysis', children=[
            html.Div([
                html.Label("Select a Product Category:"),
                dcc.Dropdown(
                    id='product-category-dropdown',
                    options=[{'label': category, 'value': category} for category in bikes['Sub_Category'].unique()],
                    value='Tires and Tubes'  # Default value is the first category
                ),
                html.Label("Select a Date:"),
                dcc.Slider(
                    id='date-slider',
                    min=0,
                    max=len(bikes['Date'].unique()) - 1,
                    step=1,
                    marks={i: date.strftime('%b %Y') for i, date in enumerate(sorted(bikes['Date'].unique())) if
                           i % 30 == 0},
                    value=len(bikes['Date'].unique()) - 1  # Default value is the last date
                ),
                html.Div([
                    dcc.Graph(id='country-wise-revenue-bar-chart', style={'width': '50%', 'display': 'inline-block'}),
                    dcc.Graph(id='age-group-pie-chart', style={'width': '50%', 'display': 'inline-block'}),
                ]),
                html.Div([
                    dcc.Graph(id='gender-pie-chart', style={'width': '50%', 'display': 'inline-block'}),
                    # Add another empty div to fill the remaining space
                    html.Div(style={'width': '50%', 'display': 'inline-block'}),
                ]),
            ])
        ]),

        dcc.Tab(label='Country and State Analysis', children=[
            html.Div([
                html.Label("Select a Metric:"),
                dcc.Dropdown(
                    id='metric-dropdown2',
                    options=[
                        {'label': 'Revenue', 'value': 'Revenue'},
                        {'label': 'Profit', 'value': 'Profit'}
                    ],
                    value='Profit'  # Default value is 'Profit'
                ),
                dcc.Graph(id='country-state-map')
            ])
        ]),


    ])
])

@app.callback(
    Output('country-metrics-graph', 'figure'),
    Input('metric-dropdown', 'value'),
    Input('country-dropdown', 'value')
)
def update_country_metrics_graph(metric, country):
    filtered_data = bikes[bikes['Country'] == country]
    filtered_data=bikes.copy()
    summed_data = filtered_data.groupby(['Year','Country'])[numerical_cols].sum().reset_index()


    # Plot the data
    fig1 = px.line(summed_data, x='Year', y=metric, title=f"Total {metric} in {country}",color='Country')
    # fig1.update_traces(line=dict(color='skyblue'))
    fig1.update_layout(title_font_family='serif', title_font_color='blue', title_font_size=20,
                      xaxis=dict(title='Year', title_font_family='serif',
                                 title_font_color='darkred', title_font_size=16),
                      yaxis=dict(title=metric, tickformat='.2f', title_font_family='serif', title_font_color='darkred',
                                 title_font_size=16))

    return fig1

@app.callback(
    Output('animated-bar-bubble-chart', 'figure'),
    Input('metric-dropdown', 'value')
)
def update_animated_bar_bubble_chart(metric):
    # Aggregate the data by Month and country
    agg_data = bikes.groupby(['Month', 'Country']).agg({'Revenue': 'sum', 'Order_Quantity': 'sum', 'Profit': 'sum'}).reset_index()

    # Plot the animated bar bubble chart
    fig = px.scatter(agg_data, x='Revenue', y='Order_Quantity', animation_frame='Month', size='Profit', color='Profit', hover_name='Country',
             labels={'Revenue': 'Revenue', 'Order_Quantity': 'Quantity', 'Profit': 'Profit'},
             title='Animated Bar Bubble Chart of Revenue and Quantity over Months by Country', color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_layout(xaxis_title='Revenue', yaxis_title='Quantity')
    return fig
# Define callback to update customer segments pie chart


# Tab 2 --------------------------------------------------

@app.callback(
    Output('customer-segments-pie-chart', 'figure'),
    Input('segment-metric-dropdown', 'value')
)
def update_customer_segments_pie_chart(metric):
    fig = px.pie(bikes, names='Customer_Segment', values=metric, title=f"{metric} by Customer Segment", color_discrete_sequence=px.colors.qualitative.Pastel)
    return fig



## Tab 3 -----------------------

@app.callback(
    Output('country-wise-revenue-bar-chart', 'figure'),
    Input('product-category-dropdown', 'value'),
    Input('date-slider', 'value')
)
def update_country_wise_revenue_bar_chart(selected_category, selected_date):
    filtered_data = bikes[(bikes['Sub_Category'] == selected_category) & (bikes['Date'] == sorted(bikes['Date'].unique())[selected_date])]
    country_revenue = filtered_data.groupby('Country')['Revenue'].sum().reset_index()
    country_revenue = country_revenue.sort_values(by='Revenue', ascending=False)  # Sort by revenue in descending order
    fig = px.bar(country_revenue, x='Country', y='Revenue',
                 title=f"Country-wise Revenue for {selected_category}",
                 color='Country', color_discrete_sequence=px.colors.qualitative.Pastel)

    return fig

@app.callback(
    Output('age-group-pie-chart', 'figure'),
    Input('product-category-dropdown', 'value'),
    Input('date-slider', 'value')
)
def update_age_group_pie_chart(selected_category, selected_date):
    filtered_data = bikes[(bikes['Sub_Category'] == selected_category) & (bikes['Date'] == sorted(bikes['Date'].unique())[selected_date])]
    age_group_counts = filtered_data['Age_Group'].value_counts().reset_index()
    age_group_counts.columns = ['Age_Group', 'Count']
    fig = px.pie(age_group_counts, names='Age_Group', values='Count', title=f"Age Group Distribution for {selected_category}",
                 color='Age_Group', color_discrete_sequence=px.colors.qualitative.Pastel)
    return fig

@app.callback(
    Output('gender-pie-chart', 'figure'),
    Input('product-category-dropdown', 'value'),
    Input('date-slider', 'value')
)
def update_gender_pie_chart(selected_category, selected_date):
    filtered_data = bikes[(bikes['Sub_Category'] == selected_category) & (bikes['Date'] == sorted(bikes['Date'].unique())[selected_date])]
    gender_counts = filtered_data['Customer_Gender'].value_counts().reset_index()
    gender_counts.columns = ['Customer_Gender', 'Count']
    fig = px.pie(gender_counts, names='Customer_Gender', values='Count', title=f"Gender Distribution for {selected_category}",
                 color='Customer_Gender', color_discrete_sequence=px.colors.qualitative.Pastel)
    return fig




## Tab 4 ----------------------------------------------------------------------

@app.callback(
    Output('country-state-map', 'figure'),
    Input('metric-dropdown2', 'value')
)
def update_country_state_map(metric):
    if metric not in ['Revenue', 'Profit']:
        raise ValueError("Invalid metric selected")

    bikes_small=bikes.head(100)
    fig = px.choropleth(
        bikes_small,
        locations='Country',
        locationmode='country names',
        color=metric,
        hover_name='Country',
        hover_data=['State', metric],
        title=f"{metric} by Country and State",
        color_continuous_scale='Viridis'
    )
    fig.update_geos(projection_type="natural earth")
    fig.update_layout(coloraxis_colorbar=dict(title=metric))
    return fig


app.server.run(debug=False,
                  port=8080,
                  host='0.0.0.0')


