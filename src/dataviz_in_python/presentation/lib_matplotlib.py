import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.backends.backend_agg import     FigureCanvas  # not needed for mpl >= 3.1
from matplotlib.figure import Figure
import panel as pn

pn.extension(sizing_mode="stretch_width")

accent_base_color = "#DAA520"
template = pn.template.FastListTemplate(
    site="Awesome Panel",
    title="Matplotlib",
    accent_base_color=accent_base_color,
    header_background=accent_base_color,
    header_accent_base_color="white",
)
theme = "dark" if template.theme == pn.template.DarkTheme else "default"


def get_plot(theme="default", accent_base_color="blue"):
    plt.style.use("default")
    if theme == "dark":
        plt.style.use("dark_background")
    Y, X = np.mgrid[-3:3:100j, -3:3:100j]
    U = -1 - X ** 2 + Y
    V = 1 + X - Y ** 2
    speed = np.sqrt(U * U + V * V)

    fig0 = Figure(figsize=(12, 6))
    ax0 = fig0.subplots()
    FigureCanvas(fig0)  # not needed for mpl >= 3.1

    strm = ax0.streamplot(X, Y, U, V, color=U, linewidth=2, cmap=cm.autumn)
    fig0.colorbar(strm.lines)
    return fig0

plot = get_plot(theme=theme, accent_base_color=accent_base_color)
component = pn.pane.Matplotlib(plot, height=500, sizing_mode="stretch_both")
template.main.append(component)
template.servable()