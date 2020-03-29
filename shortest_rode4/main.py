# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

places = {
    '山东': [117.000923, 36.675807],
    '河北': [115.48333, 38.03333],
    '吉林': [125.35000, 43.88333],
    '黑龙江': [127.63333, 47.75000],
    '辽宁': [123.38333, 41.80000],
    '内蒙古': [111.670801, 41.818311],
    '新疆': [87.68333, 43.76667],
    '甘肃': [103.73333, 36.03333],
    '宁夏': [106.26667, 37.46667],
    '山西': [112.53333, 37.86667],
    '陕西': [108.95000, 34.26667],
    '河南': [113.65000, 34.76667],
    '安徽': [117.283042, 31.86119],
    '江苏': [119.78333, 32.05000],
    '浙江': [120.20000, 30.26667],
    '福建': [118.30000, 26.08333],
    '广东': [113.23333, 23.16667],
    '江西': [115.90000, 28.68333],
    '海南': [110.35000, 20.01667],
    '广西': [108.320004, 22.82402],
    '贵州': [106.71667, 26.56667],
    '湖南': [113.00000, 28.21667],
    '湖北': [114.298572, 30.584355],
    '四川': [104.06667, 30.66667],
    '云南': [102.73333, 25.05000],
    '西藏': [91.00000, 30.60000],
    '青海': [96.75000, 36.56667],
    '天津': [117.20000, 39.13333],
    '上海': [121.55333, 31.20000],
    '重庆': [106.45000, 29.56667],
    '北京': [116.41667, 39.91667],
    '台湾': [121.30, 25.03],
    '香港': [114.10000, 22.20000],
    '澳门': [113.50000, 22.20000],
}
name = []
lon = []
lat = []
for k, v in places.items():
    name.append(k)
    lon.append(v[0])
    lat.append(v[1])

traces = []
traces.append(go.Scattermapbox(
    mode="markers",
    lon=lon,
    lat=lat,
    marker={'size': 10}
))

fig = go.Figure(traces)

# fig.add_trace(go.Scattermapbox(
#     mode = "markers+lines",
#     lon = [-50, -60,40],
#     lat = [30, 10, -20],
#     marker = {'size': 10}))

fig.update_layout(
    margin={'l': 0, 't': 0, 'b': 0, 'r': 0},

    mapbox={
        'style': "stamen-terrain",
        'center': {'lon': places['浙江'][0], 'lat': places['浙江'][1]},
        'zoom': 3
    })

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='China map'),

    html.Div(children='''
        A China map app for shortest rode.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig

    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
