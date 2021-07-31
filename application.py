import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from skimage import data

img = data.chelsea()
fig = px.imshow(img)
fig.update_layout(dragmode="drawrect")
fig.add_shape(
    dict(type="rect", x0=130, x1=212, y0=80, y1=150, line_color="purple"),
    row="all",
    col="all",
)

fig.add_trace(go.Scatter(
    x=[212],
    y=[150],
    text=["Cat"],
    mode="text"
))

config = {
    "modeBarButtonsToAdd": [
        "drawline",
        "drawopenpath",
        "drawclosedpath",
        "drawcircle",
        "drawrect",
        "eraseshape",
    ]
}

app = dash.Dash(__name__)
application = app.server
app.layout = html.Div(
    [html.H3("Drag and draw annotations"), dcc.Graph(figure=fig, config=config),]
)

if __name__ == "__main__":
    app.run_server()
