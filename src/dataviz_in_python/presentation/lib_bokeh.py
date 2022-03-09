import numpy as np
import panel as pn

from bokeh.plotting import figure
from scipy.integrate import odeint

from dataviz_in_python import config

config.configure(title="Bokeh", url="lib_bokeh")

TEXT = """
# Bokeh: Interactive Visualization in the Browser

[Bokeh](https://docs.bokeh.org/en/latest/) is a Python library for creating interactive visualizations for modern web browsers.

I think Bokeh appeals to users with specialized, scientific or streaming use cases. Bokeh has a lot of "specialized" tools for selecting or adding data points.

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/lib_bokeh.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()

def get_plot():
    sigma = 10
    rho = 28
    beta = 8.0 / 3
    theta = 3 * np.pi / 4

    def lorenz(xyz, t):
        x, y, z = xyz
        x_dot = sigma * (y - x)
        y_dot = x * rho - x * z - y
        z_dot = x * y - beta * z
        return [x_dot, y_dot, z_dot]

    initial = (-10, -7, 35)
    t = np.arange(0, 100, 0.006)

    solution = odeint(lorenz, initial, t)

    x = solution[:, 0]
    y = solution[:, 1]
    z = solution[:, 2]
    xprime = np.cos(theta) * x - np.sin(theta) * y

    colors = [
        "#C6DBEF",
        "#9ECAE1",
        "#6BAED6",
        "#4292C6",
        "#2171B5",
        "#08519C",
        "#08306B",
    ]

    plot = figure(
        title="Lorenz attractor example", tools=["pan,wheel_zoom,box_zoom,reset,hover"]
    )

    plot.multi_line(
        np.array_split(xprime, 7),
        np.array_split(z, 7),
        line_color=colors,
        line_alpha=0.8,
        line_width=1.5,
    )
    return plot

plot = get_plot()
pn.pane.Bokeh(plot, height=700, sizing_mode="stretch_both").servable()
