"""
For Plolty dash.

run with: $ python3 app.py

$ mkdir viz; dc viz
$ git clone https://github.com/lineality/plotly_dash_geomap_points_energy1.git
$ cd plotly_dash_geomap_points_energy1

Note:
May need requirements.txt with package versions removed
because that will install all newest versions.

# Use a python environment

# Recommended Process: First Time Setup
```
    $ python3 -m venv env; source env/bin/activate
    (ENV)$ python3 -m pip install --upgrade pip
    (ENV)$ python3 -m pip install git+https://github.com/psf/black
    (ENV)$ python3 -m pip install pylint pydocstyle flake8
    (ENV)$ pip install -r requirements.txt
```

# Run:
```
    (ENV)$ python3 app.py
```
Open in browser: http://127.0.0.1:8050

Press CTRL+C to quit (terminal server)

# Subsiquent cold-start run:
```
    $ source env/bin/activate; python3 app.py
```
"""

# import libraries
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)

# Create Dash App
app = dash.Dash()

# load data
df = pd.read_csv("US_Alt_Fuel_Stations_03_17_2022.csv", low_memory=False)


#########################
# Pick Hover Over Labels
#########################

hover_over_labels = {
    "Fuel Type Code": True,
    "Station Name": True,
    "Street Address": True,
    #             'Intersection Directions' : True,
    #             'City' : True,
    #             'State' : True,
    #             'ZIP' : True,
    #             'Plus4' : True,
    #             'Station Phone' : True,
    #             'Status Code' : True,
    "Expected Date": True,
    #             'Groups With Access Code' : True,
    #             'Access Days Time' : True,
    #             'Cards Accepted' : True,
    #             'BD Blends' : True,
    #             'NG Fill Type Code' : True,
    #             'NG PSI' : True,
    "EV Level1 EVSE Num": True,
    "EV Level2 EVSE Num": True,
    "EV DC Fast Count": True,
    "EV Other Info": True,
    "EV Network": True,
    "EV Network Web": True,
    #             'Geocode Status' : True,
    "Latitude": True,
    "Longitude": True,
    #             'Date Last Confirmed' : True,
    #             'ID' : True,
    #             'Updated At' : True,
    #             'Owner Type Code' : True,
    #             'Federal Agency ID' : True,
    #             'Federal Agency Name' : True,
    #             'Open Date' : True,
    #             'Hydrogen Status Link' : True,
    #             'NG Vehicle Class' : True,
    #             'LPG Primary' : True,
    #             'E85 Blender Pump' : True,
    "EV Connector Types": True,
    #             'Country' : True,
    #             'Intersection Directions (French)' : True,
    #             'Access Days Time (French)' : True,
    #             'BD Blends (French)' : True,
    #             'Groups With Access Code (French)' : True,
    #             'Hydrogen Is Retail' : True,
    #             'Access Code' : True,
    #             'Access Detail Code' : True,
    #             'Federal Agency Code' : True,
    #             'Facility Type' : True,
    #             'CNG Dispenser Num' : True,
    #             'CNG On-Site Renewable Source' : True,
    #             'CNG Total Compression Capacity' : True,
    #             'CNG Storage Capacity' : True,
    #             'LNG On-Site Renewable Source' : True,
    #             'E85 Other Ethanol Blends' : True,
    "EV Pricing": True,
    #             'EV Pricing (French)' : True,
    #             'LPG Nozzle Types' : True,
    #             'Hydrogen Pressures' : True,
    #             'Hydrogen Standards' : True,
    #             'CNG Fill Type Code' : True,
    #             'CNG PSI' : True,
    #             'CNG Vehicle Class' : True,
    #             'LNG Vehicle Class' : True,
    "EV On-Site Renewable Source": True,
    "Restricted Access": True,
}


#######################
# Graph Plot Deploy !!
#######################

MAP_HEIGHT = 800

app.layout = html.Div(
    [
        dcc.Graph(
            figure=px.scatter_mapbox(
                df,
                mapbox_style="open-street-map",
                lat="Latitude",
                lon="Longitude",
                hover_data=hover_over_labels,
                color_discrete_sequence=["fuchsia"],
                zoom=3,
                template="plotly_dark",
                height=MAP_HEIGHT,
            )
        )
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
