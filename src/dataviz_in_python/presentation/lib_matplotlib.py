import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.backends.backend_agg import FigureCanvas  # not needed for mpl >= 3.1
from matplotlib.figure import Figure
import panel as pn

from dataviz_in_python import config

config.configure("vega", url="lib_matplotlib", title="Matplotlib")

TEXT = """
# Matplotlib: Static plots in Python without limits

[Matplotlib](https://matplotlib.org/) is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible. Matplotlib is the most used plotting library in Python.

Matplotlib only supports interactivity to a limited extent compared to Altair, Bokeh, HoloViews and Plotly. So personally I normally don't use it.

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/lib_matplotlib.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()


def get_plot(theme="default"):
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

plot = get_plot(theme=config.get_theme())
pn.pane.Matplotlib(plot, height=600, sizing_mode="scale_height").servable()