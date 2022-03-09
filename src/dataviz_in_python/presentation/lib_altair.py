import altair as alt
import panel as pn
from vega_datasets import data

from dataviz_in_python import config

config.configure("vega", url="lib_altair", title="Altair")

TEXT = """
# Altair: Declarative Visualization in Python

[Altair](https://altair-viz.github.io/) is a declarative statistical visualization library for Python, based on Vega and Vega-Lite.

Traditionally Altair has been limited by data size. But [Vega Fusion](https://github.com/vegafusion/vegafusion/) is changing that. 
See also [Panel-VegaFusion](https://github.com/MarcSkovMadsen/panel-vegafusion).

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/lib_altair.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()


def get_plot(theme="default"):
    if theme == "dark":
        alt.themes.enable("dark")
    else:
        alt.themes.enable("default")

    return (
        alt.Chart(data.cars())
        .mark_circle(size=60)
        .encode(
            x="Horsepower",
            y="Miles_per_Gallon",
            color="Origin",
            tooltip=["Name", "Origin", "Horsepower", "Miles_per_Gallon"],
        )
        .properties(
            height="container",
            width="container",
        )
        .interactive()
    )


plot = get_plot(theme=config.get_theme())
pn.pane.Vega(plot, height=700, sizing_mode="stretch_both").servable()
