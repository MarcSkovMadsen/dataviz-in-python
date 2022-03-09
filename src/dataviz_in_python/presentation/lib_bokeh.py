import numpy as np
import panel as pn

from bokeh.plotting import figure
from scipy.integrate import odeint

pn.extension(sizing_mode="stretch_width")

accent_base_color = "#DAA520"
template = pn.template.FastListTemplate(
    site="Awesome Panel",
    title="Bokeh",
    accent_base_color=accent_base_color,
    header_background=accent_base_color,
    header_accent_base_color="white",
)
theme = "dark" if template.theme == pn.template.DarkTheme else "default"


def get_plot(theme="default", accent_base_color="blue"):
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

plot = get_plot(theme=theme, accent_base_color=accent_base_color)
component = pn.pane.Bokeh(plot, height=500, sizing_mode="stretch_both")
template.main.append(component)
template.servable()