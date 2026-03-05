import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import iplot



df1 = pd.read_csv('RealVals2025.csv', on_bad_lines='skip', sep=';', usecols=['Representativt dygn', 'Lufttemperatur'])
df2 = pd.read_csv('Predicted2025.csv', on_bad_lines='skip', sep=';', usecols=['Representativt dygn', 'Lufttemperatur'])

dfs = {'Uppmätt Temp':df1, 'Förutspådd Temp':df2}
fig = go.Figure()

for i in dfs:
    fig = fig.add_trace(go.Scatter(x = dfs[i]["Representativt dygn"],
                                   y = dfs[i]["Lufttemperatur"], 
                                   name = i))
    
fig.update_layout(font_size=30,
    xaxis=dict(
        tickfont=dict(
            family='Arial',
            size=30,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        tickfont=dict(
            family='Arial',
            size=30,
            color='rgb(82, 82, 82)',
        ),
    ),
)
fig.show()


df3= pd.read_csv('Predicted2025New.csv', on_bad_lines='skip', sep=';', usecols=['Representativt dygn', 'R2'])
fig2 = go.Figure()
fig2 = fig2.add_trace(go.Scatter(x = df3["Representativt dygn"], y = df3["R2"], name = "R2", mode = "markers", line=dict(color = "firebrick")))


fig2.update_layout(font_size=30,
    xaxis=dict(
        tickfont=dict(
            family='Arial',
            size=30,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        tickfont=dict(
            family='Arial',
            size=30,
            color='rgb(82, 82, 82)',
        ),
    ),
)
fig2.show()
